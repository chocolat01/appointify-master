from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib import messages
from datetime import timedelta
from app.forms import CreneauJournalierForm
from datetime import datetime, date, time, timedelta
from app.models import Horaire, creneau_journalier


def index(request):
    assert isinstance(request, HttpRequest)
    creneauJournaliers=creneau_journalier.CreneauJournalier.objects.all()
    return render(
        request,
        'app/receptioniste/templates/creneauJournalier/index.html',
        {
            'creneauJournaliers': creneauJournaliers
        }
    )
    
    
#aller a la page add du province
def add(request):
    form = CreneauJournalierForm()
    return render(
        request,
        'app/receptioniste/templates/creneauJournalier/add.html',
        {
            'form':form
        }
    )


#enregistrer
def store(request):
    if request.method == 'POST' :
        form = CreneauJournalierForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Le Créneau Journalier a été enregistrée avec succès !")
        else :
            messages.success(request, form.errors)
        return redirect('/receptioniste/templates/creneauJournalier')


#kuja kuri page ya mofi
def edit(request, id):
    assert isinstance(request, HttpRequest)
    if request.method=='GET':
        if id == 0:
            form = CreneauJournalierForm()
        else:
            creneauJournalier = creneau_journalier.CreneauJournalier.objects.get(pk=id)
            form = CreneauJournalierForm(instance=creneauJournalier)
        return render(
            request,
            'app/receptioniste/templates/creneauJournalier/edit.html',
            {
                'form': form
            }
        )


#update
def update(request, id):
    if request.method == 'POST':
        if id == 0:
            form = CreneauJournalierForm(request.POST)
        else:
            creneauJournalier= creneau_journalier.CreneauJournalier.objects.get(pk=id)
            form = CreneauJournalierForm(request.POST, instance=creneauJournalier)
        if form.is_valid():
            form.save()
        messages.success(request, "Le Créneau Journalier a  été modifiée avec succès ! ")
        return redirect('/receptioniste/templates/creneauJournalier')
    
    
#suppression
def delete(request, id):
    creneauJournalier = creneau_journalier.CreneauJournalier.objects.get(pk=id)
    creneauJournalier.delete()
    messages.success(request, "Le Créneau Journalier a été supprimée avec succès !")
    return redirect('/receptioniste/templates/creneauJournalier')

# def créer_créneaux_journaliers(horaire):
#     # On récupère l'heure de début et l'heure de fin du créneau horaire
#     debut = horaire.heure_debut
#     fin = horaire.heure_fin

#     # On initialise une variable qui représente la durée d'un créneau journalier (30 minutes)
#     durée = timedelta(minutes=30)

#     # On crée une boucle qui parcourt les tranches de 30 minutes entre l'heure de début et l'heure de fin
#     while debut < fin:
#         # On crée un objet creneau_journalier.CreneauJournalier avec le créneau horaire, l'heure de début et l'heure de fin de la tranche
#         créneau_journalier = creneau_journalier.CreneauJournalier(horaire=horaire, debut=debut, fin=debut + durée)
#         # On enregistre l'objet creneau_journalier.CreneauJournalier dans la base de données
#         créneau_journalier.save()
#         # On met à jour l'heure de début pour la prochaine tranche
#         debut = debut + durée

def créer_créneaux_journaliers(horaire):
    # On récupère l'heure de début et l'heure de fin du créneau horaire
    debut = horaire.heure_debut
    fin = horaire.heure_fin

    # On récupère la date du créneau horaire
    jour = horaire.date

    # On initialise une variable qui représente la durée d'un créneau journalier (30 minutes)
    durée = timedelta(minutes=30)

    # On combine la date et l'heure de début pour créer un objet de type datetime.datetime
    debut_datetime = datetime.combine(jour, debut)

    # On combine la date et l'heure de fin pour créer un objet de type datetime.datetime
    fin_datetime = datetime.combine(jour, fin)

    # On crée une boucle qui parcourt les tranches de 30 minutes entre l'heure de début et l'heure de fin
    while debut_datetime < fin_datetime:
        # On crée un objet creneau_journalier.CreneauJournalier avec le créneau horaire, l'heure de début et l'heure de fin de la tranche
        créneau_journalier = creneau_journalier.CreneauJournalier(horaire=horaire, debut=debut_datetime.time(), fin=(debut_datetime + durée).time())
        # On enregistre l'objet creneau_journalier.CreneauJournalier dans la base de données
        créneau_journalier.save()
        # On met à jour l'heure de début pour la prochaine tranche
        debut_datetime = debut_datetime + durée