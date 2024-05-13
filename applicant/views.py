from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from applicant.forms.applicantform import ApplicantFormPrimary, ApplicantFormAll
from applicant.forms.applicationform import ApplicationForm
from applicant.forms.educationform import EducationForm
from applicant.forms.experienceform import ExperienceForm
from applicant.forms.recommendationform import RecommendationForm
from applicant.models import Applicant, ApplicantEducation
from job.models import Experience, Recommendation,Application, Job
from user.models import applicantProfile
from datetime import date


def index(request):
    all_applicants = {'applicants': Applicant.objects.all().order_by('name')}
    return render(request, 'applicant/index.html', all_applicants)

@login_required
def application1(request, jobid):
    """ """
    applicant = get_object_or_404(applicantProfile, user=request.user).applicant
    if not applicant:
        return redirect('home-index')
    if applicant:
        if request.method == 'POST':
            form = ApplicantFormPrimary(data=request.POST)
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
            form = ApplicantFormPrimary(instance=applicant)
            return render(request, 'applicant/applyToJob_step1.html', {
                'form': form, 'job_id': jobid
            })
    return redirect('index')

@login_required
def application2(request, jobid):
    """"""
    applicant = get_object_or_404(applicantProfile, user=request.user).applicant
    if not applicant:
        return redirect('home-index')
    job = get_object_or_404(Job, pk=jobid)
    application = Application.objects.filter(applicant=applicant, job=job).first()
    if not application:
        application = Application()
    if request.method == 'POST':
        form = ApplicationForm(data=request.POST)
        if form.is_valid():
            coverLetter = form.cleaned_data["coverLetter"]
            application.applicant = applicant
            application.job = job
            application.coverLetter = coverLetter
            application.save()
            return redirect("/applicants/applications3/"+str(jobid))
    else:
        form = ApplicationForm(instance=application)

    return render(request, 'applicant/applyToJob_step2.html', {
        'form': form, 'jobid':jobid
    })

@login_required
def application3(request, jobid):
    """"""
    applicant = get_object_or_404(applicantProfile, user=request.user).applicant
    if not applicant:
        return redirect('home-index')
    education_list = ApplicantEducation.objects.filter(applicant=applicant)

    if request.method == 'POST':
        form = EducationForm(data=request.POST)
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
        form = EducationForm()
    return render(request, 'applicant/applyToJob_step3.html', {
        'form': form, 'education_list':education_list, 'jobid':jobid
    })

@login_required
def application4(request, jobid):
    applicant = get_object_or_404(applicantProfile, user=request.user).applicant
    if not applicant:
        return redirect('home-index')
    job = get_object_or_404(Job, pk=jobid)
    experience_list = Experience.objects.filter(applicant=applicant, job=job)

    if request.method == 'POST':
        form = ExperienceForm(data=request.POST)
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
        form = ExperienceForm()
    return render(request, 'applicant/applyToJob_step4.html', {
        'form': form, 'experience_list': experience_list, 'jobid': jobid
    })

@login_required
def application5(request, jobid):
    applicant = get_object_or_404(applicantProfile, user=request.user).applicant
    if not applicant:
        return redirect('home-index')
    job = get_object_or_404(Job, pk=jobid)
    recommendation_list = Recommendation.objects.filter(applicant=applicant, job=job)

    if request.method == 'POST':
        form = RecommendationForm(data=request.POST)
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
        form = RecommendationForm()
    return render(request, 'applicant/applyToJob_step5.html', {
        'form': form, 'recommendation_list': recommendation_list, 'jobid': jobid
    })

@login_required
def overview(request, jobid):
    """Allows the applicant to go over the application's status and if he's happy he
    can submit the application

    The application is already submitted, instead the isFinished field is set to True
    if applicant cancels, delete all data related to application"""

    applicant = get_object_or_404(applicantProfile, user=request.user).applicant
    if not applicant:
        return redirect('home-index')
    job = get_object_or_404(Job, pk=jobid)
    application = get_object_or_404(Application, job=job, applicant=applicant)
    if request.method == "POST":
        if application:
            application.isFinished = True
            application.applyDate = date.today()
            application.save()
        return redirect("/applicants/applications/success/"+str(jobid))

    education_list = ApplicantEducation.objects.filter(applicant=applicant)
    experience_list = Experience.objects.filter(applicant=applicant, job=job)
    recommendation_list = Recommendation.objects.filter(applicant=applicant, job=job)

    return render(request, 'applicant/overview.html', { 'applicant': applicant,
        'job': job, 'application': application, 'education_list': education_list, 'experience_list': experience_list,
        'recommendation_list': recommendation_list
    })

@login_required
def application_successful(request, jobid):
    """"""
    job_title = get_object_or_404(Job, pk=jobid).title
    return render(request, 'applicant/application_successful.html', {'title': job_title})

@login_required
def application_delete(request, jobid):
    """"""
    applicant = get_object_or_404(applicantProfile, user=request.user).applicant
    if not applicant:
        return redirect('home-index')
    job = get_object_or_404(Job, pk=jobid)
    application = get_object_or_404(Application, job=job, applicant=applicant)
    experience_list = Experience.objects.filter(applicant=applicant, job=job)
    recommendation_list = Recommendation.objects.filter(applicant=applicant, job=job)
    if request.method == "POST":
        application.delete()
        experience_list.delete()
        recommendation_list.delete()
    return redirect("home-index")

def changeProfiles1(request):
    applicant = get_object_or_404(Applicant, id=request.user.id)
    # Initialize the form with the applicant instance directly
    form = ApplicantFormAll(instance=applicant, data=request.POST if request.method == 'POST' else None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('changeProfile2')
    return render(request, 'applicant/changeProfile_step1.html', {
        'form': form
    })


def changeProfiles2(request):
    applicant = get_object_or_404(Applicant, id=request.user.id)
    educationobj = ApplicantEducation.objects.filter(applicant=applicant).first()
    form = EducationForm(instance=educationobj, data=request.POST if request.method == 'POST' else None)
    if request.method == 'POST':
        # Get the Applicant object using the logged-in User's ID
        # Initialize the form with the instance if it exists, whether it's a GET or POST request
        if form.is_valid():
            education = form.save(commit=False)
            education.applicant = applicant  # Set the applicant from the verified Applicant instance
            education.save()
            return redirect('changeProfile3')
    return render(request, 'applicant/changeProfile_step2.html', {
        'form': form
    })


def changeProfiles3(request):
    applicant = get_object_or_404(Applicant, id=request.user.id)
    experienceobject = Experience.objects.filter(applicant=applicant).first()
    form = EducationForm(instance=experienceobject, data=request.POST if request.method == 'POST' else None)
    if request.method == 'POST':
        form = EducationForm(data=request.POST)
        if form.is_valid():
            experience = form.save(commit=False)
            experience.applicant = applicant  # Set the applicant from the verified Applicant instance
            experience.save()
            return redirect('user-profile')
    return render(request, 'applicant/changeProfile_step3.html', {
        'form': form
    })




# Create your views here.
