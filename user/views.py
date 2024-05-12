from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from applicant.forms.applicantform import ApplicantFormPrimary, ApplicantFormSecondary
from user.forms.signup_form import CustomUserCreationForm
from user.forms.company_signup import CustomUserCreationForm2
from user.models import applicantProfile, companyProfile
from job.models import Job
from applicant.models import Applicant
from company.models import Company

def login(request):
    return render(request, 'user/login.html')


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            applicant = Applicant.objects.create()
            applicantProfile.objects.create(user=user,applicant=applicant)
            return redirect('user-login')
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
    return render(request, 'user/company_signup.html', {
        'form': CustomUserCreationForm2()
    })

@login_required
def profile(request):
    a_user = get_object_or_404(applicantProfile, user=request.user)
    if a_user:
        applicant = a_user.applicant

        if request.method == "POST":
            pass
            return redirect('user-profile')
        form1 = ApplicantFormPrimary()
        form2 = ApplicantFormSecondary()
        return render(request, 'user/applicant_profile.html', {
            "form1": form1, 'form2': form2, "applicant": applicant
        })
    c_user = get_object_or_404(companyProfile, user=request.user)
    if c_user:
        company = c_user.company
        job_list = Job.objects.filter(company_id=company.id)
        if request.method == "POST":
            print(2)
        return render(request, 'user/company_profile.html', {
            "form": "", "company": company, "jobs": job_list
        })
    #return server error, því ef hægt er að búa til notanda sem ekki er tengdur við applicant og company þá er það okkur að kenna
