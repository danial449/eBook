from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
   name = models.CharField(max_length = 30 , null=True , blank=True)
   email = models.EmailField(null=True , unique=True)
   is_email_verified = models.BooleanField(default=False)
   email_verification_token = models.CharField(max_length=200 ,blank=True, null=True)

   def __str__(self):
        return self.username

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE , blank=True, null=True)
    name = models.CharField(max_length = 30 , null=True , blank=True)
    username = models.CharField(max_length = 30)
    email = models.EmailField(null=True , unique=True)

    def __str__(self):
        return self.username

class ContactUs(models.Model):
    name = models.CharField(max_length = 20)
    subject = models.CharField(max_length = 20)
    email = models.EmailField(null=False , unique=False)
    message = models.TextField(max_length = 500)

    def __str__(self):
        return self.message