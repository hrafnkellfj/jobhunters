from django.db import models
from django.contrib.auth.models import User
from applicant.models import Applicant
from company.models import Company

class applicantProfile(models.Model):
    """Extends the user as an applicant"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    applicant = models.OneToOneField(Applicant, on_delete=models.CASCADE)

class companyProfile(models.Model):
    """Extends the user as a company"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.OneToOneField(Company, on_delete=models.CASCADE)
