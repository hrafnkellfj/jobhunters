from django.contrib import admin
from .models import applicantProfile
from .models import companyProfile

# Register your models here.
admin.site.register(applicantProfile)
admin.site.register(companyProfile)