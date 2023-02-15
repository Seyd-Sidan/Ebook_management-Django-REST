from unittest.util import _MAX_LENGTH
from django.db import models


# Create your models here.

my_choices = [
     ('Fantasy','Fantasy'),
     ('Literary','Literary'),
     ('Mystery','Mystery'),
     ('Non_Fiction','Non-Fiction'),
     ('Science_Fiction','Science-Fiction'),
     ('Thriller','Thriller'),
    ]

class ebook(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100,choices=my_choices)
    review = models.IntegerField()
    favourite = models.BooleanField()
    
    
# class Users(models.Model):
#     user_id = models.IntegerField()
#     username = models.CharField(max_length=100)
#     password = models.CharField(max_length=100)
    