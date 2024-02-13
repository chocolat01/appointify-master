from django.db import models
from app.models import Zone,Medecin

class Cabinet(models.Model):
    medecin = models.ForeignKey(Medecin, on_delete=models.CASCADE)
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE)
    adresse_complete =models.CharField("Adrèsse Complète", max_length=30, unique=True)  
    nom = models.CharField("Nom", max_length=20, unique=True)
    description = models.TextField("Déscription", max_length=600, unique=True)
    

    def __str__(self):
        return self.nom + " " + self.zone.commune.province.nom + " " + self.zone.commune.nom + " " + self.zone.nom + " " + self.medecin.user.first_name

    # def save(self, *args, **kwargs):
    #     if Cabinet.objects.exists():  # Vérifie si un enregistrement existe déjà
    #         return  # Si oui, ne fait rien
    #     super().save(*args, **kwargs)  # Sinon, enregistre normalement
    def save(self, *args, **kwargs):
        if Cabinet.objects.filter(medecin=self.medecin).exists():
            # Si un cabinet existe déjà pour ce médecin, ne fait rien et retourne
            return
        super().save(*args, **kwargs)