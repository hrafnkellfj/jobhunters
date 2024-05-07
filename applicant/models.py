from django.db import models
# Create your models here.

class ApplicantCountry(models.Model):
    """Allows the applicant class to link the applicant
    to a country that's in our database"""
    name = models.CharField(max_length=255)

class Applicant(models.Model):
    """This class contains all the variable that an instance of
    an applicant will need"""
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255) #unique=True?
    aboutMe = models.CharField(max_length=500)
    phone = models.IntegerField(max_length=30, blank=True)
    photo = models.CharField(max_length=100)
    street = models.CharField(max_length=255)
    houseNr = models.CharField(max_length=10)
    city = models.CharField(max_length=30)
    country = models.ForeignKey(ApplicantCountry, on_delete=models.CASCADE) #!Valið með select html úr lista
    postalCode = models.CharField(max_length=255)
    #username = models.CharField(max_length=30) eða gera unique=True á emails?







