from django.db import models

# Create your models here.
# This file contains the database models for the application. which consists of the following models:

class Major(models.Model):
    name = models.CharField(max_length=255, unique=True)
    cost = models.IntegerField(default=0)

    def __str__(self):
        return self.name
# Major table which contains the name of the major and the cost of the major

class University(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)
    website = models.URLField()
    majors = models.ManyToManyField(Major)
    extraCost = models.IntegerField(default=0)

# University table which contains the name of the university, the country of the university, the website of the university, the majors offered by the university and the extra cost of the university
    def __str__(self):
        return self.name
