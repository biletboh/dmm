from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework import status

from leads.tests.test_models import LeadSetUpMixin


class LeadCRUDTestCase(LeadSetUpMixin, APITestCase):
    """Test suite for the api views."""

    def test_create(self):
        """Test the Lead creation endpoint."""

        response = self.client.post(reverse('leads:list_create'),
                                    self.lead_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list(self):
        """Test the Lead creation endpoint."""

        response = self.client.get(reverse('leads:list_create'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
