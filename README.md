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

```bash
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
├── templates/                # Common templates
├── .env                      # Environment variables (Gemini API Key)
└── requirements.txt
```
---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Gemini-Support-Bot-Django.git
cd Gemini-Support-Bot-Django
```
### 2. Create and activate a virtual environment

```bash
python -m venv venv
# On macOS/Linux
source venv/bin/activate
# On Windows
venv\Scripts\activate
```
### 3. Configure environment variables

```bash
GEMINI_API_KEY=your_gemini_api_key_here
```
### 4. Apply database migrations

```bash
python manage.py makemigrations
python manage.py migrate
```
### 5. Create a superuser (for admin access)

```bash
python manage.py createsuperuser
```
### 6. Run the development server

```bash
python manage.py runserver
```
Open the application in your browser:
```bash
http://127.0.0.1:8000
```
