"""Definition of the custom user model."""
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    Custom user model derived from Abstractuser.
    This will be the user referenced to.
    """
    pass
