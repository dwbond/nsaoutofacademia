from django.db import models

class Person(models.Model):
    name = models.CharField(max_length = 150)
    title = models.CharField(max_length = 150)
    email = models.EmailField()

class University(models.Model):
    universityName = models.CharField(max_length = 150)
    centerName = models.CharField(max_length = 150)
    page = models.URLField()
    people = models.ManyToManyField('Person')  
