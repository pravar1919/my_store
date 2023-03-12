from django.test import SimpleTestCase
from django.urls import reverse, resolve
from retailstores.views import *


class TestUrls(SimpleTestCase):

    def test_store_url(self):
        url = reverse('retailstore:store')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, PostListView)

    def test_mystore_url(self):
        url = reverse('retailstore:my_store', args=['pravar'])
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, UserPostListView)

    def test_mystore_single_url(self):
        url = reverse('retailstore:store_single', args=['1'])
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, PostDetailView)

    def test_addstore_url(self):
        url = reverse('retailstore:add_store')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, PostCreateView)

    def test_update_store_url(self):
        url = reverse('retailstore:store-update', args=['1'])
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, PostUpdateView)
