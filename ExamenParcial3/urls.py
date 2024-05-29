"""
URL configuration for ExamenParcial3 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/examen/', include('App.Departementos.urls')),
    path('api/examen/', include('App.Empleados.urls')),
    path('api/examen/', include('App.Roles.urls')),
    path('api/examen/', include('App.Competencias.urls')),
    path('api/examen/', include('App.Tareas.urls')),
    path('api/examen/', include('App.Proyecto.urls')),
]
