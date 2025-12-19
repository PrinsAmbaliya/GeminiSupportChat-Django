from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from . views import UserSignUp,UserSignIn,SessionCreateView,UserSessionsView,ChatCreateView,UserSignUpPage,UserSignInPage,UserChatPage,ChatCreateNewView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('signupPage/',views.UserSignUpPage, name="signup_Page"),
    path('signinPage/',views.UserSignInPage,name = "signin_Page"),
    path('chat/', views.UserChatPage, name='chat_page'),
    path('chat/<uuid:session_id>/', views.UserChatPage, name='chat_page_with_id'),

    path('api/register',UserSignUp.as_view(), name="Register"),
    path('api/login',UserSignIn.as_view(), name="Login"),
    path('api/session/create',SessionCreateView.as_view(), name="ChatBot"),
    path('api/session/user/<int:user_id>',UserSessionsView.as_view(), name = "user_sessions"),
    path('api/chat/<uuid:session_id>/chat',ChatCreateView.as_view(),name="Create_chat"),
    path('api/chat/new/chat',ChatCreateNewView.as_view(),name="create_new_chat")
] 

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])