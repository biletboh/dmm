from django.test import TestCase

from leads.models import Lead, Brief


class LeadSetUpMixin(object):
    """Add intial data to a TestCase."""

    def setUp(self):
        self.lead_data = {
                    'email': 'test@dmm.com',
                    'name': 'Test User',
                    'phone': '+380930112121',
                    'message': 'I want to use dmm!'
                    }


class LeadModelTestCase(LeadSetUpMixin, TestCase):
    """Test the Lead model."""

    def test_can_create(self):
        """Test the bucketlist model can create a bucketlist."""

        old_count = Lead.objects.count()
        Lead.objects.create(**self.lead_data)
        new_count = Lead.objects.count()
        self.assertNotEqual(old_count, new_count)

    def test_str(self):
        """Test a string representation of the model."""

        lead = Lead.objects.create(**self.lead_data)
        self.assertEqual(str(lead), self.lead_data['email'])


class BriefModelTestCase(LeadSetUpMixin, TestCase):
    """Test the Brief model."""

    def setUp(self):
        super(BriefModelTestCase, self).setUp()
        self.brief_data = {
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
        self.lead = Lead.objects.create(**self.lead_data)

    def test_can_create(self):
        """Test the bucketlist model can create a bucketlist."""

        old_count = Brief.objects.count()
        Brief.objects.create(lead=self.lead, **self.brief_data)
        new_count = Brief.objects.count()
        self.assertNotEqual(old_count, new_count)

    def test_str(self):
        """Test a string representation of the model."""

        string_repr = f'Brief of {self.lead_data["email"]}'
        brief = Brief.objects.create(lead=self.lead, **self.brief_data)
        self.assertEqual(str(brief), string_repr)
