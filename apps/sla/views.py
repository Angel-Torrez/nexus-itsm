from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import SLAPolicy
from .serializers import SLAPolicySerializer

# pylint: disable=too-many-ancestors
class SLAPolicyViewSet(viewsets.ModelViewSet):
    """API endpoints for managing SLA policies."""

    queryset = SLAPolicy.objects.all()  # pylint: disable=no-member
    serializer_class = SLAPolicySerializer
    permission_classes = [IsAuthenticated]