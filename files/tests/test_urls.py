from django.test import TestCase, SimpleTestCase
from files.models import *
from files.views import *
from files.urls import *
from django.test.client import Client
from django.urls import reverse


class TestUrls(TestCase):

    def setUp(self):
        self.client = Client()

        self.FictifNFT = NftRegistration.objects.create(
        collection ="Test Collection",
        price = 100,
        max_supply = 2000,
        nbr_minted = 300,
        nbr_of_holders = 279,
        total_number_of_followers = 679
        )

    def test_nfts_main_urls(self):
        response = self.client.get(reverse('files:nfts'))
        self.assertEqual(response.status_code, 200)

    def test_nfts_update_url(self):
        response = self.client.get(reverse('files:nfts_update', args=[self.FictifNFT.id]))
        self.assertEqual(response.status_code, 200)
