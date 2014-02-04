from django.db import models

class Person(models.Model):
    name = models.CharField(max_length = 150)
    titleName = models.CharField(max_length = 150)
    email = models.EmailField()

class University(models.Model):
    universityName = models.CharField(max_length = 150)
    centerName = models.CharField(max_length = 150)
    centerEmail = models.EmailField()
    page = models.URLField()
    people = models.ManyToManyField('Person')  
