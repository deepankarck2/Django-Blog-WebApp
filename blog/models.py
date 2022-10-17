from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User #to get the users

# Create your models here. Use model ORM to make the sql commands
class Post(models.Model):
    title = models.CharField(max_length = 100) #there will be a title field in out DB, which is a char with max len 100
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE) #user deleted, post delete

    def __str__(self):
        return self.title   #to return str nicely in post sql

