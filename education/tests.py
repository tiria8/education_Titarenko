from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from education.models import Module
from users.models import User


class ModuleTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(user_email='test@test.com', password='test')
        self.user_test = User.objects.create(user_email='test1@test.com', password='test')
        self.client.force_authenticate(user=self.user)

        self.module = Module.objects.create(
            title='test_module',
            description='test',
            owner=self.user
        )

    def test_list(self):
        """Test for getting module list"""
        response = self.client.get(
            reverse('education:module-list')
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {'count': 1,
             'next': None,
             'previous': None,
             'results': [
                 {'id': self.module.pk,
                  'title': self.module.title,
                  'description': self.module.description,
                  'owner': self.user.pk
                  }
             ]
             }
        )

    def test_retrieve(self):
        """Test for getting module details"""
        response = self.client.get(
            reverse('education:module-get', kwargs={'pk': self.module.pk})
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {'id': self.module.pk,
             'title': self.module.title,
             'description': self.module.description,
             'owner': self.user.pk
             }
        )

    def test_create(self):
        """Test for creating a module"""
        data = {
            'title': 'test_module',
            'description': 'test',
            'owner': self.user.pk
        }

        response = self.client.post(
            reverse('education:module-create'),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            response.json(),
            {'id': 2,
             'title': 'test_module',
             'description': 'test',
             'owner': self.user.pk
             }

        )

        self.assertEqual(
            str(self.module),
            self.module.title
        )

        self.assertEqual(
            str(self.user),
            self.user.user_email
        )

    def test_update(self):
        """Test for updating the module"""

        data = {
            'title': 'test_module_upd',
            'description': self.module.description,
            'owner': self.user.pk
        }

        response = self.client.patch(
            reverse('education:module-update', kwargs={'pk': self.module.pk}),
            data=data
        )

        print(response.json())

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {'id': self.module.pk,
             'title': 'test_module_upd',
             'description': self.module.description,
             'owner': self.user.pk
             }
        )

    def test_delete(self):
        """Test for deleting the module"""

        response = self.client.delete(
            reverse('education:module-delete', kwargs={'pk': self.module.pk})
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
