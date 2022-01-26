import secrets
from rest_framework import serializers
from .models import ReferralCode, ReferralRelationship

class ReferralSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReferralRelationship
        fields = [
            "employer",
            "employee", 
            "refer_token"]

class RefferCodeSerializer(serializers.ModelSerializer):
    referral_code = ReferralSerializer(many=True, default="")
    class Meta:
        model = ReferralCode
        fields = [
            "token", 
            "user", 
            "referral_code"]
        