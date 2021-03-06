from django.urls import reverse
from django.contrib.auth.models import User

from rest_framework.test import APITestCase
from rest_framework import status

from leads.models import Lead, Brief
from leads.serializers import LeadSerializer
from leads.tests.test_models import BriefSetUpMixin, LeadSetUpMixin


class LeadCRUDTestCase(LeadSetUpMixin, APITestCase):
    """Test suite for the api views."""

    def setUp(self):
        super(LeadCRUDTestCase, self).setUp()
        self.user = User.objects.create_user('test', 'test@dmm.com',
                                             'testpass10')
        self.lead_invalid_data = {
            'email': 'invalid.email.com',
            'name': '',
            'phone': '212121212121',
            'message': 'invalid data'
        }

    def test_create(self):
        """Test the Lead creation endpoint."""

        response = self.client.post(reverse('leads:list_create'),
                                    self.lead_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_invalid_data(self):
        """Test the Lead creation endpoint with invalid data."""

        response = self.client.post(reverse('leads:list_create'),
                                    self.lead_invalid_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_comment(self):
        """Test the Comment update endpoint."""

        self.lead = Lead.objects.create(**self.lead_data)
        data = {'comment': 'Call back later'}
        self.client.force_authenticate(user=self.user)
        response = self.client.put(
                    reverse('leads:comment', kwargs={'pk': self.lead.pk}),
                    data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_comment(self):
        """Test the Comment update endpoint with invalid data."""

        self.lead = Lead.objects.create(**self.lead_data)
        data = {'invalid_comment': 123}
        self.client.force_authenticate(user=self.user)
        response = self.client.put(
                    reverse('leads:comment', kwargs={'pk': self.lead.pk}),
                    data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_list(self):
        """Test the Lead list endpoint."""

        Lead.objects.create(**self.lead_data)
        Lead.objects.create(email='test2@dmm.solutions', name='Test2',
                            phone='+380931212121', message='hello')
        Lead.objects.create(email='test3@dmm.solutions', name='Test3',
                            phone='+380931212121', message='hello')
        leads = Lead.objects.all()
        serializer = LeadSerializer(leads, many=True)

        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse('leads:list_create'))
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class BriefCRUDTestCase(BriefSetUpMixin, APITestCase):
    """Test suite for the api views."""

    def setUp(self):
        super(BriefCRUDTestCase, self).setUp()
        self.user = User.objects.create_user('test', 'test@dmm.com',
                                             'testpass10')
        self.brief_data['lead'] = self.lead.email
        self.brief_invalid_data = {
            'industry': 'no industry',
            'experience': Brief.EXPERIENCE.less_1.value[0],
            'aim': Brief.AIMS.marketing.value[0],
            'stage': Brief.STAGES.beginner.value[0],
            'strategies': Brief.STRATEGIES.considered.value[0],
            'audience': Brief.AUDIENCES.small_international.value[0],
            'callcenter': Brief.CALLCENTERS.own_callcenter.value[0],
            'marketing': Brief.MARKETING.own.value[0],
            'payment': Brief.PAYMENTS.crypto.value[0],
            'lead': 'invalid_lead'
        }

    def test_create(self):
        """Test the Brief creation endpoint."""

        response = self.client.post(reverse('leads:brief_list_create'),
                                    self.brief_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_invalid_data(self):
        """Test the Brief creation endpoint with invalid data."""

        response = self.client.post(reverse('leads:list_create'),
                                    self.brief_invalid_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_list(self):
        """Test the Brief list endpoint."""

        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse('leads:brief_list_create'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
