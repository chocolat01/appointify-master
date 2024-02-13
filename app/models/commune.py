from django.db import models
from app.models import Province

class Commune(models.Model):
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    nom = models.CharField("Nom" , max_length=20, unique=True)
    
    def __str__(self) -> str:
        return self.nom
    