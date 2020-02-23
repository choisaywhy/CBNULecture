from django import forms
from lecture.models import College, Department
from .models import Profile

from django.forms import ModelChoiceField


class ProfileForm(forms.Form):
    college = forms.ModelChoiceField(queryset = College.objects.all())
    department = forms.CharField(max_length=30,widget=forms.Select())