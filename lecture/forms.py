from django import forms
from .models import Lecture, LectureComment
from .widgets import starWidget

from django.core.validators import MinValueValidator, MaxValueValidator

class LectureCommentForm(forms.Form):
    star = forms.FloatField(validators=[MinValueValidator(0), MaxValueValidator(5)], widget = starWidget)
    content = forms.CharField(max_length=50)