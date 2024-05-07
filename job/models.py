from django.db import models
from applicant.models import Applicant
from company.models import Company

# Create your models here.
class JobCategory(models.Model):
    """Contains job categories"""
    type = models.CharField(max_length=255)

class Job(models.Model):
    """The Job class contains all the variables that are needed to display a Job correctly.
    Jobs are made by Company users and can be applied to by Applicant users"""
    title = models.CharField(max_length=255)
    jobPercentage = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    postDate = models.DateField()
    dueDate = models.DateField()
    startDate = models.DateField()
    category = models.ForeignKey(JobCategory, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

class Applications(models.Model):
    """This class links an Applicant to a Job when the Applicant has applied for that Job.
    The class contains variables of interest to both applicant and company users."""
    coverLetter = models.CharField(max_length=255)
    status = models.CharField(max_length=8) #Pending / Hired / Rejected
    resultDate = models.DateField(blank=True) #Dagsetning þegar status verður eitthvað annað en pending
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)








