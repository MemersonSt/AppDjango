from rest_framework.serializers import ModelSerializer
from .models import DepartamentoModels

class DepartamentoSerializer(ModelSerializer):
    class Meta:
        model = DepartamentoModels
        fields = '__all__'