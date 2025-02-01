import secrets

from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db import models

# Create your models here.

class InviteCode(models.Model):
    code = models.CharField(max_length=16, unique=True, default=lambda: secrets.token_hex(8))
    is_used = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.code} - {'Used' if self.is_used else 'Available'}"

class UserManager(BaseUserManager):
    def create_user(self, wallet_address, invite_code, **extra_fields):
        if not invite_code:
            raise ValueError("Invite code is required for registration")

        try:
            invite = InviteCode.objects.get(code=invite_code, is_used=False)
        except InviteCode.DoesNotExist:
            raise ValueError("Invalid or already used invite code")

        user = self.model(wallet_address=wallet_address, **extra_fields)
        user.save(using=self._db)

        invite.is_used = True
        invite.save()

        return user

class User(AbstractBaseUser):
    wallet_address = models.CharField(max_length=42, unique=True)
    nonce = models.CharField(max_length=255, null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'wallet_address'
