from django.http import HttpRequest
from django.shortcuts import render

def index(request):
    assert isinstance(request,HttpRequest)
    return render(
        request,
        'app/home/index.html',
    )