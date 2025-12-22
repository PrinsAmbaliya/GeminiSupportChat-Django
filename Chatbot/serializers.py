from rest_framework import serializers
from .models import Session, Chat
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
import re
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()


class SignUpSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(
        write_only=True, required=False, style={"input_type": "password"}
    )

    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "username",
            "email",
            "password",
            "confirm_password",
        ]
        extra_kwargs = {
            "username": {"required": True, "allow_blank": False},
            "email": {"required": True, "allow_blank": False},
            "password": {"write_only": True, "required": True},
        }

    def validate_password(self, password):
        if len(password) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters!")
        if not re.search(r"[A-Z]", password):
            raise serializers.ValidationError(
                "Password must contain at least one uppercase letter!"
            )
        if not re.search(r"[a-z]", password):
            raise serializers.ValidationError(
                "Password must contain at least one lowercase letter!"
            )
        if not re.search(r"[0-9]", password):
            raise serializers.ValidationError(
                "Password must contain at least one number!"
            )
        if not re.search(r"[!@#$%^&*()_+\-=\[\]{};'\":\\|,.<>/?]", password):
            raise serializers.ValidationError(
                "Password must contain at least one special character!"
            )
        return password

    def validate(self, data):
        password = data.get("password")
        confirm_password = data.get("confirm_password")
        if password and not confirm_password:
            raise serializers.ValidationError(
                {"confirm_password": "Confirm password is required."}
            )
        if password != confirm_password:
            raise serializers.ValidationError(
                {"confirm_password": "Confirm_Passwords do not match with Password!"}
            )
        return data

    def create(self, validated_data):
        validated_data.pop("confirm_password")
        user = User.objects.create_user(
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
        )
        return user


class SignInSerializer(serializers.Serializer):
    username_or_email = serializers.CharField(required=True, allow_blank=False)
    password = serializers.CharField(
        required=True,
        style={"input_type": "password"},
    )
    user = None

    def validate(self, data):
        request = self.context.get("request")
        username = data.get("username_or_email")
        password = data.get("password")

        if not username:
            raise serializers.ValidationError(
                {"Username or Email": "Username or Email is required."}
            )
        if not password:
            raise serializers.ValidationError({"Password": "Password is required."})
        user = None
        if "@" in username:
            try:
                username = User.objects.get(email=username)
                user = authenticate(request, username=username, password=password)
            except User.DoesNotExist:
                raise serializers.ValidationError({"Email": "Invalid Email!"})
        if username:
            try:
                username = User.objects.get(username=username)
                user = authenticate(request, username=username, password=password)
            except User.DoesNotExist:
                raise serializers.ValidationError({"Username": "Invalid Username!"})
        if user is None:
            raise serializers.ValidationError({"Password": "Invalid Password!"})
        data["user"] = user
        return data


class SessionSerializer(serializers.ModelSerializer):
    username = serializers.SlugRelatedField(
        slug_field="username", queryset=User.objects.all()
    )

    class Meta:
        model = Session
        fields = ["id", "session_id", "title", "description", "created_at", "username"]


class UserSessionsSerializer(serializers.ModelSerializer):
    username = serializers.SlugRelatedField(slug_field="username", read_only=True)

    class Meta:
        model = Session
        fields = ["id", "session_id", "title", "description", "created_at", "username"]


genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

SYSTEM_PROMPT = """
You are a professional and empathetic customer support assistant.

Role:
- Assist users with accounts, software, technical issues, and general support inquiries.
- Provide clear, concise, and solution-focused guidance.

Communication Guidelines:
- Respond in friendly, professional English using short, clear paragraphs.
- Avoid starting every message with an acknowledgment or apology unless contextually necessary.
- Focus on giving actionable solutions directly.
- Ask clarifying questions only when essential (maximum 3).

Response Style:
- Provide actionable, step-by-step guidance in a natural, readable flow.
- Keep responses concise but informative.
- Escalate politely if the issue cannot be resolved with the provided information.

Accuracy and Safety:
- Do not speculate or provide unverified information.
- Recommend checking logs, credentials, configurations, or permissions when relevant.

Conversation Awareness:
- Maintain context using previous messages.
- Avoid repeating explanations unless clarification is requested.
- Ensure continuity and consistency across the conversation.

Goal:
- Resolve the user’s issue efficiently while keeping the reply direct, helpful, and friendly.
"""


model = genai.GenerativeModel(
    model_name="gemini-3-flash-preview", system_instruction=SYSTEM_PROMPT
)

title_model = genai.GenerativeModel(model_name="gemini-3-flash-preview")


class ChatSerializer(serializers.ModelSerializer):
    response = serializers.CharField(required=False)
    session = serializers.PrimaryKeyRelatedField(
        queryset=Session.objects.all(), required=True
    )

    class Meta:
        model = Chat
        fields = ["id", "session", "message", "response", "timestamp"]

    def validate(self, data):
        message = data.get("message", "").strip()
        if not message:
            raise serializers.ValidationError({"message": "Message cannot be empty!"})
        return data

    def create(self, validated_data):
        session = validated_data["session"]
        message = validated_data["message"].strip()

        is_first_message = not Chat.objects.filter(session=session).exists()

        previous_chats = Chat.objects.filter(session=session).order_by("timestamp")
        conversation = SYSTEM_PROMPT.strip() + "\n\n"
        for chat in previous_chats:
            conversation += f"User: {chat.message}\n"
            if chat.response:
                conversation += f"Assistant: {chat.response}\n"
        conversation += f"User: {message}\nAssistant:"

        reply = "Sorry, I could not respond right now. Please try again later."

        try:
            response = model.generate_content(
                conversation,
                generation_config=genai.GenerationConfig(
                    temperature=0.6,
                    max_output_tokens=1024,
                ),
            )

            if response.candidates and len(response.candidates) > 0:
                reply = "".join(
                    part.text
                    for part in response.candidates[0].content.parts
                    if hasattr(part, "text")
                ).strip()
                if not reply:
                    reply = "I received your message, but couldn't generate a proper response."
            else:
                if hasattr(response, "prompt_feedback") and response.prompt_feedback:
                    block_reason = getattr(
                        response.prompt_feedback, "block_reason", "UNKNOWN"
                    )
                    reply = f"Sorry, I can't assist with this due to content guidelines (Blocked: {block_reason})."
                else:
                    reply = "No response generated. Please try rephrasing."

        except Exception as e:
            error_msg = str(e).lower()
            print("GEMINI API ERROR:", repr(e))  # Full error in console

            if (
                "quota" in error_msg
                or "resource_exhausted" in error_msg
                or "429" in error_msg
            ):
                reply = "The AI service is temporarily busy due to high demand. Please try again in a few minutes."
            elif "billing" in error_msg:
                reply = "AI service requires billing to be enabled. Please contact the administrator."
            elif "model" in error_msg and "not found" in error_msg:
                reply = "AI model error. Please check configuration."
            elif "safety" in error_msg or "blocked" in error_msg:
                reply = "Sorry, I can't respond due to content safety guidelines."
            else:
                reply = "Network error. Please check your connection and try again."

        validated_data["response"] = reply
        chat = Chat.objects.create(**validated_data)

        if is_first_message and session.title == "New Chat":
            title = self.generate_title(message)
            session.title = title
            session.save()
            print(f"New session title generated: {title}")

        return chat

    def generate_title(self, first_message):
        prompt = f"""
    Generate a concise 3–7 word title for a customer support chat.
    User message: "{first_message}"
    Return only the title.
    """

        try:
            response = title_model.generate_content(
                prompt,
                generation_config=genai.GenerationConfig(
                    temperature=0.2,
                    max_output_tokens=30,
                ),
            )

            if response.candidates and len(response.candidates) > 0:
                title = (
                    "".join(
                        part.text
                        for part in response.candidates[0].content.parts
                        if hasattr(part, "text")
                    )
                    .strip()
                )

                if 2 <= len(title.split()) <= 10:
                    return title

            return "New Chat"

        except Exception as e:
            print("Title generation failed:", repr(e))
            return "New Chat"
