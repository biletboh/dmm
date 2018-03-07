from rest_framework import serializers

from .models import Brief, Lead, Message


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


class MessagesSerializer(serializers.ModelSerializer):
    """Serialize lead's data."""

    class Meta:
        model = Message
        fields = ('id', 'name', 'phone', 'message', 'date')
        extra_kwargs = {
                    'date': {'format': '%Y-%m-%d %H:%M'},
                    }


class LeadSerializer(serializers.ModelSerializer):
    """Serialize lead's data."""

    brief = LeadBriefSerializer(read_only=True)
    messages = MessagesSerializer(many=True, read_only=True)

    class Meta:
        model = Lead
        fields = ('id', 'email', 'name', 'phone', 'message', 'date', 'comment',
                  'brief', 'messages')
        read_only_fields = ('id', 'date', 'comment', 'brief', 'messages')
        extra_kwargs = {
                    'date': {'format': '%Y-%m-%d %H:%M'},
                    'email': {'validators': []},
                    }
        depth = 1

    def validate(self, data):
        """Check if lead's email exists."""

        if Lead.objects.filter(email=data['email']).exists():
            lead = Lead.objects.get(email=data['email'])
            Message.objects.create(
                        lead=lead, name=data['name'],
                        phone=data['phone'], message=data['message'])
            msg = (data['email'] + ' already exists. '
                   + 'Added a new message from the lead.')
            raise serializers.ValidationError({'New message': msg})
        return data


class CommentSerializer(serializers.ModelSerializer):
    """Serialize lead's comment."""

    class Meta:
        model = Lead
        fields = ('comment',)
        extra_kwargs = {
                    'comment': {'required': True},
                    }
