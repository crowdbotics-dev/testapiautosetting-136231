from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Testconnectors136231ViewSet

router = DefaultRouter()
router.register(
    "testconnectors136231", Testconnectors136231ViewSet, basename="testconnectors136231"
)

urlpatterns = [
    path("connectors/", include(router.urls)),
]
