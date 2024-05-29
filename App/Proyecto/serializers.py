from rest_framework import serializers
from .models import ProyectoModels

class ProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProyectoModels
        fields = '__all__'