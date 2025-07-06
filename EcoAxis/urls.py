from django.urls import path, include
from rest_framework import routers
from .views import (
    UsuarioViewSet, EmpresaViewSet, CatalogoViewSet, SucursalViewSet,
    ProductosEmpresasViewSet, SucursalProductosEmpresasViewSet, TipoTecnicoViewSet,
    TecnicoViewSet, ReporteViewSet, MantenimientoViewSet, SubscripcionViewSet,
    ReciboCfeViewSet, TicketViewSet
)

router = routers.DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'empresas', EmpresaViewSet)
router.register(r'catalogos', CatalogoViewSet)
router.register(r'sucursales', SucursalViewSet)
router.register(r'productos-empresas', ProductosEmpresasViewSet)
router.register(r'sucursal-productos-empresas', SucursalProductosEmpresasViewSet)
router.register(r'tipos-tecnico', TipoTecnicoViewSet)
router.register(r'tecnicos', TecnicoViewSet)
router.register(r'reportes', ReporteViewSet)
router.register(r'mantenimientos', MantenimientoViewSet)
router.register(r'subscripciones', SubscripcionViewSet)
router.register(r'recibos-cfe', ReciboCfeViewSet)
router.register(r'tickets', TicketViewSet)

urlpatterns = [
    path('', include(router.urls)),
]