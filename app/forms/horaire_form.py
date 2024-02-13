from django import forms
from django.forms import ModelForm
from app.models import Horaire
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget

class CustomDateInput(forms.DateInput):
    input_type = 'text'
    format = '%d/%m/%Y'

class CustomTimeInput(forms.TimeInput):
    input_type = 'text'
    format = '%H:%M'
    
class HoraireForm(ModelForm):
    
    class Meta:
        model = Horaire
        fields = ['cabinet', 'date', 'heure_debut', 'heure_fin']
        widgets = {
        'date': CustomDateInput(format='%d/%m/%Y', attrs={'placeholder': 'jj/mm/aaaa'}),
        'heure_debut': CustomTimeInput(format='%H:%M', attrs={'placeholder': 'hh:mm'}),
        'heure_fin': CustomTimeInput(format='%H:%M', attrs={'placeholder': 'hh:mm'}),
    }
