from rest_framework import routers
from .views import UsuarioViewSet, TipoTecnicoViewSet, TecnicoViewSet

router = routers.DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'tipos-tecnico', TipoTecnicoViewSet)
router.register(r'tecnicos', TecnicoViewSet)

urlpatterns = router.urls