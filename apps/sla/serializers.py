from rest_framework import serializers
from .models import SLAPolicy

class SLAPolicySerializer(serializers.ModelSerializer):
    """Serialize SLA policy data for API requests and responses."""

    priority_display = serializers.CharField(source='get_priority_display', read_only=True)
    organization_name = serializers.CharField(source='organization.name', read_only=True, allow_null=True)

    class Meta:  # pylint: disable=too-few-public-methods
        """Configure the serialized SLA policy fields."""
        model = SLAPolicy
        fields = [
            'id', 'name', 'priority', 'priority_display', 
            'response_time_hours', 'resolution_time_hours', 
            'organization', 'organization_name', 'is_active', 
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']