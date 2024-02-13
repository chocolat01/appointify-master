from django.forms import ModelForm
from app.models import Receptioniste

class ReceptionisteForm(ModelForm):
    
    class Meta:
        model = Receptioniste
        fields = '__all__'
        
        
    