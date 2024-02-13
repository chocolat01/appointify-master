from django.db import models
from app.models import Patient,Zone,creneau_journalier

GENRE = (
    
        ('masculin','Masculin'),
        ('feminin','Féminin')
)

class Rendez_Vous(models.Model):
    # from app.models import CreneauJournalier
    creneauJournalier = models.ForeignKey(creneau_journalier.CreneauJournalier,null=True,blank=True, on_delete=models.CASCADE)
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE)
    nom = models.CharField(max_length=20)
    prenom = models.CharField(max_length=20)
    genre = models.CharField(max_length=10,null=True,blank=True ,choices= GENRE)
    telephone = models.CharField( blank =True, max_length=20)
    email = models.EmailField(null=True,blank=True, max_length=20)
    motif = models.CharField( max_length=200)   
    