from django import forms
from lecture.models import College, Department
from .models import Profile

from django.forms import ModelChoiceField

colleges = (
    ('인문대학','인문대학'),
    ('사회과학대학','사회과학대학'),
    ('자연과학대학','자연과학대학'),
    ('경영대학','경영대학'),
    ('공과대학','공과대학'),
    ('전자정보대학','전자정보대학'),
    ('농업생명환경대학','농업생명환경대학'),
    ('사범대학','사범대학'),
    ('생활과학대학','생활과학대학'),
    ('수의과학대학','수의과학대학'),
    ('약학대학','약학대학'),
    ('의과대학','의과대학'),
)

class ProfileForm(forms.Form):
    college = forms.ChoiceField(choices=colleges)
    department = forms.CharField(max_length=30,widget=forms.Select())