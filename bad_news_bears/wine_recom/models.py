from djongo import models

# from djongo.models import forms
# from django.db import models


class Wine(models.Model):
    Country = models.CharField(max_length=20)
    Description = models.TextField()
    Name = models.CharField(max_length=200)
    Category = models.CharField(max_length=200)
    Rating = models.FloatField()
    Variety = models.CharField(max_length=200)
    Alcohol = models.FloatField()




