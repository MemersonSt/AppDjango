from django.db import models
from App.Departementos.models import DepartamentoModels

# Create your models here.
class RolModels(models.Model):
    id = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=50)
    Descripcion = models.CharField(max_length=100)
    Departamento_Id = models.ForeignKey(DepartamentoModels, on_delete=models.CASCADE)

    def __str__(self):
        return self.Nombre