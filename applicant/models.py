from django.db import models
# Create your models here.

class ApplicantCountry(models.Model):
    """Allows the applicant class to link the applicant
    to a country that's in our database"""
    name = models.CharField(max_length=255)


class Applicant(models.Model):
    """This class contains all the variables and methods that a user of type Applicant will need"""
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True) #unique=True?
    aboutMe = models.CharField(max_length=500)
    phone = models.IntegerField(max_length=30, blank=True)
    photo = models.CharField(max_length=100)
    street = models.CharField(max_length=255)
    houseNr = models.CharField(max_length=10)
    city = models.CharField(max_length=30)
    country = models.ForeignKey(ApplicantCountry, on_delete=models.CASCADE) #!Valið með select html úr lista
    postalCode = models.CharField(max_length=255)
    username = models.CharField(max_length=30, unique=True)

class Recommendations(models.Model):
    """A person that can provide recommendations for an Applicant"""
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.IntegerField(max_length=30)
    allowedToContact = models.BooleanField()
    role = models.CharField(max_length=100)
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)

class Experiences(models.Model):
    """A work related experience that belongs to an Applicant"""
    company = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    start = models.DateField()
    end = models.DateField()
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)







