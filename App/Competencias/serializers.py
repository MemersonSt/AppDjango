from rest_framework.serializers import ModelSerializer
from .models import CompetenciaModel

class CompetenciaSerializer(ModelSerializer):
    class Meta:
        model = CompetenciaModel
        fields = '__all__'