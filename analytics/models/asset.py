from django.db import models


class Asset(models.Model):
    name = models.CharField()
    symbol = models.CharField()
    decimals = models.PositiveSmallIntegerField()
    erc20_address = models.CharField()
    chain_id = models.PositiveIntegerField()
