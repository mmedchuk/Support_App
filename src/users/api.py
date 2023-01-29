from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from users.serializers import UserRegistrationSerializer

User = get_user_model()


class UserCreateAPI(CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]
