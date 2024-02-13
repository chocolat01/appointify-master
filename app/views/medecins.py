from django.http import HttpRequest
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from app.forms import MedecinForm
from app.models import Medecin, User
import os

#affichage
def index(request):
    assert isinstance(request, HttpRequest)
    medecins=Medecin.objects.all()
    return render(
        request,
        'app/admin/templates/medecins/index.html',
        {
            'medecins':medecins
        }
    )
    
    
#aller a la page add du province
def add(request):
    form = MedecinForm()
    return render(
        request,
        'app/admin/templates/medecins/add.html',
        {
            'form':form
        }
    )

def addredir(request):
    form = MedecinForm()
    return render(
        request,
        'app/admin/templates/medecins/addredir.html',
        {
            'form':form
        }
    )


#enregistrer
def store(request):
    if request.method == 'POST' :
        form = MedecinForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Medecin a été enregistrée avec succès !")
        else :
            messages.success(request, form.errors)
        return redirect('/admin/templates/medecins')
    
def storeMed(request):
    if request.method == 'POST' :
        form = MedecinForm(request.POST, request.FILES)
        medecin_id = request.session.get('medecin_id')
        user = get_object_or_404(User, pk = medecin_id)
        if form.is_valid():
            medecin = form.save(commit=False)
            medecin.user = user
            medecin.save()
            messages.success(request, "Medecin a été enregistrée avec succès !")
        else :
            messages.success(request, form.errors)
        return redirect('/admin/templates/medecins')


#kuja kuri page ya mofi
def edit(request, id):
    assert isinstance(request, HttpRequest)
    if request.method=='GET':
        if id == 0:
            form = MedecinForm()
        else:
            medecin = Medecin.objects.get(pk=id)
            form = MedecinForm(instance=medecin)
            return render(
                request,
                'app/admin/templates/medecins/edit.html',
                {
                    'form': form
                }
            )


#update
def update(request, id):
    if request.method == 'POST':
        if id == 0:
            form = MedecinForm(request.POST, request.FILES)
        else:
            medecin = Medecin.objects.get(pk=id)
            form = MedecinForm(request.POST, request.FILES, instance=medecin)
        if form.is_valid():
            if request.FILES.get('profile_photo', None)is not None:
                try:
                    os.remove(Medecin.profile_photo.url)
                except Exception as e:
                    print('Exception in removing old profile image: ', e)
                Medecin.profile_photo = request.FILES['profile_photo']
            form.save()
        messages.success(request, "Medecin a  été modifiée avec succès ! ")
        return redirect('/admin/templates/medecins')

# def update(request, id):
#     if request.method == 'POST':
#         if id == 0:
#             form = MedecinForm(request.POST, request.FILES)
#         else:
#             medecin = Medecin.objects.get(pk=id)
#             form = MedecinForm(request.POST, request.FILES, instance=medecin)
#         if form.is_valid():
#             medecin = form.save(commit=False)
            
#             if 'profile_photo' in request.FILES:
#                 if medecin.profile_photo:
#                     try:
#                         os.remove(medecin.profile_photo.path)
#                     except Exception as e:
#                         print('Exception in removing old profile image:', e)
                
#                 medecin.profile_photo = request.FILES['profile_photo']
            
#             medecin.save()
            
#             messages.success(request, "Le médecin a été modifié avec succès !")
#             return redirect('/admin/templates/medecins')
#     else:
#         # Cas où la requête n'est pas de type POST
#         # Effectuez ici toute autre opération nécessaire ou redirigez vers une autre page
#         return redirect('/admin/templates/medecins')  # Exemple de redirection vers la liste des médecins
    
#     # Si la requête n'est pas de type POST, vous devez renvoyer une réponse appropriée
#     # Vous pouvez personnaliser cela selon vos besoins
#     return render(request, 'update.html')  # Exemple de rendu d'un template de mise à jour
    
    
#suppression
def delete(request, id):
    medecin = Medecin.objects.get(pk=id)
    medecin.delete()
    messages.success(request, "Medecin a été supprimée avec succès !")
    return redirect('/admin/templates/medecins')