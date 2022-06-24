from django.db import models

# Create your models here.

class Quest(models.Model):
    question = models.CharField(max_length=100)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    
# class Vote(models.Model):
#     likes = models.PositiveIntegerField(default=0)
#     dislikes = models.PositiveIntegerField(default=0)
    
#     def get_total_likes(self):
#         return self.likes.users.count()

#     def get_total_dislikes(self):
#         return self.dislikes.users.count()