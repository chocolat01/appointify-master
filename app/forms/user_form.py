from django.contrib.auth.forms import UserCreationForm
from app.models import User

class UserForm(UserCreationForm):
    
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
    