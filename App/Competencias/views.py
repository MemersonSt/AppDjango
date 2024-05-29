from rest_framework import viewsets
from .models import CompetenciaModel
from .serializers import CompetenciaSerializer

# Create your views here.
class CompetenciaViewSet(viewsets.ModelViewSet):
    serializer_class = CompetenciaSerializer
    queryset = CompetenciaModel.objects.all()