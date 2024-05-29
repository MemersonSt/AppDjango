from rest_framework import viewsets
from .models import ProyectoModels
from .serializers import ProyectoSerializer

# Create your views here.
class ProyectoViewSet(viewsets.ModelViewSet):
    queryset = ProyectoModels.objects.all()
    serializer_class = ProyectoSerializer