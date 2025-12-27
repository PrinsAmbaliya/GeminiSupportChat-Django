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
<img width="1919" height="1019" alt="Screenshot 2025-12-22 093420" src="https://github.com/user-attachments/assets/ec5402a7-28d4-468c-9cfe-0452d3ce5bde" />

### 2. Save User Details
<img width="1919" height="962" alt="image" src="https://github.com/user-attachments/assets/1f2b4c33-fce4-47c3-8005-1a96e3edd908" />

### 3. SignIn Page
<img width="1919" height="1020" alt="Screenshot 2025-12-22 093740" src="https://github.com/user-attachments/assets/16a6cac1-2f46-4526-aab1-9b63cbde8c23" />

### 4. ChatBot In Dark Mode
<img width="1919" height="965" alt="image" src="https://github.com/user-attachments/assets/5cc6f6c4-35c7-49e6-9f71-ec1f67eebf86" />

### 5. ChatBot In Light Mode
<img width="1919" height="967" alt="image" src="https://github.com/user-attachments/assets/69486fed-a86c-496e-bc1a-6cf10af3810a" />

### 6. Save User Session Id Of Every New Chats
<img width="1919" height="955" alt="image" src="https://github.com/user-attachments/assets/32196e71-92c8-43d0-938f-f6e089048629" />

### 7. Save User Chats
<img width="1919" height="958" alt="image" src="https://github.com/user-attachments/assets/861a863a-2e7b-4ba2-b558-a5224698987f" />

### 8. API Testing Of SignUp In Postman
<img width="1919" height="1017" alt="Screenshot 2025-12-22 103204" src="https://github.com/user-attachments/assets/25f59950-1d6a-4e7d-997d-f249eca2b3b9" />

### 9. API Testing Of SignIn In Postman
<img width="1918" height="1019" alt="image" src="https://github.com/user-attachments/assets/d83cbc85-5b69-46cb-b385-1d35c3bf877c" />

### 10. API Testing Of Create Session Id In Postman
<img width="1919" height="1016" alt="image" src="https://github.com/user-attachments/assets/dc90ff57-84a8-4861-9bfa-88bbe31e5de6" />

### 11. API Testing Of Save Chats Of Session Id In Postman
<img width="1919" height="1014" alt="image" src="https://github.com/user-attachments/assets/5430da8b-851f-4555-9f29-5ea4f6639e20" />

---

## Author

Prins Ambaliya

GitHub: PrinsAmbaliya

LinkedIn: https://www.linkedin.com/in/prins-ambaliya-bb7546367
