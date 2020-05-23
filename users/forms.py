"""Define forms and specify custom User model."""
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from django.contrib.auth import get_user_model
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """Custom creation form."""

    class Meta(UserCreationForm.Meta):
        """Override the default user with custom user."""
        model = CustomUser
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):
    """Custom change form."""

    class Meta(UserChangeForm.Meta):
        """Override the default user with custom user."""
        model = CustomUser
        fields = UserChangeForm.Meta.fields
