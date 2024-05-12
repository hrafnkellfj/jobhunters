from django.db import models
from django.shortcuts import get_object_or_404
from applicant.models import Applicant, ApplicantCountry
from company.models import Company
from datetime import date

# Create your models here.
class JobCategory(models.Model):
    """Contains job categories"""
    type = models.CharField(max_length=255)

class Job(models.Model):
    """The Job class contains all the variables that are needed to display a Job correctly.
    Jobs are made by Company users and can be applied to by Applicant users"""
    title = models.CharField(max_length=255)
    jobPercentage = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    location = models.CharField(max_length=255)
    postDate = models.DateField()
    dueDate = models.DateField()
    startDate = models.DateField()
    jobImage = models.CharField(max_length=999, blank=True,default='https://img.freepik.com/premium-vector/default-image-icon-vector-missing-picture-page-website-design-mobile-app-no-photo-available_87543-11093.jpg?w=360')
    category = models.ForeignKey(JobCategory, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def apply_filters(query_dict, job_list):
        """Gets a list of jobs and applies filters and search term to it."""
        company = None
        if query_dict["title"]:
            job_list = job_list.filter(title__icontains=query_dict["title"])
        if query_dict["orderby"]:
            job_list = job_list.order_by(query_dict["orderby"])
        if query_dict["category"]:
            job_list = job_list.filter(category=query_dict["category"])
        if query_dict["company"]:
            company = get_object_or_404(Company, title__icontains=query_dict["company"])
        if company:
            job_list = job_list.filter(company_id=company.id)
        return job_list

class Application(models.Model):
    """This class links an Applicant to a Job when the Applicant has applied for that Job.
    The class contains variables of interest to both applicant and company users."""
    #frá notanda handvirkt
    coverLetter = models.CharField(max_length=500)
    #frá notanda autofill eða handvirkt
    """street = models.CharField(max_length=255)
    houseNr = models.CharField(max_length=10)
    city = models.CharField(max_length=30)
    country = models.ForeignKey(ApplicantCountry, on_delete=models.CASCADE)  # !Valið með select html úr lista
    postalCode = models.CharField(max_length=255)"""
    #Umsóknar meðhöndlun
    status = models.CharField(max_length=8, default="Pending") #Pending / Hired / Rejected
    applyDate = models.DateField()
    resultDate = models.DateField(blank=True, null=True) #Dagsetning þegar status verður eitthvað annað en pending
    isFinished = models.BooleanField(default=False)  #umsækjandi hefur yfirfarið og staðfest umsókn
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)

#Recommendations og Experiences eru undir job en ekki applicant
#því annars varð circular import þegar foreignkey var sett á þau fyrir Applications
class Recommendation(models.Model):
    """A person that can provide recommendations for an Applicant"""
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    allowedToContact = models.BooleanField( )
    role = models.CharField(max_length=100)
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)

class Experience(models.Model):
    """A work related experience that belongs to an Applicant"""
    company = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    start = models.DateField()
    end = models.DateField(blank=True, null=True)
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)





