from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib import messages
from app.models import Zone,Province,Commune
from app.forms import ZoneForm



#affichage
def index(request):
    assert isinstance(request, HttpRequest)
    zones=Zone.objects.all()
    return render(
        request,
        'app/admin/templates/zones/index.html',
        {
            'zones':zones
        }
    )
    
    
#aller a la page add du province
def add(request):
    form = ZoneForm()
    provinces = Province.objects.all()
    return render(
        request,
        'app/admin/templates/zones/add.html',
        {
            'form':form,
            'provinces':provinces
        }
    )


#enregistrer
def store(request):
    if request.method == 'POST' :
        form = ZoneForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "La Zone a été enregistrée avec succès !")
        else :
            messages.success(request, form.errors)
        return redirect('/admin/templates/zones')


#kuja kuri page ya mofi
def edit(request, id):
    assert isinstance(request, HttpRequest)
    if request.method=='GET':
        if id == 0:
            form = ZoneForm()
        else:
            zone = Zone.objects.get(pk=id)
            form = ZoneForm(instance=zone)
        return render(
            request,
            'app/admin/templates/zones/edit.html',
            {
                'form': form,
                
                
            }
        )


#update
def update(request, id):
    if request.method == 'POST':
        if id == 0:
            form = ZoneForm(request.POST)
        else:
            zone = Zone.objects.get(pk=id)
            form = ZoneForm(request.POST, instance=zone)
        if form.is_valid():
            form.save()
        messages.success(request, "La zone a  été modifiée avec succès ! ")
        return redirect('/admin/templates/zones')
    
    
#suppression
def delete(request, id):
    zone = Zone.objects.get(pk=id)
    zone.delete()
    messages.success(request, "La zone a été supprimée avec succès !")
    return redirect('/admin/templates/zones')

def getCommunes(request):
    province_id = request.GET.get('province_id')
    communes = Commune.objects.filter(province_id = province_id).order_by('nom')
    return render(
        request,
        'app/admin/templates/zones/getCommunes.html',
        {
            'communes': communes
        }
    )
