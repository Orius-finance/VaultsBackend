from django.contrib.postgres.fields import ArrayField
from django.db import models

from analytics.models.asset import Asset


# Create your models here.
class Protocol(models.Model):
    name = models.CharField()
    available_assets = ArrayField(models.ForeignKey(Asset, on_delete=models.SET_NULL))
    current_tvl = models.PositiveIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

