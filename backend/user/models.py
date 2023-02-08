from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

# Create your models here.

class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    nickname = models.TextField(max_length=255)
    name = models.TextField(max_length=255)
    profile_image_name = models.CharField(max_length=100, default="default")



class ProfileImage(models.Model) :
    profile_image_name = models.CharField(max_length=100, default="default")
    image = models.BinaryField()
    email = models.EmailField(unique=True)