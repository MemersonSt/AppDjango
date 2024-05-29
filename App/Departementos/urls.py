from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'departamentos', views.DepartamentoViewSet)
urlpatterns = router.urls
