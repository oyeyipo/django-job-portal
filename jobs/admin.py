from django.contrib import admin

from .models import Applicant, Job


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ["title", "job_type"]
    list_filter = ["created_at", "updated_at"]


@admin.register(Applicant)
class Applicant(admin.ModelAdmin):
    pass
