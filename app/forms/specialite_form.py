from django.forms import ModelForm
from app.models import Specialite

class   SpecialiteForm(ModelForm):
    
    class Meta:
        model = Specialite
        fields = '__all__'