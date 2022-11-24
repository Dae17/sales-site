# from tkinter import CASCADE
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from datetime import date

from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
  photo = models.ImageField(upload_to='users', null=True)
  bio = models.TextField(max_length=250, blank = True)
  location = models.CharField(max_length=30, blank=True)
  
