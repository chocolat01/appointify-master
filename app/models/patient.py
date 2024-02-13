from django.db import models
from app.models import Zone
from phone_field import PhoneField


GENRE = (
    
        ('masculin','Masculin'),
        ('feminin','Féminin')
)

class Patient (models.Model):
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE)
    nom = models.CharField("Nom",max_length=20)
    prenom = models.CharField("Prénom",max_length=20)
    genre = models.CharField("GENRE", max_length=10, choices= GENRE)
    telephone = PhoneField("Téléphone du Patient", blank =True)
    email = models.EmailField("Email", max_length=20)
    
    
    def __str__(self) ->str:
        return self.nom+" "+self.prenom
    
    
    class Meta :
        constraints = [
            models.UniqueConstraint(
                fields=['nom','prenom','telephone'],
                name = 'unique_patient'
            )
        ]