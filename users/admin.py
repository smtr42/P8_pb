"""Admin specifications to use the User custom model."""
from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from users.forms import UserChangeForm, UserCreationForm


class UserAdmin(BaseUserAdmin):
    """Update admin.py to use custom user model."""

    model = User
    form = UserChangeForm
    add_form = UserCreationForm


admin.site.register(User, UserAdmin)
