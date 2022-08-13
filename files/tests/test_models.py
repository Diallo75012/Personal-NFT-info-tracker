from functools import total_ordering
from django.test import TestCase, SimpleTestCase
from django.db.models import *
from files.models import *
from files.views import *
from files.urls import *
import unittest
import datetime



class TestModelsAnimal(TestCase):
    # the setUp function is used to create an object and not have to repeat this several time, so we can all our
    # future tests using that same object
    def setUp(self):
        self.FictifNFT = NftRegistration.objects.create(
        collection ="Test Collection",
        price = 100,
        max_supply = 2000,
        nbr_minted = 300,
        nbr_of_holders = 279,
        total_number_of_followers = 679
        )

    def test_nbr_minted_300(self):
        self.assertEquals(self.FictifNFT.nbr_minted, 300 )
        self.assertTrue(isinstance(self.FictifNFT, NftRegistration))
        self.assertEqual(self.FictifNFT.collection, "Test Collection")