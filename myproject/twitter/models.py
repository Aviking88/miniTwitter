from django.db import models

# Create your models here.

class userData(models.Model):
    userName = models.CharField(max_length=100)
    dob = models.CharField(max_length=10)
    email = models.CharField(primary_key=True,max_length=30)
    password= models.CharField(max_length=100)

class tweetData(models.Model):
    msgID=   models.AutoField(primary_key=True)
    userName = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    tweettime =models.DateTimeField(auto_now_add = True)
    message = models.CharField(max_length=141)
