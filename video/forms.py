from django import forms

from .models import *

class VideoForm(forms.ModelForm):
    class Meta:
        model=VideoModel
        fields=("sorting","name","description","source",)
        
