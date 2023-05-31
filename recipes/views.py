from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Luiz otavio',
    })


def contato(request):
    return render(request, 'temp/temp.html')


def sobre(request):
    return HttpResponse("Sobre")
