from django.contrib import admin

from .models import Job, Application, Recommendation

# Register your models here.
admin.site.register(Job)
admin.site.register(Application)
admin.site.register(Recommendation)
