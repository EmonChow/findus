from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from django.db.models import Q
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from drf_spectacular.utils import OpenApiParameter, extend_schema
from authentication.decorators import IsAdminUser, has_permissions
from authentication.models import Permission
from authentication.serializers import (
    AdminUserSerializer,
    PasswordChangeSerializer,
    AdminUserListSerializer,

)



# Create your views here.
User = get_user_model()





class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        user = self.user

        serializer = AdminUserListSerializer(
                self.user
            ).data  

        # Add serialized user data to the token response
        for k, v in serializer.items():
            data[k] = v

        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer



