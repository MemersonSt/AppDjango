from django.db import models
from App.Departementos.models import DepartamentoModels

# Create your models here.
class ProyectoModels(models.Model):
    id = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=50)
    Descripcion = models.CharField(max_length=100)
    Fecha_Inicio = models.DateField()
    Fecha_Finalizacionn = models.DateField()
    Departemanto_Id = models.ForeignKey(DepartamentoModels, on_delete=models.CASCADE)