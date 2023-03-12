from django.test import TestCase, Client
from django.urls import reverse
from retailstores.models import *
from django.contrib.auth.models import User
import json


class TestViews(TestCase):

    def test_store_list(self):
        client = Client()

        response = client.get(reverse('retailstore:store'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'retailstores/store_detail.html')

    # def test_store_detail_list(self):
    #     self.user = User.objects.create(
    #         username='admin', email='pra@gmail.com', password='Demo@1234')
    #     client = Client()

    #     response = client.get(
    #         reverse('retailstore:store_single', args=[23]))
    #     Store.objects.create(
    #         user=self.user,
    #         name='store11',
    #         description='My store',
    #         categories='Grocery',
    #     )
    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'retailstores/store_single.html')
