from django.db import models
from django.conf import settings

class ReferralRelationship(models.Model):
    # who invite 
    employer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='inviter',
        verbose_name="inviter",
        on_delete=models.CASCADE,
    )
    # who connected 
    employee = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='invited',
        verbose_name="invited",
        on_delete=models.CASCADE,
    )
    # referral code
    refer_token = models.ForeignKey(
        "ReferralCode",
        related_name="referral_code",
        verbose_name="referral_code",
        on_delete=models.CASCADE,
    )
    def __str__(self) -> str:
        return f"{self.referrer}_{self.referred}"

class ReferralCode(models.Model):
    token = models.CharField(unique=True, max_length=150)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name="code_master", on_delete=models.CASCADE
    )
    def __str__(self) -> str:
        return f"{self.user}_{self.token}"