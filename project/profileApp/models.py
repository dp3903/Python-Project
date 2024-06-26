from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    profile_img = models.ImageField(upload_to="static/", height_field=None, width_field=None, max_length=None, null = True, blank = True)
    def __str__(self):
        return str(self.id) + " " + self.username