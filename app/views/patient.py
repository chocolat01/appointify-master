from django.http import HttpRequest
from django.shortcuts import redirect, render

def index(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/patient/home/index.html',
        {
           
        }
        
    )