from django.urls import reverse
from django.contrib.auth.models import User

from rest_framework.test import APITestCase
from rest_framework import status

from leads.tests.test_models import BriefSetUpMixin, LeadSetUpMixin
from leads.models import Brief


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

    def test_detail(self):
        """Test the Brief detail endpoint."""

        self.client.force_authenticate(user=self.user)
        self.brief_data['lead'] = self.lead
        self.brief = Brief.objects.create(**self.brief_data)
        response = self.client.get(reverse('leads:brief_detail',
                                           kwargs={'pk': self.brief.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
