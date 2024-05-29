from rest_framework import viewsets
from .models import RolModels
from .serializers import RolesSerializer

# Create your views here.
class RolesViewSet(viewsets.ModelViewSet):
    queryset = RolModels.objects.all()
    serializer_class = RolesSerializer