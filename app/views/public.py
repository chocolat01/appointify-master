from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.db.models import Count

from app.models import Medecin, Cabinet, Horaire
def index(request):
    assert isinstance(request, HttpRequest)
    medecins_par_specialites =  Medecin.objects.order_by('specialite__nom')
    medecins_par_specialite =  get_medecins_par_specialite(medecins_par_specialites)
    return render(
        request,
        'app/public/home/index.html',
        {
           'medecins_par_specialite':medecins_par_specialite,
        }
        
    )
    

# def get_medecins_par_specialite(queryset):
#     medecins_par_specialite = {}
#     for medecin in queryset:
#         specialite_nom = medecin.specialite.nom
#         medecin_nom = f"{medecin.user.first_name} {medecin.user.last_name}"
#         if specialite_nom not in medecins_par_specialite:
#             medecins_par_specialite[specialite_nom] = [medecin_nom]
#         else:
#             medecins_par_specialite[specialite_nom].append(medecin_nom)
#     return medecins_par_specialite

def get_medecins_par_specialite(queryset):
    medecins_par_specialite = {}
    for medecin in queryset:
        specialite_nom = medecin.specialite.nom
        medecin = medecin
        if specialite_nom not in medecins_par_specialite:
            medecins_par_specialite[specialite_nom] = [medecin]
        else:
            medecins_par_specialite[specialite_nom].append(medecin)
    return medecins_par_specialite


# def description(request, id):
#     assert isinstance(request, HttpRequest)
#     if request.method=='GET':
#         if id == 0:
#             print("Salut")
#         else:
#             medecin = Medecin.objects.filter(pk=id)
#             return render(
#                 request,
#                 'app/public/templates/med_descriptions.html',
#                 {
#                     'medecin': medecin
#                 }
#             )

def description(request, id):
    assert isinstance(request, HttpRequest)
    if request.method=='GET':
        if id == 0:
            print("Salut")
        else:
            # Utiliser la méthode get au lieu de filter pour obtenir un objet unique
            medecin = Medecin.objects.get(pk=id)
            cabinet = Cabinet.objects.get(pk=id)
            cabinet_id = Cabinet.objects.all().filter(medecin_id=id).values_list('id', flat=True).first()
            # Possibilité d'envoyer un nom à la vue avec {'medecin': medecin(nom=
            horaires = Horaire.objects.all().filter(cabinet_id=cabinet_id)
            return render(
                request,
                'app/public/templates/med_descriptions.html',
                {
                    'medecin': medecin,
                    'cabinet': cabinet,
                    'horaires': horaires
                }
            )

def choix_créneaux(request,id):
    # On récupère le cabinet dont l'id est passé en paramètre
    cabinet = Cabinet.objects.get(pk=id)
    # On récupère les créneaux horaires du cabinet, triés par date
    horaires = Horaire.objects.filter(cabinet=cabinet).order_by("date")
    # On crée un dictionnaire qui contient le cabinet et les horaires
    context = {"cabinet": cabinet, "horaires": horaires}
    # On rend le template HTML qui affiche les créneaux, en passant le contexte
    return render(request, "app/public/templates/choix_creneau.html", context)

    
