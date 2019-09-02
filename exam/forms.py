from django import forms

from .models import *

class ExamForm(forms.ModelForm):
    class Meta:
        model=ExamModel
        fields=("name","sorting",'question',"score",)
        
class ScoreForm(forms.ModelForm):
    class Meta:
        model=ScoreModel
        fields=("answer",)
        
class CheckForm(forms.Form):
    score=forms.FloatField()