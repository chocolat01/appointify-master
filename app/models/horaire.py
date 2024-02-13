from django.db import models
from app.models import Cabinet

class Horaire (models.Model):
    cabinet= models.ForeignKey(Cabinet, on_delete=models.CASCADE)
    date = models.DateField("Date",max_length=30)
    heure_debut = models.TimeField("Heure_Début",max_length=20)
    heure_fin = models.TimeField("Heure_Fin",max_length=20)            
    
    
    def __str__(self) ->str:
        return str(self.date) +" : "+str(self.heure_debut)+" "+str(self.heure_fin)

    def save(self, *args, **kwargs):
        # On appelle la méthode save du modèle parent
        super().save(*args, **kwargs)
        # On importe la fonction créer_créneaux_journaliers uniquement lorsque l'on en a besoin
        from app.views import créer_créneaux_journaliers
        # On appelle la fonction créer_créneaux_journaliers avec l'objet Horaire
        créer_créneaux_journaliers(self)
