from django.db import models

# Create your models here.

class Quest(models.Model):
    question = models.CharField(max_length=100)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    
class Login(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=10)
