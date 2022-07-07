from rest_framework.viewsets import ModelViewSet
from users.api.permissions import AnonCreateAndUpdateOwnerOnly
from .serializers import UserSerializer
from django_filters.rest_framework import DjangoFilterBackend
#from django.contrib.auth.models import User
from users.models import User
from rest_framework_simplejwt.authentication import JWTAuthentication


class UserApiViewSet(ModelViewSet):
    permission_classes = [AnonCreateAndUpdateOwnerOnly]
    serializer_class = UserSerializer
    queryset = User.objects.all()
    authentication_classes = [JWTAuthentication]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['username', ]
