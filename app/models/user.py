from django.db import models
from phone_field import PhoneField
from django.contrib.auth.models import AbstractUser
ROLE = (
        ('administrateur','Administrateur'),
        ('medecin','Médecin'),
        ('receptioniste','Receptioniste'),
        ('aucun','Aucun'),
        
        
)

GENRE = (
    
        ('masculin','Masculin'),
        ('feminin','Féminin')
)

class User(AbstractUser):
    phone = PhoneField("Numéro de Téléphone")
    role = models.CharField("RôLE", max_length=20,choices=ROLE)
    genre = models.CharField("GENRE", max_length=10, choices= GENRE)
    
    def __str__(self) -> str:
        return self.role+" : "+self.first_name+" "+self.last_name