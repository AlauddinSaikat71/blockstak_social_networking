from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Posts(models.Model):
    PostId = models.AutoField(primary_key = True)
    PostContent = models.TextField()

class User(AbstractUser):
    # Add custom fields here, if needed
    # For example:
    # profile_picture = models.ImageField(upload_to='profile_pictures', blank=True)
    # bio = models.TextField(blank=True)

    # Set the email field as the unique identifier
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
