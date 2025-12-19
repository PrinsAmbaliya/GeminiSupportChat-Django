from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from . serializers import SignInSerializer,SignUpSerializer,ChatSerializer,SessionSerializer
from . models import Chat,Session
import uuid 
import json
import re

class UserSignUp(APIView):
    parser_classes = [MultiPartParser, FormParser]
    authentication_classes =[]
    
    def get(self,request,*args, **kwargs):
        users = User.objects.all().order_by('id')
        serializer = SignUpSerializer(users,many=True)
        
        return Response({
            "message":"All User Deteils",
            "data": serializer.data
        })
        
        
    def post(self,request,*args, **kwargs):
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"User Sucessfully Add","data":serializer.data}, status=200)
        else:
            return Response(serializer.errors, status=400)
    
def UserSignUpPage(request):
    context = {"old_data": {}, "errors": {}, "non_field_errors": []}

    if request.method == "POST":
        serializer = SignUpSerializer(data=request.POST)

        if serializer.is_valid():
            serializer.save()
            return redirect('signin_Page')

        errors = {}
        non_field_errors = []

        for field, msgs in serializer.errors.items():
            if field in ["username", "email", "password", "confirm_password"]:
                errors[field] = msgs if isinstance(msgs, list) else [msgs]
            else:
                non_field_errors.extend(msgs if isinstance(msgs, list) else [msgs])

        context["errors"] = errors
        context["non_field_errors"] = non_field_errors
        context["old_data"] = request.POST

    return render(request, "signup.html", context)
    

class UserSignIn(APIView):
    parser_classes = [MultiPartParser,FormParser]
    authentication_classes = []
    def post(self,request,*args, **kwargs):
        serializer = SignInSerializer(data=request.data,context={"request": request})
        if serializer.is_valid():
            user = serializer.validated_data["user"]
            login(request,user)
            return Response({"message":f"{user.username} Sign In Sucessfully"},status=200)
        else:
            return Response(serializer.errors,status=400)
        
def UserSignInPage(request):
    context = {"old_data": {}, "non_field_errors": [], "errors": {}}

    if request.method == "POST":
        serializer = SignInSerializer(data=request.POST, context={"request": request})

        if serializer.is_valid():
            user = serializer.validated_data["user"]
            login(request, user)
            return redirect('chat_page')
        else:
            errors = {}
            non_field_errors = []

            for field, msgs in serializer.errors.items():
                if field in ["username_or_email", "password"]:
                    errors[field] = msgs if isinstance(msgs, list) else [msgs]
                else:
                    non_field_errors.extend(msgs if isinstance(msgs, list) else [msgs])

            context["errors"] = errors
            context["non_field_errors"] = non_field_errors
            context["old_data"] = request.POST
            
    context["signup_success"] = request.GET.get('signup_success') == '1'
    return render(request, "signin.html", context)

class SessionCreateView(APIView):
    parser_classes = [MultiPartParser,FormParser]
    authentication_classes = []
    def post(self,request,*args, **kwargs):
        serializer = SessionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Session created successfully", "data": serializer.data}, status=201)
        return Response(serializer.errors, status=400)

class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return

class ChatCreateView(APIView):
    authentication_classes = [CsrfExemptSessionAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = [JSONParser, MultiPartParser, FormParser]

    def post(self, request, session_id, *args, **kwargs):
        print("CURRENT USER:", request.user.username)  # Add .username for clarity
        print("IS AUTHENTICATED:", request.user.is_authenticated)
        try:
            session = Session.objects.get(
                session_id=session_id,
                username=request.user
            )
        except Session.DoesNotExist:
            return Response({"error": "Session not found"}, status=400)

        message = request.data.get("message", "").strip()
        if not message:
            return Response({"response": "Please type a message"}, status=400)

        serializer = ChatSerializer(data={
            "session": session.pk,
            "message": message
        })

        if serializer.is_valid():
            chat = serializer.save()
            return Response({"response": chat.response}, status=201)

        return Response(serializer.errors, status=400)

class ChatCreateNewView(APIView):
    authentication_classes = [CsrfExemptSessionAuthentication]
    permission_classes = [IsAuthenticated]  
    parser_classes = [JSONParser, MultiPartParser, FormParser]

    def post(self, request, *args, **kwargs):
        message = request.data.get("message", "").strip()
        if not message:
            return Response({"error": "Message cannot be empty"}, status=400)

        session = Session.objects.create(
            title="New Chat",
            description="",
            username=request.user   
        )

        serializer = ChatSerializer(data={
            "session": session.pk,
            "message": message
        }, context={'request': request})

        if serializer.is_valid():
            chat = serializer.save()
            return Response({
                "session_id": str(session.session_id),
                "response": chat.response
            }, status=201)

        return Response(serializer.errors, status=400)


def UserChatPage(request, session_id=None):
    if not request.user.is_authenticated:
        return redirect('signin_Page')

    if request.GET.get('new_chat'):
        return redirect('chat_page')  

    if session_id:
        try:
            session = Session.objects.get(session_id=session_id, username=request.user)
            chats = Chat.objects.filter(session=session).order_by('timestamp')
            context = {
                "session_id": str(session.session_id),
                "session_title": session.title,
                "chats": chats,
                "is_new_chat": False,
            }
            return render(request, "chatbot.html", context)
        except Session.DoesNotExist:
            return redirect('chat_page')

    return render(request, "chatbot.html", {
        "session_id": None,
        "session_title": "New Chat",
        "chats": [],
        "is_new_chat": True,
    })

class UserSessionsView(APIView):
    parser_classes = [MultiPartParser,FormParser]
    authentication_classes = []
    def get(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({"error": "User not found!"}, status=400)
        sessions = Session.objects.filter(username=user_id)
        if not sessions.exists():
            return Response({"message": "No sessions found for this user."}, status=200)
        serializer = SessionSerializer(sessions, many=True)
        return Response(serializer.data, status=200)