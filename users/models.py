from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """ Custom user model derived from Abstractuser.
    This will be the user we will reference to. """
    pass
