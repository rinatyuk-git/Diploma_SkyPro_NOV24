from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status

from content.models import Document
from users.models import User


class DocumentTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="test@test.test")
        self.moduser = User.objects.create(email="moderator@test.test", is_staff=True)
        self.doc = Document.objects.create(
            name="Test1_Doc1",
            owner=self.user,
        )
        # mock patch
        self.client.force_authenticate(user=self.user)

    def test_document_create(self):
        url = reverse('content:doc_upload')
        data = {
            "owner": self.user.pk,
            "name": "Test1_Doc1",
        }
        # email = {"email": "moderator@test.test"}
        response = self.client.post(url, data)
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )
        self.assertEqual(
            Document.objects.all().count(), 2
        )

    def test_document_list(self):
        url = reverse('content:docs_list')
        response = self.client.get(url)
        data = response.json()
        result = {
            'count': 1,
            'next': None,
            'previous': None,
            'results': [
                {
                    "id": self.doc.pk,
                    "status": None,
                    "name": "Test1_Doc1",
                    "owner": self.user.pk,
                }
            ]
        }
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data, result
        )

    def test_document_retrieve(self):
        url = reverse('content:doc_detail', args=(self.doc.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('name'), self.doc.name
        )
