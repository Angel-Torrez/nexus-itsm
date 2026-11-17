from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from .serializers import UserRegisterSerializer, UserSerializer

User = get_user_model()


class RegisterView(generics.CreateAPIView):
    """Register a new user account."""

    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserRegisterSerializer


class UserDetailView(generics.RetrieveAPIView):
    """Return the authenticated user details."""

    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user