from django.db import models

# Create your models here.
class Vault(models.Model):
    vault_address = models.CharField(max_length=42)
    accountant_address = models.CharField(max_length=42)
