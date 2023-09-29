from django.shortcuts import render
from .models import Filme

def lista_filmes(request):
    filmes = Filme.objects.all()
    return render(request, 'siteapp/lista_filmes.html', {'filmes': filmes})
from django.shortcuts import render

# Create your views here.
# siteapp/views.py
from django.shortcuts import render

def pagina_inicial(request):
    filmes = Filme.objects.all()
    return render(request, 'siteapp/pagina_inicial.html', {'filmes': filmes})
