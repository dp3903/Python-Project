from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class myuser(AbstractUser):
    profile_img = models.CharField( max_length=50 )