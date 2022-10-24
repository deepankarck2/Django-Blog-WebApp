from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django.contrib.auth.models import User #to get the users 

# Create your models here.
class Profile(models.Model):   #1-1 relationship with existing user model 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics') #profile pic path changed in the media

    def __str__(self) -> str:
        return f"{self.user.username} Profile" #pritns current logged in user name
    