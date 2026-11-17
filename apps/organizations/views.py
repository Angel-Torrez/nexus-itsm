from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Organization
from .serializers import OrganizationSerializer

# pylint: disable=too-many-ancestors
class OrganizationViewSet(viewsets.ModelViewSet):
    """ViewSet for managing organizations."""

    queryset = Organization.objects.all()  # pylint: disable=no-member
    serializer_class = OrganizationSerializer
    permission_classes = [IsAuthenticated]