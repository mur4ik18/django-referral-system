from referral_system.models import ReferralRelationship, ReferralCode
import secrets
from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, referral_token=None):
        # checking if user add all fields
        if not referral_token:
            raise ValueError("Please use your token!")
        if not email:
            raise ValueError("Users must have an email address!")
        # getting referral code and if code is not exist return error
        ref_code = ReferralCode.objects.filter(token=referral_token)
        if not ref_code:
            raise ValueError("Your token is not valid!")

        print(ref_code[0].user)

        # check code before using
        usages_token = ReferralRelationship.objects.filter(refer_token=ref_code[0])
        if not usages_token:
            # create user
            user = self.model(
                username=username, email=self.normalize_email(email), referral_token=referral_token
            )
            user.set_password(password)
            user.save(using=self._db)
            # create relationship for inviter and invited persone
            ReferralRelationship(
                employer=ref_code[0].user, employee=user, refer_token=ref_code[0]
            ).save()
            # create for new user 3 referall code (for frends)
            for i in range(3):
                self.create_reftoken(user)

        else:
            raise ValueError("This token is used!")

        return user

    def create_superuser(self, username, email, password=None, referral_token=None):
        # admin can use defunct referral code
        user = self.model(username=username, email=email, referral_token=referral_token)
        # set password and andmin things
        user.set_password(password)
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        # create 5 referral codes
        for i in range(5):
            self.create_reftoken(user)
        return user

    # method for creating tokens
    def create_reftoken(self, user):
        token = secrets.token_urlsafe(20)
        ReferralCode(token=token, user=user).save()