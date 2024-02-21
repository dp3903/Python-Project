# from django.db import models
# from django.contrib.auth.models import User


# class Users(models.Model):
#     UID = models.CharField(max_length=10)
#     username = models.CharField(max_length=50)
#     password = models.CharField(max_length=50)
#     email = models.EmailField(max_length=254)
#     profile_img = models.ImageField(upload_to="../profileImages/", height_field=None, width_field=None, max_length=None)
#     def __str__(self):
#         return self.UID + " " + self.username


# class Template(models.Model):
#     templateId = models.CharField(max_length=10)
#     templateName = models.CharField(max_length=20)
#     UID = models.ForeignKey(Users, on_delete=models.CASCADE)
#     description = models.TextField()
#     date = models.DateField()
#     templateZip = models.FileField()
#     totaldownloads = models.IntegerField()

#     def __str__(self):
#         return self.templateId + " " + self.templateName + " " + self.UID + " " + self.description + " " + self.date + " " + self.templateZip + " " + self.totaldownloads
    

# class AppLogs(models.Model):
#     transType = {
#         "U": "upload",
#         "D": "download",
#         "del": "delete",
#         "new": "new",
#     }
#     transaction_type = models.CharField(max_length=50,choices=transType)
#     TID = models.ForeignKey(Template, on_delete=models.CASCADE)
#     UID = models.ForeignKey(Users, on_delete=models.CASCADE)
#     def __str__(self):
#         return self.transaction_type + " " + self.UID + " " + self.TID
    