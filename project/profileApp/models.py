from django.db import models
from django.contrib.auth.models import AbstractUser

class Users(AbstractUser):
    profile_img = models.ImageField(upload_to='profile_img')
    def __str__(self):
        return self.id + " " + self.username