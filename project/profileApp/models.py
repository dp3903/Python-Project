from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    profile_img = models.ImageField(upload_to="../profileImages/", height_field=None, width_field=None, max_length=None)
    def __str__(self):
        return self.id + " " + self.username