from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager

class User(AbstractUser):
    referral_token = models.CharField(max_length=255)
    # redefining standard user manager
    objects = UserManager()
    # add new required field "referral_token"
    REQUIRED_FIELDS = ["referral_token", "email"]