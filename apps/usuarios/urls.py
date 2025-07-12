from rest_framework import routers
from django.urls import path
from .views import UsuarioViewSet, TipoTecnicoViewSet, TecnicoViewSet, RegistroUsuarioView, UserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = routers.DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'tipos-tecnico', TipoTecnicoViewSet)
router.register(r'tecnicos', TecnicoViewSet)

urlpatterns = [
    path('registro/', RegistroUsuarioView.as_view(), name='registro_usuario'),
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/me', UserView.as_view(), name='user_detail'),
]

urlpatterns += router.urls