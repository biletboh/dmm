from django.urls import reverse
from django.contrib.auth.models import User

from rest_framework.test import APITestCase
from rest_framework import status

from leads.tests.test_models import BriefSetUpMixin, LeadSetUpMixin
from leads.models import Lead


class LeadCRUDTestCase(LeadSetUpMixin, APITestCase):
    """Test suite for the api views."""

    def setUp(self):
        super(LeadCRUDTestCase, self).setUp()
        self.user = User.objects.create_user('test', 'test@dmm.com',
                                             'testpass10')

    def test_create(self):
        """Test the Lead creation endpoint."""

        response = self.client.post(reverse('leads:list_create'),
                                    self.lead_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_comment(self):
        """Test the Lead creation endpoint."""

        self.lead = Lead.objects.create(**self.lead_data)
        data = {'comment': 'Call back later'}
        self.client.force_authenticate(user=self.user)
        response = self.client.put(
                    reverse('leads:comment', kwargs={'pk': self.lead.pk}),
                    data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list(self):
        """Test the Lead list endpoint."""

        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse('leads:list_create'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class BriefCRUDTestCase(BriefSetUpMixin, APITestCase):
    """Test suite for the api views."""

    def setUp(self):
        super(BriefCRUDTestCase, self).setUp()
        self.user = User.objects.create_user('test', 'test@dmm.com',
                                             'testpass10')
        self.brief_data['lead'] = self.lead.email

    def test_create(self):
        """Test the Brief creation endpoint."""

        response = self.client.post(reverse('leads:brief_list_create'),
                                    self.brief_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list(self):
        """Test the Brief list endpoint."""

        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse('leads:brief_list_create'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
