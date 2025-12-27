// DOM Elements
const chatForm = document.getElementById("chatForm");
const userInput = document.getElementById("userInput");
const chatBox = document.getElementById("chatBox");
const voiceBtn = document.getElementById("voiceBtn");
const ttsToggle = document.getElementById("ttsToggle");

let ttsEnabled = false;
let recognizer = null;
let listening = false;
let micStream = null;

// Mic button image
const micImg = document.createElement("img");
micImg.src = "/static/images/mic.png";
micImg.style.width = "30px";
micImg.style.height = "30px";
micImg.alt = "Microphone";
voiceBtn.innerHTML = "";
voiceBtn.appendChild(micImg);

// Speech Recognition Setup
const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;

if (SpeechRecognition) {
    recognizer = new SpeechRecognition();
    recognizer.lang = "en-US";
    recognizer.continuous = true;
    recognizer.interimResults = true;

    recognizer.onstart = () => voiceBtn.classList.add("listening");
    recognizer.onend = () => voiceBtn.classList.remove("listening");

    recognizer.onresult = (event) => {
        let text = "";
        for (let i = event.resultIndex; i < event.results.length; i++) {
            text += event.results[i][0].transcript;
        }
        userInput.value = text.trim();

        if (event.results[event.results.length - 1].isFinal) {
            setTimeout(() => chatForm.requestSubmit(), 300);
        }
    };

    recognizer.onerror = () => stopListening();
}

voiceBtn.addEventListener("click", () => {
    if (!SpeechRecognition) return;
    listening ? stopListening() : startListening();
});

function startListening() {
    navigator.mediaDevices.getUserMedia({ audio: true })
        .then(stream => {
            micStream = stream;
            recognizer.start();
            listening = true;
        })
        .catch(() => stopListening());
}

function stopListening() {
    if (recognizer && listening) recognizer.stop();
    if (micStream) micStream.getTracks().forEach(t => t.stop());
    micStream = null;
    listening = false;
    voiceBtn.classList.remove("listening");
}

// Text-to-Speech
function speakText(text) {
    if (!ttsEnabled || !window.speechSynthesis) return;
    window.speechSynthesis.cancel();
    const utter = new SpeechSynthesisUtterance(text);
    utter.lang = "en-US";
    window.speechSynthesis.speak(utter);
}

ttsToggle.addEventListener("click", () => {
    ttsEnabled = !ttsEnabled;
    ttsToggle.classList.toggle("active", ttsEnabled);
});

// Format Time
function formatTime() {
    return new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
}

// Add Message
function addMessage(text, sender) {
    const wrapper = document.createElement("div");
    wrapper.classList.add("msg-wrapper", sender);

    const avatar = document.createElement("div");
    avatar.className = sender === "user" ? "user-avatar" : "bot-avatar";

    const msgDiv = document.createElement("div");
    msgDiv.classList.add("message");
    msgDiv.textContent = text;

    const time = document.createElement("div");
    time.classList.add("timestamp");
    time.textContent = formatTime();

    sender === "user"
        ? wrapper.append(time, msgDiv, avatar)
        : wrapper.append(avatar, msgDiv, time);

    chatBox.appendChild(wrapper);
    chatBox.scrollTop = chatBox.scrollHeight;
}


// Typing Indicator
function addTypingIndicator() {
    const wrapper = document.createElement("div");
    wrapper.classList.add("msg-wrapper", "bot");
    wrapper.id = "typing-indicator";

    const avatar = document.createElement("div");
    avatar.className = "bot-avatar";

    const typing = document.createElement("div");
    typing.classList.add("message", "typing");

    for (let i = 0; i < 3; i++) {
        typing.appendChild(document.createElement("span"));
    }

    wrapper.append(avatar, typing);
    chatBox.appendChild(wrapper);
    chatBox.scrollTop = chatBox.scrollHeight;
    return wrapper;
}


// Main: Send Message
chatForm.addEventListener("submit", async (e) => {
    e.preventDefault();
    const msg = userInput.value.trim();
    if (!msg) return;

    addMessage(msg, "user");
    userInput.value = "";

    const typing = addTypingIndicator();

    const isFirstMessage = (currentSessionId === "None" || !currentSessionId);
    const url = isFirstMessage 
        ? "/api/chat/new/chat" 
        : `/api/chat/${currentSessionId}/chat`;

    try {
        const res = await fetch(url, {
            method: "POST",
            credentials: 'include',
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCookie("csrftoken"),
                "X-Requested-With": "XMLHttpRequest"
            },  
            body: JSON.stringify({ message: msg })
        });

        const data = await res.json();
        typing.remove();

        if (res.ok && data.response) {
            // If this was the first message, update session ID and URL
            if (isFirstMessage && data.session_id) {
                currentSessionId = data.session_id;
                document.getElementById("currentSessionId").value = currentSessionId;
                history.pushState({}, '', `/chat/${currentSessionId}/`);
            }

            addMessage(data.response, "bot");
            if (ttsEnabled) speakText(data.response);
        } else {
            addMessage("Error: Could not get response.", "bot");
        }
    } catch (err) {
        typing.remove();
        addMessage("Network error. Check your connection.", "bot");
        console.error(err);
    }
});

// Theme Toggle
document.addEventListener("DOMContentLoaded", () => {
    const body = document.body;
    const tdnn = document.querySelector(".tdnn");
    const moon = document.querySelector(".moon");

    if (localStorage.getItem("theme") === "light") {
        body.classList.add("light");
        moon.classList.add("sun");
        tdnn.classList.add("day");
    }

    tdnn.addEventListener("click", () => {
        body.classList.toggle("light");
        moon.classList.toggle("sun");
        tdnn.classList.toggle("day");
        localStorage.setItem("theme", body.classList.contains("light") ? "light" : "dark");
    });
});

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
