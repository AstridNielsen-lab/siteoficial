from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_inicial, name='pagina_inicial'),  # URL raiz
    path('lista-filmes/', views.lista_filmes, name='lista_filmes'),

]
