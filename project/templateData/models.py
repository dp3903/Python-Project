from django.db import models
from django.contrib.auth.models import AbstractUser
from profileApp.models import Users


# class Users(AbstractUser):
#     profile_img = models.ImageField(upload_to="../profileImages/", height_field=None, width_field=None, max_length=None)
#     def __str__(self):
#         return self.id + " " + self.username


class Template(models.Model):
    templateId = models.CharField(max_length=10,primary_key=True)
    templateName = models.CharField(max_length=20)
    UID = models.ForeignKey(Users, on_delete=models.CASCADE)
    description = models.TextField()
    date = models.DateField()
    templateZip = models.FileField()
    totaldownloads = models.IntegerField()

    def __str__(self):
        return self.templateId + " " + self.templateName + " " + self.UID + " " + self.description + " " + self.date + " " + self.templateZip + " " + self.totaldownloads
    

class AppLogs(models.Model):
    CHOICES = (
        ("upload", "upload"),
        ("download", "download"),
        ("delete", "delete"),
        ("new", "new"),
        ("default", "default"),
    )
    transaction_type = models.CharField(max_length=10,choices=CHOICES,default="default",blank=True)
    TID = models.ForeignKey(Template, on_delete=models.CASCADE)
    UID = models.ForeignKey(Users, on_delete=models.CASCADE)
    def __str__(self):
        return self.transaction_type + " " + self.UID + " " + self.TID
    