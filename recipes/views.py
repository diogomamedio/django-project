from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'recipes/home.html',context={
        'name': 'João'
    })

def sobre(request):
    return HttpResponse("Sobre Django!")
def contato(request):
    return HttpResponse("Contato Django!")