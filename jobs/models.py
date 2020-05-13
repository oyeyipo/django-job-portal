from django.db import models

from core.models import TimestampedModel

from django.conf import settings

User = settings.AUTH_USER_MODEL


class Job(TimestampedModel):

    FULL = 1
    PART = 2
    INTERN = 3

    JOB_TYPE = (
        (FULL, "Full time"),
        (PART, "Part time"),
        (INTERN, "Internship"),
    )

    FRONTEND = 1
    UXUI = 2
    BACKEND = 3
    FULLSTACK = 4
    DEVOPS = 5

    CATIGORY = (
        (FRONTEND, "Frontend"),
        (UXUI, "UX/UI design"),
        (BACKEND, "Backend"),
        (FULLSTACK, "FullStack"),
        (DEVOPS, "Devops"),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    description = models.TextField()
    location = models.CharField(max_length=150)
    job_type = models.PositiveSmallIntegerField(choices=JOB_TYPE, default=INTERN)
    category = models.PositiveSmallIntegerField(choices=CATIGORY, default=FULLSTACK)

    def __str__(self):
        return self.title


class Applicant(TimestampedModel):
    user = models.OneToOneField(
        User,
        primary_key=True,
        on_delete=models.CASCADE,
        related_name="applicant_profile",
    )
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="applicants")

    def __str__(self):
        return self.user.get_full_name()
