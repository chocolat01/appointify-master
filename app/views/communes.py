from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib import messages
from app.forms import CommuneForm
from app.models import Commune

#affichage
def index(request):
    assert isinstance(request, HttpRequest)
    communes=Commune.objects.all()
    return render(
        request,
        'app/admin/templates/communes/index.html',
        {
            'communes':communes
        }
    )
    
    
#aller a la page add du province
def add(request):
    form = CommuneForm()
    return render(
        request,
        'app/admin/templates/communes/add.html',
        {
            'form':form
        }
    )


#enregistrer
def store(request):
    if request.method == 'POST' :
        form = CommuneForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "La Commune a été enregistrée avec succès !")
        else :
            messages.success(request, form.errors)
        return redirect('/admin/templates/communes')


#kuja kuri page ya mofi
def edit(request, id):
    assert isinstance(request, HttpRequest)
    if request.method=='GET':
        if id == 0:
            form = CommuneForm()
        else:
            commune = Commune.objects.get(pk=id)
            form = CommuneForm(instance=commune)
        return render(
            request,
            'app/admin/templates/communes/edit.html',
            {
                'form': form
            }
        )


#update
def update(request, id):
    if request.method == 'POST':
        if id == 0:
            form = CommuneForm(request.POST)
        else:
            commune = Commune.objects.get(pk=id)
            form = CommuneForm(request.POST, instance=commune)
        if form.is_valid():
            form.save()
        messages.success(request, "La communea  été modifiée avec succès ! ")
        return redirect('/admin/templates/communes')
    
    
#suppression
def delete(request, id):
    commune = Commune.objects.get(pk=id)
    commune.delete()
    messages.success(request, "La commune a été supprimée avec succès !")
    return redirect('/admin/templates/communes')