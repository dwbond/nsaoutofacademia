from django.db import models

class Person(models.Model):
    name = models.CharField(max_length = 150)
    titleName = models.CharField(max_length = 150)
    email = models.EmailField()

    class Meta:
        verbose_name_plural = "people"

class University(models.Model):
    universityName = models.CharField(max_length = 150)
    centerName = models.CharField(max_length = 150)
    centerEmail = models.EmailField()
    page = models.URLField()
    designation = models.CharField(max_length = 150)
    isPublic = models.BooleanField()
    people = models.ManyToManyField('Person')

    class Meta:
        verbose_name_plural = "universities"
