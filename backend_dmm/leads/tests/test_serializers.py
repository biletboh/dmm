from django.test import TestCase

from leads.models import Lead
from leads.serializers import LeadSerializer
from leads.tests.test_models import LeadSetUpMixin


class LeadSerializerTestCase(LeadSetUpMixin, TestCase):
    """Test the Lead serializer."""

    def setUp(self):
        super(LeadSerializerTestCase, self).setUp()
        self.serializer_data = {
                    'email': 'testserializer@dmm.com',
                    'name': 'Test Serializer',
                    'phone': '+380930112121',
                    'message': 'I want to test serializer!'
                    }
        self.lead = Lead.objects.create(**self.lead_data)
        self.serializer = LeadSerializer(instance=self.lead)

    def test_fields(self):
        """Test ."""

        data = self.serializer.data
        keys = ['id', 'email', 'name', 'phone', 'message',
                'date', 'comment', 'brief', 'messages']
        self.assertCountEqual(data.keys(), keys)
