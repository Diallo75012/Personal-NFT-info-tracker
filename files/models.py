import collections
from django.db import models

# Create your models here.
class NftRegistration(models.Model):
    collection = models.CharField(max_length=50)
    price = models.IntegerField()
    max_supply = models.IntegerField()
    nbr_minted = models.IntegerField()
    nbr_of_holders = models.IntegerField()
    total_number_of_followers = models.IntegerField()


