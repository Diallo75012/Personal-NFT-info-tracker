from django.test import TestCase, SimpleTestCase
from files.models import *
from files.views import *
from files.urls import *
from django.test.client import Client
from django.urls import reverse


class TestUrls(TestCase):

    def setUp(self):
        self.client = Client()

    def test_nfts_main_urls(self):
        response = self.client.get(reverse('files:nfts'))
        self.assertEqual(response.status_code, 200)