from django.shortcuts import render
from django.http import HttpRequest

from .forms import ContactFormForm

def indice(request):
    return render(request, 'index.html', {})

def acerca(request):
    return render(request, 'about.html', {})

def bienvenido(request):
    return render(request, 'welcome.html', {})

def contacto(request: HttpRequest):
    if request.method == 'POST':
        form = ContactFormForm(request.POST)

        if form.is_valid():
            print("Crear contacto")

    else:
        form = ContactFormForm()
    return render(request, 'contacto.html', {'form': form})