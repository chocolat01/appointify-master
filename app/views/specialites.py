from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib import messages
from app.forms import SpecialiteForm
from app.models import Specialite

#affichage
def index(request):
    assert isinstance(request, HttpRequest)
    specialites=Specialite.objects.all()
    return render(
        request,
        'app/admin/templates/specialites/index.html',
        {
            'specialites':specialites
        }
    )
    
    
#aller a la page add du province
def add(request):
    form = SpecialiteForm()
    return render(
        request,
        'app/admin/templates/specialites/add.html',
        {
            'form':form
        }
    )


#enregistrer
def store(request):
    if request.method == 'POST' :
        form = SpecialiteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "specialite a été enregistrée avec succès !")
        else :
            messages.success(request, form.errors)
        return redirect('/admin/templates/specialites')


#kuja kuri page ya mofi
def edit(request, id):
    assert isinstance(request, HttpRequest)
    if request.method=='GET':
        if id == 0:
            form = SpecialiteForm()
        else:
            specialite = Specialite.objects.get(pk=id)
            form = SpecialiteForm(instance=specialite)
        return render(
            request,
            'app/admin/templates/specialites/edit.html',
            {
                'form': form
            }
        )


#update
def update(request, id):
    if request.method == 'POST':
        if id == 0:
            form = SpecialiteForm(request.POST)
        else:
            specialite = Specialite.objects.get(pk=id)
            form = SpecialiteForm(request.POST, instance=specialite)
        if form.is_valid():
            form.save()
        messages.success(request, "La specialite a  été modifiée avec succès ! ")
        return redirect('/admin/templates/specialites')
    
    
#suppression
def delete(request, id):
    specialite = Specialite.objects.get(pk=id)
    specialite.delete()
    messages.success(request, "La specialite a été supprimée avec succès !")
    return redirect('/admin/templates/specialites')