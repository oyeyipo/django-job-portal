from django.shortcuts import render

from .models import Job

# Create your views here.
def home_page(request):

    jobs = Job.objects.all()

    context = {
        "job_items": jobs,
    }
    return render(request, "jobs/home.html", context)
