from django.db import models

# Create your models here.


class Company(models.Model):
    title = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    logo = models.URLField() #??Sjá piazza, fyrsta spurning 06/05
    coverImage = models.URLField() #??Sjá piazza, fyrsta spurning 06/05
    description = models.CharField(max_length=500)
    companyPage = models.URLField()
    username = models.CharField(unique=True) #email sem username?
