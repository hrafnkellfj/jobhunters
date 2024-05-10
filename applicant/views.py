from django.shortcuts import render, redirect
from applicant.forms.application_step1_form import StepOneCreateForm
from applicant.forms.application_step2_form import StepTwoCreateForm
from applicant.forms.application_step3_form import StepThreeCreateForm
from applicant.forms.application_step4_form import StepFourCreateForm
from applicant.forms.application_step5_form import StepFiveCreateForm
from applicant.models import Applicant, ApplicantEduction
from job.models import Experience, Recommendation, Application
from applicant.forms.changeprofile_step1_form import StepOneChangeProfile
from applicant.forms.changeprofile_step2_form import StepTwoChangeProfile
from applicant.forms.changeprofile_step3_form import StepThreeChangeProfile
from applicant.models import ApplicantCountry


def index(request):
    all_applicants = {'applicants': Applicant.objects.all().order_by('name')}
    return render(request, 'applicant/index.html', all_applicants)


def application1(request):
    job_id = request.GET.get('job_id')

    if job_id:
        request.session['current_job_id'] = job_id  # Store job ID in the session
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
            request.session['step_four_data'] = step_four_data
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
    step_one_data = {**request.session.get('step_one_data', {})}
    step_two_data = {**request.session.get('step_two_data', {})}
    step_three_data = {**request.session.get('step_three_data', {})}
    step_four_data = {**request.session.get('step_four_data', {})}
    step_five_data = {**request.session.get('step_five_data', {})}
    country_pk = step_one_data.get('country')
    country_obj = ApplicantCountry.objects.filter(pk=country_pk).first()
    step_one_data['country'] = country_obj.name

    all_data = {**step_one_data,
                **request.session.get('step_two_data', {}),
                **request.session.get('step_three_data', {}),
                **request.session.get('step_four_data', {}),
                **request.session.get('step_five_data', {})}
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'submit':
            # Retrieve the applicant using the update_or_create method or other logic
            user_email = request.user.email

            # Find the existing applicant or create a new one
            applicant, created = Applicant.objects.update_or_create(
                email=user_email,
                defaults={
                    'name': step_one_data.get('name'),
                    'street': step_one_data.get('street'),
                    'houseNr': step_one_data.get('houseNr'),
                    'city': step_one_data.get('city'),
                    'postalCode': step_one_data.get('postalCode'),
                    'aboutMe': step_two_data.get('aboutMe')
                }
            )

            # Now, create or update ApplicantEduction and pass the applicant instance
            applicant_education_data = {
                'applicant': applicant,  # Pass the applicant instance to the foreign key field
                'school': step_three_data.get('school'),
                'degree': step_three_data.get('degree'),
                'fieldOfStudy': step_three_data.get('fieldOfStudy'),
                'start': step_three_data.get('start'),
                'end': step_three_data.get('end')
            }
            job_id = request.session.get('current_job_id')
            applied_job = Application.objects.filter(pk=job_id).first()
            # Use create or update_or_create to save the education record
            applicant_education = ApplicantEduction.objects.update_or_create(**applicant_education_data)
            experience_data = {
                'applicant': applicant,
                'company': step_four_data.get('company'),
                'role': step_four_data.get('role'),
                'start': step_four_data.get('start'),
                'end': step_four_data.get('end'),
                'applied_job_id': job_id
            }
            experience = Experience.objects.update(**experience_data)
            recommendation_data = {
                'applicant': applicant,
                'name': step_five_data.get('name'),
                'email': step_five_data.get('email'),
                'phone': step_five_data.get('phone'),
                'role': step_five_data.get('role'),
                'allowedToContact': step_five_data.get('allow_contact')
            }
            recommendation = Recommendation.objects.update(**recommendation_data)

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
        form = StepOneChangeProfile(data=request.POST)
        if form.is_valid():
            application = form.save()
            return redirect('changeProfile2')
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
            return redirect('changeProfile3')
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
            return redirect('user-profile')
    else:
        form = StepThreeCreateForm()
    return render(request, 'applicant/changeProfile_step3.html', {
        'form': form
    })

# Create your views here.
