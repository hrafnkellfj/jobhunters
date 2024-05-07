from django.db import models

# Create your models here.


class Company(models.Model):
    title = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    logo = models.CharField(max_length=100)
    coverImage = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    companyPage = models.URLField()
    username = models.CharField(unique=True)
