# GeminiSupportBot-Django

A **Django-based Customer Support Chatbot** powered by **Google Gemini (gemini-3-flash-preview)**.  
Users can sign up, sign in, create chat sessions, and interact with an AI chatbot.  
The project uses **PostgreSQL** for persistent data storage and supports automatic chat title generation.

---

## Features

- User Authentication (Sign Up / Sign In)
- Session-based chat system
- Automatic chat title generation from user query
- Context-aware AI responses using Google Gemini
- Persistent chat history using PostgreSQL
- Light & Dark mode UI
- Django Admin panel support
- REST API endpoints
- Postman API testing support

---

## Tech Stack

- Backend: Django, Django REST Framework
- AI Model: Google Gemini (gemini-3-flash-preview)
- Database: PostgreSQL
- Frontend: HTML, CSS, JavaScript
- API Testing: Postman
  
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

- Sign Up / Sign In: Users can create an account and log in.
- Chat Interface: Users can create new chat sessions and send messages.
- AI Responses: Chatbot responds using Google Gemini AI.
- Session Management: Users can view previous chat sessions and messages.

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
<img width="1919" height="1020" alt="image" src="https://github.com/user-attachments/assets/935d2b63-6782-477c-bd53-5aaffd19a6a5" />

### 2. Save User Details In Admin
<img width="1919" height="1020" alt="image" src="https://github.com/user-attachments/assets/db3a6fe5-6b82-4c31-9635-f1da781ef043" />

### 3. SignIn Page
<img width="1919" height="1020" alt="image" src="https://github.com/user-attachments/assets/93fc6ce8-6253-4afb-b0bc-d0613a211a60" />

### 4. Save User Login Details In Admin
<img width="1919" height="1017" alt="image" src="https://github.com/user-attachments/assets/ef117aaa-cc6c-464b-8b2d-388d886a7a6e" />

### 5. ChatBot In Dark Mode
<img width="1919" height="1020" alt="image" src="https://github.com/user-attachments/assets/55c774e8-a3e5-4a85-adfb-a582920195d8" />

### 6. ChatBot In Light Mode
<img width="1919" height="1017" alt="image" src="https://github.com/user-attachments/assets/88ef7fc7-c6cd-49e5-a270-8ffe0e46539c" />

### 7. Save User Session Id Of Every New Chats
<img width="1919" height="1017" alt="image" src="https://github.com/user-attachments/assets/7c15cd13-8735-4fab-b43b-8f6bb9292a94" />

### 8. Save User Chats
<img width="1919" height="1021" alt="image" src="https://github.com/user-attachments/assets/6c045407-dd97-4309-8a31-b52d032cf4cd" />

### 9. API Testing Of SignUp In Postman
<img width="1919" height="1018" alt="image" src="https://github.com/user-attachments/assets/402e55ac-0a2d-46d6-ae82-656f118ddd24" />

### 10. API Testing Of SignIn In Postman
<img width="1919" height="1021" alt="image" src="https://github.com/user-attachments/assets/da4bbe30-d10f-4006-8d0f-39b6049a781d" />

### 11. API Testing Of Create Session Id In Postman
<img width="1919" height="1016" alt="image" src="https://github.com/user-attachments/assets/f2a2d5a3-02b7-47f3-8a68-c0b5833dfde5" />

### 12. API Testing Of Save Chats Of Session Id In Postman
<img width="1919" height="1016" alt="image" src="https://github.com/user-attachments/assets/f59d8ad9-95d7-4c88-8ba0-a82b9bd6df26" />

### 13. API Testing Of Save Chats Of Session Id For New Chat In Postman
<img width="1919" height="1018" alt="image" src="https://github.com/user-attachments/assets/8529fc70-756f-4418-a054-f28855228bb4" />


---

## Author

Prins Ambaliya

GitHub: PrinsAmbaliya

LinkedIn: https://www.linkedin.com/in/prins-ambaliya-bb7546367
