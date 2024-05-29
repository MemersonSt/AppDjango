from rest_framework.serializers import ModelSerializer
from .models import TareaModels

class TareaSerializer(ModelSerializer):
    class Meta:
        model = TareaModels
        fields = '__all__'