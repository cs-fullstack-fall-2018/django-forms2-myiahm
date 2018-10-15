from django import forms
from datetime import datetime



class Formmodel(forms.Form):
    name = forms.CharField()
    recipe = forms.CharField()
    timeCook = forms.IntegerField()
