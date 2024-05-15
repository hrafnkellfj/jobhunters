from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from user.forms.signup_form import CustomUserCreationForm
from user.forms.company_signup import CustomUserCreationForm2
from user.models import applicantProfile, companyProfile
from job.models import Job, Application
from applicant.models import Applicant, Education, Experience
from company.models import Company

def login(request):
    return render(request, 'user/login.html')

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            applicant = Applicant.objects.create(email=user.email)
            applicantProfile.objects.create(user=user, applicant=applicant)
            return redirect('user-login')
        else:
            return render(request, 'user/signup.html', {'form': form})
    return render(request, 'user/signup.html', {
        'form': CustomUserCreationForm()
    })

def company_signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm2(request.POST)
        if form.is_valid():
            user, company = form.save()
            companyProfile.objects.create(user=user, company=company)
            return redirect('user-login')
        else:
            return render(request, 'user/company_signup.html', {'form': form})
    return render(request, 'user/company_signup.html', {
        'form': CustomUserCreationForm2()
    })

@login_required()
def profile(request):
    try:
        a_user = applicantProfile.objects.get(user=request.user)
        applicant = a_user.applicant
        experience_list = Experience.objects.filter(applicant=applicant)
        education_list = Education.objects.filter(applicant=applicant)
        return render(request, 'applicant/applicant_profile.html', {
            "applicant": applicant, 'education_list': education_list, 'experience_list':experience_list
        })
    except applicantProfile.DoesNotExist or TypeError:
        pass  # Ignore and try for company profile

    try:
        c_user = companyProfile.objects.get(user=request.user)
        company = c_user.company
        job_list = Job.objects.filter(company=company)
        job_dict = {job:len((Application.objects.filter(job=job))) for job in job_list }
        if request.method == "POST":
            pass  # your POST handling logic for company
        return render(request, 'company/company_profile.html', {
            "form": "", "company": company, "job_dict": job_dict
        })
    except companyProfile.DoesNotExist or TypeError:
        raise Http404("No profile available")
        #return server error, því ef hægt er að búa til notanda sem ekki er tengdur við applicant og company þá er það okkur að kenna
