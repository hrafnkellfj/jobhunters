from django.shortcuts import render, redirect, get_object_or_404
from applicant.forms.step1_application_form import StepOneCreateForm
from applicant.forms.step2_application_form import StepTwoCreateForm
from applicant.forms.step2_changep_form import StepTwoChangeProfile
from applicant.forms.step3_application_form import StepThreeCreateForm
from applicant.forms.step4_application_form import StepFourCreateForm
from applicant.forms.step5_application_form import StepFiveCreateForm
from applicant.models import Applicant, ApplicantEducation
from job.models import Experience, Recommendation,Application, Job
from applicant.forms.step1_changep_form import StepOneChangeProfile
from applicant.models import ApplicantCountry
from django.utils import timezone
from user.models import applicantProfile
from datetime import date


def index(request):
    all_applicants = {'applicants': Applicant.objects.all().order_by('name')}
    return render(request, 'applicant/index.html', all_applicants)

def application1(request, jobid):
    """ """
    applicant = get_object_or_404(applicantProfile, user=request.user).applicant
    if applicant:
        if request.method == 'POST':
            form = StepOneCreateForm(data=request.POST)
            if form.is_valid():
                applicant.name = form.cleaned_data['name']
                applicant.street = form.cleaned_data['street']
                applicant.houseNr = form.cleaned_data['houseNr']
                applicant.city = form.cleaned_data['city']
                applicant.postalCode = form.cleaned_data['postalCode']
                applicant.country = form.cleaned_data['country']
                applicant.save()
                return redirect("/applicants/applications2/"+str(jobid))
        else:
            form = StepOneCreateForm(instance=applicant)
            return render(request, 'applicant/applyToJob_step1.html', {
                'form': form, 'job_id': jobid
            })
    return redirect('index')


def application2(request, jobid):
    """"""
    applicant = get_object_or_404(applicantProfile, user=request.user).applicant
    job = get_object_or_404(Job, pk=jobid)
    application = Application.objects.filter(applicant=applicant, job=job).first()
    if not application:
        application = Application()
    if request.method == 'POST':
        form = StepTwoCreateForm(data=request.POST)
        if form.is_valid():
            coverLetter = form.cleaned_data["coverLetter"]
            application.applicant = applicant
            application.job = job
            application.coverLetter = coverLetter
            application.applyDate = date.today()
            application.status = "Pending"
            application.save()
            return redirect("/applicants/applications3/"+str(jobid))
    else:
        form = StepTwoCreateForm(instance=application)

    return render(request, 'applicant/applyToJob_step2.html', {
        'form': form, 'jobid':jobid
    })


def application3(request, jobid):
    """"""
    applicant = get_object_or_404(applicantProfile, user=request.user).applicant
    education_list = ApplicantEducation.objects.filter(applicant=applicant)

    if request.method == 'POST':
        form = StepThreeCreateForm(data=request.POST)
        if form.is_valid():
            school = form.cleaned_data["school"]
            degree = form.cleaned_data["degree"]
            fieldofstudy = form.cleaned_data["fieldOfStudy"]
            start = form.cleaned_data["start"]
            end = form.cleaned_data["end"]
            if school and degree and fieldofstudy and start and end:
                new_education = ApplicantEducation()
                new_education.school = school
                new_education.degree = degree
                new_education.fieldOfStudy = fieldofstudy
                new_education.start = start
                new_education.end = end
                new_education.applicant=applicant
                new_education.save()
                return redirect('/applicants/applications3/' + str(jobid))

            else:
                request.method=""
                return render(request, 'applicant/applyToJob_step3.html', {
                    'form': form, 'education_list': education_list, 'jobid': jobid
                })
    else:
        form = StepThreeCreateForm()
    return render(request, 'applicant/applyToJob_step3.html', {
        'form': form, 'education_list':education_list, 'jobid':jobid
    })


def application4(request, jobid):
    applicant = get_object_or_404(applicantProfile, user=request.user).applicant
    job = get_object_or_404(Job, pk=jobid)
    experience_list = Experience.objects.filter(applicant=applicant, job=job)

    if request.method == 'POST':
        form = StepFourCreateForm(data=request.POST)
        if form.is_valid():
            company = form.cleaned_data["company"]
            role = form.cleaned_data["role"]
            start = form.cleaned_data["start"]
            end = form.cleaned_data["end"]
            if company and role and start and end:
               new_experience = Experience()
               new_experience.company = company
               new_experience.role = role
               new_experience.start = start
               new_experience.end = end
               new_experience.job = job
               new_experience.applicant = applicant
               new_experience.save()
               return redirect('/applicants/applications4/' + str(jobid))
            else:
                request.method = ""
                return render(request, 'applicant/applyToJob_step4.html', {
                    'form': form, 'experience_list': experience_list, 'jobid': jobid
                })
    else:
        form = StepFourCreateForm()
    return render(request, 'applicant/applyToJob_step4.html', {
        'form': form, 'experience_list': experience_list, 'jobid': jobid
    })


def application5(request, jobid):
    applicant = get_object_or_404(applicantProfile, user=request.user).applicant
    job = get_object_or_404(Job, pk=jobid)
    recommendation_list = Recommendation.objects.filter(applicant=applicant, job=job)

    if request.method == 'POST':
        form = StepFiveCreateForm(data=request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            phone = form.cleaned_data["phone"]
            role = form.cleaned_data["role"]
            allow_contact = form.cleaned_data["allowedToContact"]
            if name and allow_contact:
                new_recommendation = Recommendation()
                new_recommendation.name = name
                new_recommendation.allowedToContact = allow_contact
                new_recommendation.applicant = applicant
                new_recommendation.job = job
                if email:
                    new_recommendation.email = email
                if phone:
                    new_recommendation.phone = phone
                if role:
                    new_recommendation.role = role
                new_recommendation.save()
                return redirect('/applicants/applications5/' + str(jobid))
            else:
                request.method = ""
                #error = vantar eitthvað
                return render(request, 'applicant/applyToJob_step5.html', {
                    'form': form, 'recommendation_list': recommendation_list, 'jobid': jobid
                })
    else:
        form = StepFiveCreateForm()
    return render(request, 'applicant/applyToJob_step5.html', {
        'form': form, 'recommendation_list': recommendation_list, 'jobid': jobid
    })


def overview(request):
    """"""

    pass


    #return render(request, 'applicant/yfirfara.html', {'data': all_data})




def mottekinUmsokn(request):
    return render(request, 'applicant/mottekinUmsokn.html')


def profile(request):
    return render(request, 'user/applicant_profile.html')


def changeProfiles1(request):
    if request.method == 'POST':
        form = StepOneChangeProfile(data=request.POST)
        if form.is_valid():
            application = form.save()
    else:
        form = StepOneChangeProfile()
    return render(request, 'applicant/changeProfile_step1.html', {
        'form': form
    })


def changeProfiles2(request):
    if request.method == 'POST':
        form = StepTwoChangeProfile(data=request.POST)
        if form.is_valid():
            application = form.save()
    else:
        form = StepTwoChangeProfile()
    return render(request, 'applicant/changeProfile_step2.html', {
        'form': form
    })


def changeProfiles3(request):
    if request.method == 'POST':
        form = StepThreeCreateForm(data=request.POST)
        if form.is_valid():
            application = form.save()
    else:
        form = StepThreeCreateForm()
    return render(request, 'applicant/changeProfile_step3.html', {
        'form': form
    })

# Create your views here.
