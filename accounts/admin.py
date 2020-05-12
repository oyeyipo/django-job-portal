from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.models import Group

from .models import User


class UserCreationForm(forms.ModelForm):
    """  
    A form for creating new users. Includes all the required
    fields, plus a repeated passwords.
    """

    password1 = forms.CharField(label="Password eg. Ola", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password confirmation", widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ("email",)

    def cleaned_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password2"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """
    A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ("email", "last_name", "first_name")

    def clean_password(self):
        return self.initial["password"]


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    # The form to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    list_display = (
        "email",
        "last_name",
        "first_name",
        "is_admin",
    )
    list_filter = ("is_admin",)
    fieldsets = (
        (None, {"fields": ("email", "password",),}),
        ("Personal info", {"fields": ("last_name", "first_name",),}),
        (
            "Permissions",
            {
                "fields": (
                    ("is_admin", "is_active", "is_superuser"),
                    "groups",
                    "user_permissions",
                    "status",
                ),
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {"classes": ("wide",), "fields": ("email", "password1", "password2",),},
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)
    filter_horizontal = (
        "groups",
        "user_permissions",
    )
