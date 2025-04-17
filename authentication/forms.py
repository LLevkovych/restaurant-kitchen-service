from django.contrib.auth.forms import UserCreationForm
from django import forms

from core.models import Cook


class CookCreationForm(UserCreationForm):
    class Meta:
        model = Cook
        fields = ("username", "first_name", "last_name", "years_of_experience")


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Cook
        fields = ["first_name", "last_name", "years_of_experience"]
