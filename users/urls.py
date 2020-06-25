from django.urls import path

from .views import SignUp

app_name = "users"
urlpatterns = [
    path("accounts/", SignUp.as_view(), name="signup"),
]
