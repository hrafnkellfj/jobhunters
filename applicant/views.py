from django.shortcuts import render
from django.http import HttpResponse
from templates.applicant.forms.step1_application_form import StepOneCreateForm
from templates.applicant.forms.step2_application_form import StepTwoCreateForm
from templates.applicant.forms.step2_changep_form import StepTwoChangeProfile
from templates.applicant.forms.step3_application_form import StepThreeCreateForm
from templates.applicant.forms.step4_application_form import StepFourCreateForm
from templates.applicant.forms.step5_application_form import StepFiveCreateForm
from applicant.models import Applicant
from templates.applicant.forms.step1_changep_form import StepOneChangeProfile


def index(request):
    all_applicants = {'applicants': Applicant.objects.all().order_by('name')}
    return render(request, 'applicant/index.html', all_applicants)


def mottekinUmsokn(request):
    return render(request, 'applicant/mottekinUmsokn.html')


def application1(request):
    if request.method == 'POST':
        form = StepOneCreateForm(data=request.POST)
        if form.is_valid():
            application = form.save()
    else:
        form = StepOneCreateForm()
    return render(request, 'applicant/applyToJob_step1.html', {
        'form': form
    })


def application2(request):
    if request.method == 'POST':
        form = StepTwoCreateForm(data=request.POST)
        if form.is_valid():
            application = form.save()
    else:
        form = StepTwoCreateForm()
    return render(request, 'applicant/applyToJob_step2.html', {
        'form': form
    })


def application3(request):
    if request.method == 'POST':
        form = StepThreeCreateForm(data=request.POST)
        if form.is_valid():
            application = form.save()
    else:
        form = StepThreeCreateForm()
    return render(request, 'applicant/applyToJob_step3.html', {
        'form': form
    })


def application4(request):
    if request.method == 'POST':
        form = StepFourCreateForm(data=request.POST)
        if form.is_valid():
            application = form.save()
    else:
        form = StepFourCreateForm()
    return render(request, 'applicant/applyToJob_step4.html', {
        'form': form
    })


def application5(request):
    if request.method == 'POST':
        form = StepFourCreateForm(data=request.POST)
        if form.is_valid():
            application = form.save()
    else:
        form = StepFiveCreateForm()
    return render(request, 'applicant/applyToJob_step5.html', {
        'form': form
    })


def yfirfara(request):
    if request.method == 'POST':
        form = StepFiveCreateForm(data=request.POST)
        if form.is_valid():
            application = form.save()
    else:
        form = StepFiveCreateForm()
    return render(request, 'applicant/yfirfara.html', {
        'form': form
    })


def mottekinUmsokn(request):
    return render(request, 'applicant/mottekinUmsokn.html')


def profile(request):
    return render(request, 'applicant/profile.html')


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
            ... # save the form
    else:
        form = StepTwoChangeProfile()
    return render(request, 'applicant/changeProfile_step2.html', {
        'form': form
    })


def changeProfiles3(request):
    if request.method == 'POST':
        form = StepThreeCreateForm(data=request.POST)
        if form.is_valid():
            ...
    else:
        form = StepThreeCreateForm()
    return render(request, 'applicant/changeProfile_step3.html', {
        'form': form
    })

# Create your views here.
