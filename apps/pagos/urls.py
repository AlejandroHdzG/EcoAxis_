from django.urls import path
from .views import (
    PagoSubscripcionCreateView,
    PagoSubscripcionListView,
    PagoSubscripcionDetailView,
    PagoSubscripcionUpdateView,
    PagoSubscripcionDeleteView,
)

urlpatterns = [
    path('pagos/', PagoSubscripcionListView.as_view(), name='listar_pagos'),
    path('pagos/crear/', PagoSubscripcionCreateView.as_view(), name='crear_pago'),
    path('pagos/<uuid:pago_uuid>/', PagoSubscripcionDetailView.as_view(), name='ver_pago'),
    path('pagos/<uuid:pago_uuid>/editar/', PagoSubscripcionUpdateView.as_view(), name='editar_pago'),
    path('pagos/<uuid:pago_uuid>/eliminar/', PagoSubscripcionDeleteView.as_view(), name='eliminar_pago'),
]
