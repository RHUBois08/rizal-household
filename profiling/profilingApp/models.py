from django.db import models

# Create your models here.
class Person(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    middlename = models.CharField(max_length=50)
    suffix = models.CharField(max_length=50)
    email = models.EmailField()
    dob = models.DateField()