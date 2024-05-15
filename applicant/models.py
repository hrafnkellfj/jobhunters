from django.db import models


class ApplicantCountry(models.Model):
    """Allows the applicant class to link the applicant
    to a country that's in our database"""
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Applicant(models.Model):
    """This class contains all the variables and methods that a user of type Applicant will need"""
    #Autofillast í job application ef þetta er fyllt út
    name = models.CharField(max_length=255)
    street = models.CharField(max_length=255, blank=False, null=True)
    houseNr = models.CharField(max_length=10, blank=False, null=True)
    city = models.CharField(max_length=30, blank=False, null=True)
    country = models.ForeignKey(ApplicantCountry, blank=False, null=True, on_delete=models.CASCADE)
    postalCode = models.CharField(max_length=255, blank=False, null=True)
    email = models.EmailField(max_length=255, unique=True)

    # auka frá okkur + email fyrir ofan
    aboutMe = models.CharField(max_length=500, blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    photo = models.CharField(max_length=999, blank=True, null=True,
                             default='https://cdn-icons-png.freepik.com/256/12259/12259373.png?ga=GA1.1.1834476485.1715253075&semt=ais_hybrid')


class Education(models.Model):
    """This class holds information about the education of the applicant."""
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    school = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    fieldOfStudy = models.CharField(max_length=255)
    start = models.DateField()
    end = models.DateField()

class Experience(models.Model):
    """A work related experience that belongs to an Applicant"""
    company = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    start = models.DateField()
    end = models.DateField(blank=True, null=True)
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
