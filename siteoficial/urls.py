from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('siteapp.urls')),  # Inclua as URLs do aplicativo 'siteapp'
    path('admin/', admin.site.urls),
]
