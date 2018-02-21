from django.urls import reverse
from django.contrib.auth.models import User

from rest_framework.test import APITestCase
from rest_framework import status

from leads.tests.test_models import LeadSetUpMixin


class LeadCRUDTestCase(LeadSetUpMixin, APITestCase):
    """Test suite for the api views."""

    def setUp(self):
        super(LeadCRUDTestCase, self).setUp()
        User.objects.create_user('test', 'test@dmm.com', 'testpass10')

    def test_create(self):
        """Test the Lead creation endpoint."""
        response = self.client.post(reverse('leads:list_create'),
                                    self.lead_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list(self):
        """Test the Lead creation endpoint."""

        self.client.login(username='test', password='testpass10')
        response = self.client.get(reverse('leads:list_create'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
