from rest_framework import routers
from .views import SubscripcionViewSet

router = routers.DefaultRouter()
router.register(r'subscripciones', SubscripcionViewSet)

urlpatterns = router.urls