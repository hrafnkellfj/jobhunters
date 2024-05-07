from django.db import models

class ApplicantCountry(models.Model):
    """Allows the applicant class to link the applicant
    to a country that's in our database"""
    name = models.CharField(max_length=255)


class Applicant(models.Model):
    """This class contains all the variables and methods that a user of type Applicant will need"""
    #grunnur
    name = models.CharField(max_length=255)
    photo = models.CharField(max_length=100, blank=True)
    username = models.CharField(max_length=30, unique=True)
    #auka frá okkur
    email = models.EmailField(max_length=255, unique=True)
    aboutMe = models.CharField(max_length=500, blank=True)
    phone = models.IntegerField(blank=True)
    #Autofillast í job application ef þetta er fyllt út
    street = models.CharField(max_length=255, blank=True)
    houseNr = models.CharField(max_length=10, blank=True)
    city = models.CharField(max_length=30, blank=True)
    country = models.ForeignKey(ApplicantCountry, blank=True, on_delete=models.CASCADE) #!Valið með select html úr lista
    postalCode = models.CharField(max_length=255, blank=True)







