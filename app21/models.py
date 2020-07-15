from django.db import models

# Create your models here.
class StudentModel(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    contact = models.IntegerField(unique=True)
    email = models.CharField(max_length=30,unique=True)
    uname = models.CharField(max_length=30, primary_key=True, unique=True)
    passwd = models.CharField(max_length=20)

class LoginModel(models.Model):
    uname = models.CharField(max_length=30,unique=True)
    passwd = models.CharField(max_length=20)
    type = models.CharField(max_length=20)