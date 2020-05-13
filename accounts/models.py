from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone

from django.contrib.auth.base_user import AbstractBaseUser

from core.models import TimestampedModel

from .manager import UserManager


class User(AbstractBaseUser, PermissionsMixin, TimestampedModel):
    """ # TODO: docs """

    # username = models.CharField(db_index=True, max_length=255, unique=True)
    APPLICANT = 1
    TEST_CANDIDATE = 2
    SUCCESSFULL_CANDIDATE = 3
    EMPLOYEE = 4

    STATUS_CHOICES = (
        (APPLICANT, "applicant"),
        (TEST_CANDIDATE, "test candidate"),
        (SUCCESSFULL_CANDIDATE, "successful candidate"),
        (EMPLOYEE, "employee"),
    )

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(db_index=True, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    level = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, default=APPLICANT)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        """
        Returns a string representation of this `User`.

        This string is used when a `User` is printed in the console.
        """
        return self.email

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """
        This method is required by Django for things like handling emails.
        Typically, this would be the user's first name. Since we do not store
        the user's real name, we return their username instead.
        """
        return self.first_name

    @property
    def is_staff(self):
        "Is the user member of staff?"
        return self.is_admin

    def email_user(self, subject, message, from_email=None, **kwargs):
        """ Sends an email to this User. """
        send_mail(subject, message, from_email, [self.email], **kwargs)
