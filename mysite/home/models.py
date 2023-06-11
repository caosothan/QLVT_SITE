from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length = 100)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add = True)




class User_data(models.Model):
    username = models.CharField(max_length = 100)
    password = models.TextField(max_length = 10)
    

