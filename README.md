# Gemini-Support-Bot-Django

A **Django-based Customer Support Chatbot** powered by Google Gemini AI API. Users can sign up, sign in, create chat sessions, and interact with a chatbot for assistance. This project demonstrates a full-stack Django application integrated with an AI-powered chatbot for customer support.

---

## Features

- User authentication (Sign Up / Sign In)
- Create and manage chat sessions
- Real-time AI chatbot responses using Google Gemini
- Session-based chat history
- Web interface for chatting with the bot
- REST API endpoints for programmatic access

---

## Project Structure

Gemini-Support-Bot-Django/
├── Chatbot/                  # Django app
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
│   └── templates/            # HTML templates
├── Chatbot/settings.py
├── Chatbot/urls.py
├── manage.py
├── static/                   # Static files for frontend
├── staticfiles/              # Generated static files (ignored in Git)
├── templates/                # Common templates
├── .env                      # Environment variables (Gemini API Key)
└── requirements.txt

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Gemini-Support-Bot-Django.git
cd Gemini-Support-Bot-Django
