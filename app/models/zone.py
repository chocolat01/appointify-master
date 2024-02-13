from django.db import models
from app.models import Commune

class Zone(models.Model):
    commune = models.ForeignKey(Commune, on_delete=models.CASCADE)
    nom = models.CharField("Nom", max_length=20,unique=True)
    
    def __str__(self):
        return self.nom
    