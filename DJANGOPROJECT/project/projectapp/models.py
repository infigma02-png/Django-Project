from django.db import models

# Create your models here.
class Users(models.Model):
  Firstname=models.CharField(max_length=50)
  Lastname=models.CharField(max_length=50)
  Email=models.CharField(max_length=50)
  Subject=models.CharField(max_length=50)
  Message=models.TextField(max_length=500)