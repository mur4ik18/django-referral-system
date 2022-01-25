from django.contrib import admin
from .models import ReferralRelationship, ReferralCode

admin.site.register(ReferralRelationship)
admin.site.register(ReferralCode)