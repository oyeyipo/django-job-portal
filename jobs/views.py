from django.shortcuts import render, get_object_or_404

from .models import Job

# Create your views here.
def home_page(request):

    jobs = Job.objects.all()

    context = {
        "job_items": jobs,
    }
    return render(request, "jobs/home.html", context)


def detail_page(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    context = {"job": job}
    return render(request, "jobs/detail.html", context)
