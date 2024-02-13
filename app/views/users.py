from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib import messages
from app.forms import UserForm,MedecinForm
from app.models import User
from app.views.medecins import addredir
from django.contrib.auth import authenticate ,login, logout
from django.contrib import messages

#affichage
def index(request):
    assert isinstance(request, HttpRequest)
    users=User.objects.all()
    return render(
        request,
        'app/admin/templates/users/index.html',
        {
            'users':users
        }
    )
    
    
#aller a la page add du province
# def add(request):
#     form = UserForm()
#     return render(
#         request,
#         'app/admin/templates/users/add.html',
#         {
#             'form':form
#         }
#     )

# def add(request):
#     if request.method == 'POST':
#         form = UserForm(request.POST)
#         if form.is_valid():
#             # Traitement du formulaire valide
#             form.save()
#             messages.success(request, 'L\'utilisateur a été ajouté avec succès.')
#             return redirect('users_list')
#         else:
#             # Traitement du formulaire invalide
#             messages.error(request, 'Le formulaire contient des erreurs. Veuillez corriger les erreurs ci-dessous.')
#     else:
#         form = UserForm()
#         if request.user.role == 'administrateur':
#             # Si l'utilisateur est un administrateur, afficher les choix "Médecin" et "Administrateur"
#             form.fields['role'].choices = [('administrateur', 'Administrateur'), ('medecin', 'Médecin')]
#         elif request.user.role == 'medecin':
#             form.fields['role'].choices = [('receptioniste','Receptioniste')]
#     return render(
#         request,
#         'app/admin/templates/users/add.html',
#         {
#             'form':form
#         }
#     )

def add(request):
    ROLE_CHOICES = (
        ('administrateur','Administrateur'),
        ('medecin','Médecin'),
        ('receptioniste','Receptioniste'),
        ('aucun','Aucun'),
    )
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            # Traitement du formulaire valide
            form.save()
            messages.success(request, 'L\'utilisateur a été ajouté avec succès.')
            return redirect('users_list')
        else:
            # Traitement du formulaire invalide
            messages.error(request, 'Le formulaire contient des erreurs. Veuillez corriger les erreurs ci-dessous.')
    else:
        form = UserForm()
        if request.user.is_authenticated:
            if request.user.role == 'administrateur':
                # Si l'utilisateur est un administrateur, afficher les choix "Administrateur" et "Médecin"
                form.fields['role'].choices = [('administrateur', 'Administrateur'), ('medecin', 'Médecin')]
            elif request.user.role == 'medecin':
                # Si l'utilisateur est un médecin, afficher le choix "Receptioniste"
                form.fields['role'].choices = [('receptioniste', 'Receptioniste')]
            else:
                # Si l'utilisateur n'a pas de rôle, afficher tous les choix
                form.fields['role'].choices = ROLE_CHOICES
        else:
            # Si l'utilisateur n'est pas authentifié, afficher tous les choix
            form.fields['role'].choices = ROLE_CHOICES
            
    return render(
        request,
        'app/admin/templates/users/add.html',
        {
            'form':form
        }
    )

  
#enregistrer
def store(request):
    if request.method == 'POST' :
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            role = user.role
            user_id = user.id
            messages.success(request, "L'utilisateur a été enregistrée avec succès !")
            if role == "medecin" :
                request.session['medecin_id'] = user_id
                form = MedecinForm(initial = {'user' : user})
                return render(
                    request,
                    'app/admin/templates/medecins/addredir.html',
                    {
                        'form':form
                    }
                )
        else :
            messages.success(request, form.errors)
        return redirect('/admin/templates/users')


#kuja kuri page ya mofi
def edit(request, id):
    assert isinstance(request, HttpRequest)
    if request.method=='GET':
        if id == 0:
            form = UserForm()
        else:
            user = User.objects.get(pk=id)
            form = UserForm(instance=user)
        return render(
            request,
            'app/admin/templates/users/edit.html',
            {
                'form': form
            }
        )


#update
def update(request, id):
    if request.method == 'POST':
        if id == 0:
            form = UserForm(request.POST)
        else:
            user = User.objects.get(pk=id)
            form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
        messages.success(request, "L'utilisateur a  été modifiée avec succès ! ")
        return redirect('/admin/templates/users')
    
    
#suppression
def delete(request, id):
    user = User.objects.get(pk=id)
    user.delete()
    messages.success(request, "L'utilisateur a été supprimée avec succès !")
    return redirect('/admin/templates/users')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.role == 'administrateur':
                return redirect('/admin/home')
            elif user.role == 'medecin':
                return redirect('/medecin/home')
            elif user.role == 'receptioniste':
                return redirect('/receptioniste/home')
                    
        else:
            messages.info(request, 'Username or password incorrect')   
    return render(
        request,
        'app/admin/templates/users/login.html'
    )
    
def  user_logout(request):
    logout(request)
    return redirect('/')
    