from django.contrib.auth import logout
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import MyTokenObtainPairSerializer

from utils.customized_drf import BaseViewSet, JsonResponse
from .models import UserProfile
from .serializers import UserProfileSerializer


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class LogoutAPIView(APIView):
    def post(self, request):
        logout(request)
        return JsonResponse(data={'message': 'logout success!', }, status=200)


class UserProfileViewSet(BaseViewSet):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all().order_by('id')
