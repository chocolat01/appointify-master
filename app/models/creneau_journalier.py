from django.db import models
from app.models import Horaire
from django.shortcuts import redirect, render
from django.contrib import messages

class CreneauJournalier(models.Model):
    horaire = models.ForeignKey("Horaire", on_delete=models.CASCADE)
    debut = models.TimeField("Début")
    fin = models.TimeField("Fin")
    pris = models.BooleanField("Pris", default=False)

    def __str__(self) -> str:
        return self.debut + " - " + self.fin
