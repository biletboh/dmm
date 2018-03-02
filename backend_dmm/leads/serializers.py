from rest_framework import serializers

from .models import Brief, Lead


class BriefSerializer(serializers.ModelSerializer):
    """Serialize brief data."""

    class Meta:
        model = Brief
        fields = ('industry', 'experience', 'aim', 'stage', 'strategies',
                  'audience', 'callcenter', 'marketing', 'payment', 'lead')
        read_only_fields = ('date',)


class LeadBriefSerializer(serializers.ModelSerializer):
    """Serialize brief to display human readable choices."""

    industry = serializers.SerializerMethodField()
    experience = serializers.SerializerMethodField()
    aim = serializers.SerializerMethodField()
    stage = serializers.SerializerMethodField()
    strategies = serializers.SerializerMethodField()
    audience = serializers.SerializerMethodField()
    callcenter = serializers.SerializerMethodField()
    marketing = serializers.SerializerMethodField()
    payment = serializers.SerializerMethodField()

    class Meta:
        model = Brief
        fields = ('industry', 'experience', 'aim', 'stage', 'strategies',
                  'audience', 'callcenter', 'marketing', 'payment')
        read_only_fields = ('date',)

    def get_industry(self, obj):
        return obj.get_industry_display()

    def get_experience(self, obj):
        return obj.get_experience_display()

    def get_aim(self, obj):
        return obj.get_aim_display()

    def get_stage(self, obj):
        return obj.get_stage_display()

    def get_strategies(self, obj):
        return obj.get_strategies_display()

    def get_audience(self, obj):
        return obj.get_audience_display()

    def get_callcenter(self, obj):
        return obj.get_callcenter_display()

    def get_marketing(self, obj):
        return obj.get_marketing_display()

    def get_payment(self, obj):
        return obj.get_payment_display()


class LeadSerializer(serializers.ModelSerializer):
    """Serialize lead's data."""

    brief = LeadBriefSerializer(read_only=True)

    class Meta:
        model = Lead
        fields = ('email', 'name', 'phone', 'message', 'date', 'brief')
        read_only_fields = ('date', 'brief')
        extra_kwargs = {'date': {'format': '%Y-%m-%d %H:%M'}}
