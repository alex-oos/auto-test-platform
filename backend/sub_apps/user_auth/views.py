from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import MyTokenObtainPairSerializer

from utils.customized_drf import BaseViewSet
from .models import UserProfile
from .serializers import UserProfileSerializer


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class UserProfileViewSet(BaseViewSet):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all().order_by('id')
