from django.db import models

# Create your models here.


class Major(models.Model):
    name = models.CharField(max_length=255, unique=True)
    cost = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class University(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)
    website = models.URLField()
    majors = models.ManyToManyField(Major)
    extraCost = models.IntegerField(default=0)

    def __str__(self):
        return self.name
