from tkinter import N
from django.db import models

# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length=40,default=None)
    designation = models.CharField(max_length=50,default=None)
    salary = models.IntegerField(default=None)
    photo = models.ImageField(upload_to = "image")
    date = models.DateTimeField(auto_now_add=True)