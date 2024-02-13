from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib import messages
from app.forms import ProvinceForm
from app.models import Province

#affichage
def index(request):
    assert isinstance(request, HttpRequest)
    provinces=Province.objects.all()
    return render(
        request,
        'app/admin/templates/provinces/index.html',
        {
            'provinces':provinces
        }
    )
    
    
#aller a la page add du province
def add(request):
    form = ProvinceForm()
    return render(
        request,
        'app/admin/templates/provinces/add.html',
        {
            'form':form
        }
    )


#enregistrer
def store(request):
    if request.method == 'POST' :
        form = ProvinceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "La province a été enregistrée avec succès !")
        else :
            messages.success(request, form.errors)
        return redirect('/admin/templates/provinces')


#kuja kuri page ya mofi
def edit(request, id):
    assert isinstance(request, HttpRequest)
    if request.method=='GET':
        if id == 0:
            form = ProvinceForm()
        else:
            province = Province.objects.get(pk=id)
            form = ProvinceForm(instance=province)
            return render(
                request,
                'app/admin/templates/provinces/edit.html',
                {
                    'form': form
                }
            )


#update
def update(request, id):
    if request.method == 'POST':
        if id == 0:
            form = ProvinceForm(request.POST)
        else:
            province = Province.objects.get(pk=id)
            form = ProvinceForm(request.POST, instance=province)
        if form.is_valid():
            form.save()
        messages.success(request, "La province a  été modifiée avec succès ! ")
        return redirect('/admin/templates/provinces')
    
    
#suppression
def delete(request, id):
    province = Province.objects.get(pk=id)
    province.delete()
    messages.success(request, "La province a été supprimée avec succès !")
    return redirect('/admin/templates/provinces')