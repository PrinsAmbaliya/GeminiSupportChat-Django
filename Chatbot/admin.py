from django.contrib import admin
from .models import Session, Chat
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

admin.site.unregister(User)


# @admin.register(User)
class CustomerUserAdmin(UserAdmin):
    list_display = (
        "id",
        "username",
        "email",
        "first_name",
        "last_name",
        "is_staff",
        "is_active",
        "date_joined",
        "last_login",
    )
    search_fields = (
        "id",
        "username",
        "email",
        "first_name",
    )

    list_filter = (
        "is_staff",
        "is_active",
        "date_joined",
        "last_login",
    )


admin.site.register(User, CustomerUserAdmin)


class SessionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "username",
        "session_id",
        "title",
        # 'description',
        "created_at",
    )
    search_fields = ("title", "username__username", "session_id", "id")
    list_filter = ("created_at",)


admin.site.register(Session, SessionAdmin)


class ChatAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "username",
        "session_id",
        "message",  
        "response",
        "timestamp",
    )
    list_filter = ("timestamp",)
    search_fields = ("session__username__username", "session__session_id", "id")

    def username(self, obj):
        return obj.session.username.username

    username.admin_order_field = "session__username__username"
    username.short_description = "Username"

    def session_id(self, obj):
        return obj.session.session_id

    session_id.admin_order_field = "session__session_id"
    session_id.short_description = "Session ID"


admin.site.register(Chat, ChatAdmin)
