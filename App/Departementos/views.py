from rest_framework import viewsets
from .models import DepartamentoModels
from .serializers import DepartamentoSerializer

# Create your views here.
class DepartamentoViewSet(viewsets.ModelViewSet):
    serializer_class = DepartamentoSerializer
    queryset = DepartamentoModels.objects.all()