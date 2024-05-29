from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'competencias', views.CompetenciaViewSet)
urlpatterns = router.urls