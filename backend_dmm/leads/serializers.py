from rest_framework import serializers

from .models import Brief, Lead


class BriefSerializer(serializers.ModelSerializer):
    """Serialize brief data."""

    class Meta:
        model = Brief
        fields = ('industry', 'experience', 'aim', 'stage', 'strategies',
                  'audience', 'callcenter', 'marketing', 'payment', 'lead')
        read_only_fields = ('date',)


class LeadSerializer(serializers.ModelSerializer):
    """Serialize lead's data."""

    class Meta:
        model = Lead
        fields = ('email', 'name', 'phone', 'message', 'date', 'brief')
        read_only_fields = ('date', 'brief')
        extra_kwargs = {'date': {'format': '%Y-%m-%d %H:%M'}}
        depth = 1
