from rest_framework import serializers
from .models import Organization

class OrganizationSerializer(serializers.ModelSerializer):
    """Serialize organization records."""

    class Meta:
        """Configuration for the organization serializer."""

        # pylint: disable=too-few-public-methods
        model = Organization
        fields = ['id', 'name', 'code', 'description', 'is_active', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']