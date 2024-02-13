from django.http import HttpRequest
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from app.forms import ReceptionisteForm, ReceptionistSignUpForm
from app.models import Receptioniste, User

#affichage
def index(request):
    assert isinstance(request, HttpRequest)
    receptionistes=Receptioniste.objects.all()
    return render(
        request,
        'app/medecin/templates/receptionistes/index.html',
        {
            'receptionistes':receptionistes
        }
    )
    
def addUser(request):
    form = ReceptionistSignUpForm()
    return render(
        request,
        'app/medecin/templates/receptionistes/user_add.html',
        {
            'form':form
        }
    )

def storeUser(request):
    if request.method == 'POST' :
        form = ReceptionistSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            role = user.role
            user_id = user.id
            messages.success(request, "L'utilisateur a été enregistrée avec succès !")
            if role == "receptioniste" :
                request.session['receptioniste_id'] = user_id
                form = ReceptionisteForm(initial = {'user' : user})
                return render(
                    request,
                    'app/medecin/templates/receptionistes/add.html',
                    {
                        'form':form
                    }
                )
        else :
            messages.success(request, form.errors)
        return redirect('/medecin/templates/receptionistes')

    
#aller a la page add du province
def add(request):
    form = ReceptionisteForm()
    return render(
        request,
        'app/medecin/templates/receptionistes/add.html',
        {
            'form':form
        }
    )


#enregistrer
def store(request):
    if request.method == 'POST' :
        form = ReceptionisteForm(request.POST)
        receptioniste_id = request.session.get('receptioniste_id')
        user = get_object_or_404(User, pk = receptioniste_id)
        if form.is_valid():
            receptioniste = form.save(commit=False)
            receptioniste.user = user
            receptioniste.save()
            messages.success(request, "Receptioniste a été enregistrée avec succès !")
        else :
            messages.success(request, form.errors)
        return redirect('/medecin/templates/receptionistes')


#kuja kuri page ya mofi
def edit(request, id):
    assert isinstance(request, HttpRequest)
    if request.method=='GET':
        if id == 0:
            form = ReceptionisteForm()
        else:
            receptioniste= Receptioniste.objects.get(pk=id)
            form = ReceptionisteForm(instance=receptioniste)
            return render(
                request,
                'app/medecin/templates/receptionistes/edit.html',
                {
                    'form': form
                }
            )


#update
def update(request, id):
    if request.method == 'POST':
        if id == 0:
            form = ReceptionisteForm(request.POST)
        else:
            receptioniste = Receptioniste.objects.get(pk=id)
            form = ReceptionisteForm(request.POST, instance=receptioniste)
        if form.is_valid():
            form.save()
        messages.success(request, "receptioniste a  été modifiée avec succès ! ")
        return redirect('/medecin/templates/receptionistes')
    
    
#suppression
def delete(request, id):
    receptioniste= Receptioniste.objects.get(pk=id)
    receptioniste.delete()
    messages.success(request, " receptioniste a été supprimée avec succès !")
    return redirect('/medecin/templates/receptionistes')