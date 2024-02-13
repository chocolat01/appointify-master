from django.forms import ModelForm
from app.models import Medecin

class MedecinForm(ModelForm):
    
    class Meta:
        model =Medecin
        fields = '__all__'