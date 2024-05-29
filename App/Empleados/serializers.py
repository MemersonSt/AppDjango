from rest_framework.serializers import ModelSerializer
from .models import EmpleadoModel

class EmpleadoSerializer(ModelSerializer):
    class Meta:
        model = EmpleadoModel
        fields = '__all__'