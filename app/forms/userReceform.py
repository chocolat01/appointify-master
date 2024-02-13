from django import forms
from django.contrib.auth.forms import UserCreationForm
from app.models import User

class ReceptionistSignUpForm(UserCreationForm):
    role = forms.ChoiceField(choices=[('receptioniste', 'Receptioniste')])

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'username',
            'phone',
            'password1',
            'password2',
            'role',
            'genre',
        ]