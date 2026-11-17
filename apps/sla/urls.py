from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SLAPolicyViewSet

router = DefaultRouter()
router.register(r'slas', SLAPolicyViewSet, basename='sla')

urlpatterns = [
    path('', include(router.urls)),
]