from django.db import models

# Create your models here.


class Company(models.Model):
    """"This class contains all the variables and methods that a user of type Company will need"""
    title = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    logo = models.CharField(max_length=100, blank=True, null=True, default='image_missing.png')
    coverImage = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=1000)
    companyPage = models.URLField(blank=True, null=True)
    username = models.CharField(unique=True, max_length=100)
    


    def __str__(self):
        """A string representation of a company"""
        return self.title
    def get_all_companies(self):
        """Returns a list of all companies"""

    
