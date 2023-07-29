from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.TextField(max_length=30,help_text='Please Inter Name student ')
    age =models.IntegerField()
    img= models.ImageField(upload_to="ipone-%y/%m/%d")
    
class Stud(models.Model):
    name = models.TextField(max_length=30,help_text='Please Inter Name student ')
    age =models.IntegerField()
    img= models.ImageField(upload_to="ipone-%y/%m/%d")
    