from django import forms
from django.forms import ModelForm
from app.models import creneau_journalier
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget

class CustomDateInput(forms.DateInput):
    input_type = 'text'
    format = '%d/%m/%Y'

class CustomTimeInput(forms.TimeInput):
    input_type = 'text'
    format = '%H:%M'
    
class CreneauJournalierForm(ModelForm):
    
    class Meta:
        model = creneau_journalier.CreneauJournalier
        fields = ['horaire', 'debut', 'fin', 'pris']
        widgets = {
            'debut': CustomTimeInput(attrs={'placeholder': 'hh:mm'}),
            'fin': CustomTimeInput(attrs={'placeholder': 'hh:mm'}),
        }