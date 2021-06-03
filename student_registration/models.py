from django.db import models

# Create your models here.

class Faculty(models.Model):
    fname = models.CharField(max_length=50)

class Student(models.Model):
    name = models.CharField(max_length=100)
    std_code = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.IntegerField()
    faculty = models.ForeignKey(Faculty, on_delete = models.CASCADE)