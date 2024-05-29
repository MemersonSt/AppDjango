from rest_framework import viewsets
from .models import EmpleadoModel
from .serializers import EmpleadoSerializer

# Create your views here.
class EmpleadoViewSet(viewsets.ModelViewSet):
    serializer_class = EmpleadoSerializer
    queryset = EmpleadoModel.objects.all()