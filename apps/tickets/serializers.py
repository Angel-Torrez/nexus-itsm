from rest_framework import serializers
from .models import Ticket

class TicketSerializer(serializers.ModelSerializer):
    """Serializer para tickets del sistema."""

    status_display = serializers.CharField(source='get_status_display', read_only=True)
    priority_display = serializers.CharField(source='get_priority_display', read_only=True)
    organization_name = serializers.CharField(source='organization.name', read_only=True)
    created_by_username = serializers.CharField(source='created_by.username', read_only=True)
    assigned_to_username = serializers.CharField(source='assigned_to.username', read_only=True, allow_null=True)

    # pylint: disable=too-few-public-methods
    class Meta:
        """Configuración del serializador de tickets."""

        model = Ticket
        fields = [
            'id', 'title', 'description', 'status', 'status_display',
            'priority', 'priority_display', 'organization', 'organization_name',
            'sla_policy', 'created_by', 'created_by_username',
            'assigned_to', 'assigned_to_username', 'created_at',
            'updated_at', 'resolved_at'
        ]
        read_only_fields = ['id', 'created_by', 'created_at', 'updated_at', 'resolved_at']

    def create(self, validated_data):
        # Asignar automáticamente al usuario autenticado como creador del ticket
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            validated_data['created_by'] = request.user
        return super().create(validated_data)