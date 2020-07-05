from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import UserCreationForm


class SignUp(CreateView):
    # form_class = UserCreationForm
    # success_url = reverse_lazy("accounts/login")
    # template_name = "account/signup.html"
    pass