from rest_framework import serializers

from leads.models import Lead


class AccountSerializer(serializers.ModelSerializer):
    """Serialize lead's data."""

    class Meta:
        model = Lead
        fields = ('id', 'email', 'name', 'phone', 'message')
