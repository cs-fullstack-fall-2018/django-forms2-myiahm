from django import forms
from datetime import datetime
from .models import FormModel



class Form(forms.ModelForm):
    class Meta:
        model = FormModel
        fields = ('name', 'recipe','timeCook')

