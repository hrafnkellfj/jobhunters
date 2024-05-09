from django.shortcuts import render, redirect
from django.http import HttpResponse
from templates.applicant.forms.step1_application_form import StepOneCreateForm
from templates.applicant.forms.step2_application_form import StepTwoCreateForm
from templates.applicant.forms.step3_application_form import StepThreeCreateForm
from templates.applicant.forms.step4_application_form import StepFourCreateForm
from templates.applicant.forms.step5_application_form import StepFiveCreateForm
from applicant.models import Applicant, ApplicantEduction,ApplicantCountry
from job.models import Experience, Recommendation
from templates.applicant.forms.step1_changep_form import StepOneChangeProfile
from applicant.models import ApplicantCountry


def index(request):
    all_applicants = {'applicants': Applicant.objects.all().order_by('name')}
    return render(request, 'applicant/index.html', all_applicants)



def application1(request):
    if request.method == 'POST':
        form = StepOneCreateForm(data=request.POST)
        if form.is_valid():
            country = form.cleaned_data['country']
            # Store only the primary key of the country
            request.session['applicant_country_pk'] = country.pk
            # Create a copy of form.cleaned_data without non-serializable objects
            step_one_data = form.cleaned_data.copy()
            step_one_data['country'] = country.pk  # Replace the object with the primary key

            request.session['step_one_data'] = step_one_data
            return redirect('Step2')
    else:
        # When retrieving the initial data, reconstruct foreign keys from primary keys
        initial_data = request.session.get('step_one_data', {})
        # Retrieve the country instance again if its primary key is in the session
        country_pk = request.session.get('applicant_country_pk')
        if country_pk:
            initial_data['country'] = country_pk  # Replace it with the PK to pre-fill the form

        form = StepOneCreateForm(initial=initial_data)
    return render(request, 'applicant/applyToJob_step1.html', {
        'form': form
    })


def application2(request):
    if request.method == 'POST':
        form = StepTwoCreateForm(data=request.POST)
        if form.is_valid():
            request.session['step_two_data'] = form.cleaned_data
            return redirect('Step3')
    else:
        initial_data = request.session.get('step_two_data', {})
        form = StepTwoCreateForm(initial=initial_data)

    return render(request, 'applicant/applyToJob_step2.html', {
        'form': form
    })


def application3(request):
    if request.method == 'POST':
        form = StepThreeCreateForm(data=request.POST)
        if form.is_valid():
            step_three_data = form.cleaned_data.copy()

            # Handle the non-serializable fields (like dates)
            for date_field in ['start', 'end']:  # Replace with your actual date fields
                if date_field in step_three_data and step_three_data[date_field]:
                    step_three_data[date_field] = step_three_data[date_field].strftime('%Y-%m-%d')

            # Save the serializable data to the session
            request.session['step_three_data'] = step_three_data
            return redirect('Step4')
    else:
        initial_data = request.session.get('step_three_data', {})
        form = StepThreeCreateForm(initial=initial_data)
    return render(request, 'applicant/applyToJob_step3.html', {
        'form': form
    })


def application4(request):
    if request.method == 'POST':
        form = StepFourCreateForm(data=request.POST)
        if form.is_valid():
            step_four_data = form.cleaned_data.copy()

            # Handle the non-serializable fields (like dates)
            for date_field in ['start', 'end']:  # Replace with your actual date fields
                if date_field in step_four_data and step_four_data[date_field]:
                    step_four_data[date_field] = step_four_data[date_field].strftime('%Y-%m-%d')

            # Save the serializable data to the session
            request.session['step_three_data'] = step_four_data
            return redirect('Step5')
    else:
        initial_data = request.session.get('step_four_data', {})
        form = StepFourCreateForm(initial=initial_data)
    return render(request, 'applicant/applyToJob_step4.html', {
        'form': form
    })


def application5(request):
    if request.method == 'POST':
        form = StepFiveCreateForm(data=request.POST)
        if form.is_valid():
            request.session['step_five_data'] = form.cleaned_data
            return redirect('yfirfara')
    else:
        initial_data = request.session.get('step_five_data', {})
        form = StepFiveCreateForm(initial=initial_data)
    return render(request, 'applicant/applyToJob_step5.html', {
        'form': form
    })

def yfirfara(request):
    all_data = {**request.session.get('step_one_data', {}),
                **request.session.get('step_two_data', {}),
                **request.session.get('step_three_data', {}),
                **request.session.get('step_four_data', {}),
                **request.session.get('step_five_data', {})}
    step_one_data= {**request.session.get('step_one_data', {})}
    step_two_data = {**request.session.get('step_two_data', {})}
    step_three_data = {**request.session.get('step_three_data', {})}
    step_four_data = {**request.session.get('step_four_data', {})}
    step_five_data = {**request.session.get('step_five_data', {})}
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'submit':
            applicant_data = {
                'name':step_one_data.get('name'),
                'street': step_one_data.get('street'),
                'houseNr': step_one_data.get('houseNr'),
                'city': step_one_data.get('city'),
                'postalCode': step_one_data.get('postalCode'),
                'aboutMe': step_two_data.get('aboutMe')
            }
            # Create the Applicant instance
            applicant = Applicant.objects.create(**applicant_data)
            applicant_country_data = {'country': step_one_data.get('country')}
            applicant_country = ApplicantCountry.objects.create(**applicant_country_data)
            applicant_education_data = {
                'school': step_three_data.get('school'),
                'degree': step_three_data.get('degree'),
                'fieldOfStudy': step_three_data.get('fieldOfStudy'),
                'start': step_three_data.get('start'),
                'end': step_three_data.get('end')
            }
            applicant_education = ApplicantEduction.objects.create(**applicant_education_data)
            experience_data = {
                'company': step_four_data.get('company'),
                'role': step_four_data.get('role'),
                'start': step_four_data.get('start'),
                'end': step_four_data.get('end')
            }
            experience = Experience.objects.create(**experience_data)
            recommendation_data = {
                'name': step_five_data.get('name'),
                'email': step_five_data.get('email'),
                'phone': step_five_data.get('phone'),
                'role': step_five_data.get('role'),
                'allow_contact': step_five_data.get('allow_contact')
            }
            recommendation = Recommendation.objects.create(**recommendation_data)

            request.session.pop('step_one_data', None)
            request.session.pop('step_two_data', None)
            request.session.pop('step_three_data', None)
            request.session.pop('step_four_data', None)
            request.session.pop('step_five_data', None)

            return redirect('mottekid')
        elif action == 'cancel':
            request.session.pop('step_one_data', None)
            request.session.pop('step_two_data', None)
            request.session.pop('step_three_data', None)
            request.session.pop('step_four_data', None)
            request.session.pop('step_five_data', None)
            return redirect('/jobs/')
    return render(request, 'applicant/yfirfara.html', {'data': all_data})



def mottekinUmsokn(request):
    return render(request, 'applicant/mottekinUmsokn.html')


def changeProfiles1(request):
    if request.method == 'POST':
        print(1)
    else:
        form = StepOneChangeProfile()
    return render(request, 'applicant/changeProfile_step1.html', {
        'form': form
    })


def changeProfiles2(request):
    ...


def changeProfiles3(request):
    ...


def changeProfiles4(request):
    ...

# Create your views here.
