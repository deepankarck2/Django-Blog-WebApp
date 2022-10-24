from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver #importing who will receive
from .models import Profile

#we will use this so that a new profile is creted for each users

@receiver(post_save, sender=User) #when a user is saved, send signal to the reeiver
def create_profile(sender, instance, created, **kwargs):    #reciver takes signal and creates the row. Instance is the user. 
    if created:
        Profile.objects.create(user=instance) #create is used to create a row in profile table

@receiver(post_save, sender=User) #when a user is saved, send signal to the reeiver
def save_profile(sender, instance, **kwargs):    #reciver takes signal and creates the row. Instance is the user. 
    instance.profile.save() #user.profile.save