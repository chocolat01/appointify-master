from django.forms import ModelForm
from app.models import Cabinet
from django import forms

class CabinetForm(ModelForm):
    
    class Meta:
        model = Cabinet
        fields = '__all__'
        widgets = {'description' : forms.Textarea(attrs={'rows' : 4, 'columns' : 50})}
        
        
    