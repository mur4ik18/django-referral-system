from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from .models import ReferralCode
from .serializers import RefferCodeSerializer

class RefferCodeJsonListView(ListAPIView):
    def get(self, request):
        # getting querry set with referral codes for user who make request
        queryset = ReferralCode.objects.filter(user=request.user)
        data = RefferCodeSerializer(queryset, many=True)
        return Response(data.data, status=status.HTTP_200_OK)
