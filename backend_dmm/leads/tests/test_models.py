from django.test import TestCase

from leads.models import Lead, Brief


class SetUpMixin(object):
    """Add intial data to a TestCase."""

    def setUp(self):
        self.lead_data = {
                    'email': 'test@dmm.com',
                    'name': 'Test User',
                    'phone': '+380930112121',
                    'message': 'I want to use dmm!'
                    }
        self.lead = Lead.objects.create(**self.lead_data)


class LeadModelTestCase(SetUpMixin, TestCase):
    """Test the Lead model."""

    def test_str(self):
        """Test a string representation of the model."""

        self.assertEqual(str(self.lead), self.lead_data['email'])


class BriefModelTestCase(SetUpMixin, TestCase):
    """Test the Brief model."""

    def setUp(self):
        super(BriefModelTestCase, self).setUp()
        brief_data = {
            'industry': Brief.INDUSTRIES.forex.value[0],
            'experience': Brief.EXPERIENCE.less_1.value[0],
            'aim': Brief.AIMS.marketing.value[0],
            'stage': Brief.STAGES.beginner.value[0],
            'strategies': Brief.STRATEGIES.considered.value[0],
            'audience': Brief.AUDIENCES.small_international.value[0],
            'callcenter': Brief.CALLCENTERS.own_callcenter.value[0],
            'marketing': Brief.MARKETING.own.value[0],
            'payment': Brief.PAYMENTS.crypto.value[0],
        }
        self.brief = Brief.objects.create(lead=self.lead, **brief_data)

    def test_str(self):
        """Test a string representation of the model."""

        string_repr = f'Brief of {self.lead_data["email"]}'
        self.assertEqual(str(self.brief), string_repr)
