from django.contrib import admin

from .models import Applicant, Education, Experience
# Register your models here.
admin.site.register(Applicant)
admin.site.register(Education)
admin.site.register(Experience)