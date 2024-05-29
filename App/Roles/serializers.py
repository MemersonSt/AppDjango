from rest_framework import serializers
from .models import RolModels

class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RolModels
        fields = '__all__'