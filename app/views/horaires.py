from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib import messages
from app.forms import HoraireForm
from app.models import Horaire

#affichage
def index(request):
    assert isinstance(request, HttpRequest)
    horaires=Horaire.objects.all()
    return render(
        request,
        'app/receptioniste/templates/horaires/index.html',
        {
            'horaires':horaires
        }
    )
    
    
#aller a la page add du province
def add(request):
    form = HoraireForm()
    return render(
        request,
        'app/receptioniste/templates/horaires/add.html',
        {
            'form':form
        }
    )


#enregistrer
def store(request):
    if request.method == 'POST' :
        form = HoraireForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "specialite a été enregistrée avec succès !")
        else :
            messages.success(request, form.errors)
        return redirect('/receptioniste/templates/horaires')


#kuja kuri page ya mofi
def edit(request, id):
    assert isinstance(request, HttpRequest)
    if request.method=='GET':
        if id == 0:
            form = HoraireForm()
        else:
            horaire = Horaire.objects.get(pk=id)
            form = HoraireForm(instance=horaire)
        return render(
            request,
            'app/receptioniste/templates/horaires/edit.html',
            {
                'form': form
            }
        )


#update
def update(request, id):
    if request.method == 'POST':
        if id == 0:
            form = HoraireForm(request.POST)
        else:
            horaire= Horaire.objects.get(pk=id)
            form = HoraireForm(request.POST, instance=horaire)
        if form.is_valid():
            form.save()
        messages.success(request, "La specialite a  été modifiée avec succès ! ")
        return redirect('/receptioniste/templates/horaires')
    
    
#suppression
def delete(request, id):
    horaire = Horaire.objects.get(pk=id)
    horaire.delete()
    messages.success(request, "La specialite a été supprimée avec succès !")
    return redirect('/receptioniste/templates/horaires')