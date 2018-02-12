from rest_framework import serializers

from .models import Lead


class LeadSerializer(serializers.ModelSerializer):
    """Serialize lead's data."""

    class Meta:
        model = Lead
        fields = ('email', 'name', 'phone', 'message')
        read_only_fields = ('date',)
