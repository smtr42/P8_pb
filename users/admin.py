from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from users.forms import UserChangeForm, UserCreationForm


# admin.site.register(User, UserAdmin)


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
