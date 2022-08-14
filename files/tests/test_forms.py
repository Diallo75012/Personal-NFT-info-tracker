from django.test import TestCase, SimpleTestCase
from django.test.client import Client
from files.models import *
from files.views import *
from files.urls import *
from files.forms import *



class TestNftInfoForm(TestCase):
    def test_price_not_number(self):
        form = NftInfoForm(data={"price": "e"})

        self.assertEqual(
            form.errors["price"], ["Enter a whole number."]
        )

    def test_title_with_ampersand(self):
        form = NftInfoForm(data={"max_supply": None})

        self.assertEqual(form.errors["max_supply"], ["This field is required."])