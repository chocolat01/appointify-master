from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib import messages
from app.models import Zone,Province,Commune,Cabinet,Medecin
from app.forms import CabinetForm



#affichage
# def index(request):
#     assert isinstance(request, HttpRequest)
#     # Vérifier si l'utilisateur est connecté
#     if request.user.is_authenticated:
#         # Récupérer les cabinets associés à l'utilisateur connecté
#         # cabinets = Cabinet.objects.filter(medecin=Medecin.objects.filter(user=list(Medecin.objects.filter(id=request.user.id).values("id"))[0]['id']))
#         user_id=list(Medecin.objects.filter(id=request.user.id).values("id"))[0]['id']
#         medecin_id=list(Medecin.objects.filter(user=user_id).values('id'))[0]['id']
#         cabinets=Cabinet.objects.filter(medecin=medecin_id)
#     return render(
#         request,
#         'app/medecin/templates/cabinets/index.html',
#         {
#             'cabinets':cabinets,
#         }
#     )
    
def index(request):
    cabinets = []
    if request.user.is_authenticated:
        try:
            medecin = Medecin.objects.get(user=request.user)
            cabinets = Cabinet.objects.filter(medecin=medecin)
        except Medecin.DoesNotExist:
            pass
    return render(request, 'app/medecin/templates/cabinets/index.html', {'cabinets': cabinets})    
#aller a la page add du province

def add(request):
    form = CabinetForm()
    provinces = Province.objects.all()
    communes = Commune.objects.all()
    return render(
        request,
        'app/medecin/templates/cabinets/add.html',
        {
            'form':form,
            'provinces':provinces,
            'communes':communes
        }
    )


#enregistrer
def store(request):
    if request.method == 'POST' :
        form = CabinetForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Le cabinet a été enregistrée avec succès !")
        else :
            messages.success(request, form.errors)
        return redirect('/medecin/templates/cabinets')


#kuja kuri page ya mofi
def edit(request, id):
    assert isinstance(request, HttpRequest)
    if request.method=='GET':
        if id == 0:
            form = CabinetForm()
        else:
            cabinet = Cabinet.objects.get(pk=id)
            form = CabinetForm(instance=cabinet)
        return render(
            request,
            'app/medecin/templates/cabinets/edit.html',
            {
                'form': form,
                
                
            }
        )


#update
def update(request, id):
    if request.method == 'POST':
        if id == 0:
            form = CabinetForm(request.POST)
        else:
            cabinet = Cabinet.objects.get(pk=id)
            form = CabinetForm(request.POST, instance=cabinet)
        if form.is_valid():
            form.save()
        messages.success(request, "Le Cabinet a  été modifiée avec succès ! ")
        return redirect('/medecin/templates/cabinets')
    
    
#suppression
def delete(request, id):
    cabinet = Cabinet.objects.get(pk=id)
    cabinet.delete()
    messages.success(request, "Le Cabinet a été supprimée avec succès !")
    return redirect('/medecin/templates/cabinets')

def getCommunes(request):
    province_id = request.GET.get('province_id')
    communes = Commune.objects.filter(province_id = province_id).order_by('nom')
    return render(
        request,
        'app/medecin/templates/cabinets/getCommunes.html',
        {
            'communes': communes
        }
    )
    
def getZones(request):
    commune_id = request.GET.get('commune_id')
    zones = Zone.objects.filter(zone_id = commune_id).order_by('nom')
    return render(
        request,
        'app/medecin/templates/cabinets/getZones.html',
        {
            'zones': zones
        }
    )
