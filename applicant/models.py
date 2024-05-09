from django.db import models


class ApplicantCountry(models.Model):
    """Allows the applicant class to link the applicant
    to a country that's in our database"""
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Applicant(models.Model):
    """This class contains all the variables and methods that a user of type Applicant will need"""

    #grunnur
    name = models.CharField(max_length=255)
    photo = models.CharField(max_length=999, blank=True, null=True)
    username = models.CharField(max_length=30, unique=True)

    #auka frá okkur
    email = models.EmailField(max_length=255, unique=True)
    aboutMe = models.CharField(max_length=1000, blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)

    #Autofillast í job application ef þetta er fyllt út
    street = models.CharField(max_length=255, blank=True, null=True)
    houseNr = models.CharField(max_length=10, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    country = models.ForeignKey(ApplicantCountry, blank=True, null=True,on_delete=models.CASCADE)  #!Valið með select html úr lista
    postalCode = models.CharField(max_length=255, blank=True, null=True)

class ApplicantEduction(models.Model):
    """This class holds information about the education of the applicant."""
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    school = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    dateStart = models.DateField()
    dateEnd = models.DateField()