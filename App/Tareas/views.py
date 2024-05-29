from rest_framework import viewsets
from .models import TareaModels
from .serializers import TareaSerializer

# Create your views here.
class TareaViewSet(viewsets.ModelViewSet):
    queryset = TareaModels.objects.all()
    serializer_class = TareaSerializer