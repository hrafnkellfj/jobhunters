from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from applicant.forms.applicantform import ApplicantFormPrimary, ApplicantFormAll
from applicant.forms.applicationform import ApplicationForm
from applicant.forms.educationform import EducationForm
from applicant.forms.experienceform import ExperienceForm
from applicant.forms.recommendationform import RecommendationForm
from applicant.models import Education, Experience
from job.models import Recommendation, Application, Job
from user.models import applicantProfile
from datetime import date


def index(request):
    """The index class for applicants, used as a redirect for the user-profile"""
    return redirect('user-profile')


@login_required
def applications(request):
    """Shows a list of all applications belonging to a logged-in user"""
    if hasattr(request.user, 'applicantprofile'):
        application_list = Application.objects.filter(applicant=request.user.applicantprofile.applicant)
        return render(request, 'applicant/applicant_applications.html', {'application_list': application_list})

    if hasattr(request.user, 'companyprofile'):
        company = request.user.companyprofile.company
        job_list = Job.objects.filter(company=company)
        job_dict = {job: len((Application.objects.filter(job=job))) for job in job_list}
        return render(request,'company/job_applications_company.html',{'job_dict': job_dict})
    return redirect('home-index')

@login_required
def application1(request, jobid):
    """The first step in the create application process: Contact information"""
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
    """The second step in the application process: Writing the cover letter"""
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
    """The third step in the application process: Applicant education history"""
    applicant = get_object_or_404(applicantProfile, user=request.user).applicant
    if not applicant:
        return redirect('home-index')
    education_list = Education.objects.filter(applicant=applicant)

    if request.method == 'POST':
        form = EducationForm(data=request.POST)
        if form.is_valid():
            school = form.cleaned_data["school"]
            degree = form.cleaned_data["degree"]
            fieldofstudy = form.cleaned_data["fieldOfStudy"]
            start = form.cleaned_data["start"]
            end = form.cleaned_data["end"]
            if school and degree and fieldofstudy and start and end:
                new_education = Education()
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
    """The fourth step in the application process: Applicant job experiences"""
    applicant = get_object_or_404(applicantProfile, user=request.user).applicant
    if not applicant:
        return redirect('home-index')
    experience_list = Experience.objects.filter(applicant=applicant)

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
    """The fifth step in the application process: Applicant recommendations"""
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
            if name:
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

    form = RecommendationForm()
    return render(request, 'applicant/applyToJob_step5.html', {
        'form': form, 'recommendation_list': recommendation_list, 'jobid': jobid
    })

@login_required
def overview(request, jobid):
    """The final step in the application process. Allows the applicant to go over the application's status and if he's
     happy he can submit the application, if not he can delete the application and all objects related  to it.

    The application is already submitted, instead the isFinished field is set to True
    if applicant cancels, delete all data related to application"""
    applicant = get_object_or_404(applicantProfile, user=request.user).applicant
    if not applicant:
        return redirect('home-index')
    job = get_object_or_404(Job, pk=jobid)
    application = get_object_or_404(Application, job=job, applicant=applicant)
    education_list = Education.objects.filter(applicant=applicant)
    experience_list = Experience.objects.filter(applicant=applicant)
    recommendation_list = Recommendation.objects.filter(applicant=applicant, job=job)
    if request.method == "POST":
        if "accept" in request.POST:
            if application:
                application.isFinished = True
                application.applyDate = date.today()
                application.save()
            return redirect("/applicants/applications/success/"+str(jobid))
        if "delete" in request.POST:
            application.delete()
            recommendation_list.delete()
            return redirect("/jobs")
        if "back" in request.POST:
            return redirect('/applicants/applications5/' + str(jobid))
        if "application_del" in request.POST:
            application.delete()
            recommendation_list.delete()
            return redirect("/applicants/applications")


    return render(request, 'applicant/overview.html', { 'applicant': applicant,
        'job': job, 'application': application, 'education_list': education_list, 'experience_list': experience_list,
        'recommendation_list': recommendation_list
    })

@login_required
def application_successful(request, jobid):
    """A success screen if a job application is successful"""
    job_title = get_object_or_404(Job, pk=jobid).title
    return render(request, 'applicant/application_successful.html', {'title': job_title})

@login_required
def application_delete(request, jobid):
    """This view deletes the application and all related objects

    Put in its own view so we can call it from other places than just the overview"""
    applicant = get_object_or_404(applicantProfile, user=request.user).applicant
    if not applicant:
        return redirect('home-index')
    job = get_object_or_404(Job, pk=jobid)
    application = get_object_or_404(Application, job=job, applicant=applicant)
    recommendation_list = Recommendation.objects.filter(applicant=applicant, job=job)
    if request.method == "POST":
        application.delete()
        recommendation_list.delete()
    return redirect("home-index")

@login_required
def changeProfiles1(request):
    """The first step in changing an applicant profile: Contact information"""
    applicant = get_object_or_404(applicantProfile, user=request.user).applicant
    # Initialize the form with the applicant instance directly
    form = ApplicantFormAll(instance=applicant, data=request.POST if request.method == 'POST' else None)
    if request.method == 'POST':
        if 'submit' in request.POST:
            if form.is_valid():
                form.save()
                return redirect('changeProfile2')
        if 'continue' in request.POST:
            return redirect('changeProfile2')
        if 'back' in request.POST:
            return redirect('user-profile')
    return render(request, 'applicant/changeProfile_step1.html', {
        'form': form
    })

@login_required
def changeProfiles2(request):
    """The second step in changing an applicant profile: Education"""
    applicant = get_object_or_404(applicantProfile, user=request.user).applicant
    if request.method == 'POST':
        if 'submit' in request.POST:
            form = EducationForm(data=request.POST)
            if form.is_valid():
                education = form.save(commit=False)
                education.applicant = applicant  # Set the applicant from the verified Applicant instance
                education.save()
                return redirect('changeProfile2')
        if 'continue' in request.POST:
            return redirect('changeProfile3')
        if 'back' in request.POST:
            return redirect('changeProfile1')
    form = EducationForm()
    return render(request, 'applicant/changeProfile_step2.html', {
        'form': form
    })

@login_required
def changeProfiles3(request):
    """The third and final step in changing an applicant profile: Experiences"""
    applicant = get_object_or_404(applicantProfile, user=request.user).applicant
    if request.method == 'POST':
        if 'submit' in request.POST:
            form = ExperienceForm(data=request.POST)
            if form.is_valid():
                experience = form.save(commit=False)
                experience.applicant = applicant  # Set the applicant from the verified Applicant instance
                experience.save()
                return redirect('changeProfile3')
        if 'continue' in request.POST:
            return redirect('user-profile')
        if 'back' in request.POST:
            return redirect('changeProfile2')
    form = ExperienceForm()
    return render(request, 'applicant/changeProfile_step3.html', {
        'form': form
    })




# Create your views here.
