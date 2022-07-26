from django.contrib import admin

from employers.models import EmployerProfile,Jobs

# Register your models here.
admin.site.register(EmployerProfile)
admin.site.register(Jobs)
