from rest_framework.serializers import ModelSerializer
from App.Empleados.models import EmpleadoModel

class LoginSerializer(ModelSerializer):
    class Meta:
        model = EmpleadoModel
        fields = ['Correo', 'password']

class TokenSerializer(ModelSerializer):
    class Meta:
        model = EmpleadoModel
        fields = ['id', 'Nombre', 'Correo', 'Fecha_Nacimiento', 'Numero_Telefono', 'Departamento_Id', 'Fecha_Contratacion', 'Cargo', 'Salario']