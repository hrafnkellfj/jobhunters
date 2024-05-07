from django.db import models
from applicant.models import Applicant
from company.models import Company

# Create your models here.
class JobCategory(models.Model):
    """text"""
    name = models.CharField(max_length=255)

class Job(models.Model):
    """Text"""
    postDate = models.DateField()
    dueDate = models.DateField()
    startDate = models.DateField()
    category = models.ForeignKey(JobCategory, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

class Applications(models.Model):
    """Text"""
    coverLetter = models.CharField(max_length=255)
    status = models.CharField(max_length=8) #Pending / Hired / Rejected
    resultDate = models.DateField(blank=True)
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)








