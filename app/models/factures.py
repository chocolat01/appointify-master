from django.db import models
from app.models import Rendez_Vous


class Facture (models.Model):
    rendez_vous = models.ForeignKey(Rendez_Vous, on_delete=models.CASCADE)
    montant = models.PositiveIntegerField("Montant")
    date_paiement = models.DateField("Date",max_length=20)
    
    def __str__(self) ->str:
        return self.montant+" : "+self.date_paiement
    