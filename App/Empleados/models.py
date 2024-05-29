from django.db import models
from App.Departementos.models import DepartamentoModels

# Create your models here.
class EmpleadoModel(models.Model):
    id = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=50)
    Correo = models.CharField(max_length=50)
    Fecha_Nacimiento = models.DateField()
    Numero_Telefono = models.CharField(max_length=10)
    Departamento_Id = models.ForeignKey(DepartamentoModels, on_delete=models.CASCADE)
    Fecha_Contratacion = models.DateField()
    Cargo = models.CharField(max_length=50)
    Salario = models.FloatField()