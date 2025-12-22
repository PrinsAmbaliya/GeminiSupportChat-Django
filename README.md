# Gemini-Support-Bot-Django

A **Django-based Customer Support Chatbot** powered by Google Gemini AI API. Users can sign up, sign in, create chat sessions, and interact with a chatbot for assistance. This project demonstrates a full-stack Django application integrated with an AI-powered chatbot for customer support.

---

## Features

- User authentication (Sign Up / Sign In)
- Create and manage chat sessions
- Real-time AI chatbot responses using Google Gemini
- Session-based chat history
- Session-based chat title
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

---

## Usage

-Sign Up / Sign In: Users can create an account and log in.

-Chat Interface: Users can create new chat sessions and send messages.

-AI Responses: Chatbot responds using Google Gemini AI.

-Session Management: Users can view previous chat sessions and messages.

---

## API Endpoints

| Endpoint                      | Method | Description                |
| ----------------------------- | ------ | -------------------------- |
| `/api/register`               | POST   | Register a new user        |
| `/api/login`                  | POST   | Login user                 |
| `/api/session/create`         | POST   | Create a new chat session  |
| `/api/chat/<session_id>/chat` | POST   | Send message to chatbot    |
| `/api/session/user/<user_id>` | GET    | Get all sessions of a user |

---

## Admin Panel

- Access the Django admin panel at: /admin/
- Login with the superuser credentials you created
- Manage users, sessions, and chat messages from the admin interface

---

## Screenshots

### 1. SignUp Page
<img width="1919" height="1019" alt="Screenshot 2025-12-22 093420" src="https://github.com/user-attachments/assets/ec5402a7-28d4-468c-9cfe-0452d3ce5bde" />

### 2. Save User Details
<img width="1918" height="1017" alt="Screenshot 2025-12-22 093514" src="https://github.com/user-attachments/assets/7f4790fa-16fa-4981-bb24-8c8b55473699" />

### 3. SignIn Page
<img width="1919" height="1020" alt="Screenshot 2025-12-22 093740" src="https://github.com/user-attachments/assets/16a6cac1-2f46-4526-aab1-9b63cbde8c23" />

### 4. ChatBot In Dark Mode
<img width="1919" height="1020" alt="Screenshot 2025-12-22 093912" src="https://github.com/user-attachments/assets/f1f4b404-8bc1-42ae-a02d-cffce94877f8" />

### 5. ChatBot In Light Mode
<img width="1919" height="1019" alt="Screenshot 2025-12-22 093950" src="https://github.com/user-attachments/assets/1b6bc1f3-b583-4fbb-86e4-e79640437b77" />

### 6. Save User Session Id Of Every New Chats
<img width="1919" height="1021" alt="Screenshot 2025-12-22 095347" src="https://github.com/user-attachments/assets/141bd341-5df4-4209-a1dd-1694eea19477" />

### 7. Save User Chats
<img width="1915" height="1021" alt="Screenshot 2025-12-22 095502" src="https://github.com/user-attachments/assets/2e8fdcc0-432f-4942-a0b9-89ba8eedd1e1" />

---

## Author

Prins Ambaliya

GitHub: PrinsAmbaliya

LinkedIn: https://www.linkedin.com/in/prins-ambaliya-bb7546367
