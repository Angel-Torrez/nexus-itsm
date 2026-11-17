from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Ticket
from .serializers import TicketSerializer

class TicketViewSet(viewsets.ModelViewSet):
    """Provide authenticated CRUD operations for tickets."""
    # pylint: disable=too-many-ancestors
    queryset = Ticket.objects.all()  # pylint: disable=no-member
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Inyecta el usuario autenticado al crear el ticket
        serializer.save(created_by=self.request.user)