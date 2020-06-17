"""Definition of the custom user model."""
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

class User(AbstractUser):
    """
    Custom user model derived from Abstractuser.
    This will be the user referenced to.
    """
    first_name = models.CharField(_("Prénom"), max_length=100)
    email = models.EmailField(_("Adresse mail"), max_length=100)

    def __str__(self):
        return self.email
    
