from distutils.command.upload import upload
from email.policy import default
from turtle import width
from django.db import models
from django.contrib.auth.models import User #to get the users 
from PIL import Image

# Create your models here.
class Profile(models.Model):   #1-1 relationship with existing user model  ORM
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='guest-user.jpg', upload_to='profile_pics') #profile pic path changed in the media
    
    def __str__(self) -> str:
        return f"{self.user.username} Profile" #pritns current logged in user name
    
    # to resize image
    def save(self): #gets run after our model is saved. Overrriding it
        super().save() #grab the image and resize it
        
        img = Image.open(self.image.path) 
        if (img.height > 300 or img.width > 300):
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)