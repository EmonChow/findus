from django.core.exceptions import ObjectDoesNotExist

from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from authentication.models import Role
from authentication.serializers import RoleSerializer, RoleListSerializer
from authentication.filters import RoleFilter

from drf_spectacular.utils import  extend_schema, OpenApiParameter
from commons.pagination import Pagination


@extend_schema(request=RoleSerializer, responses=RoleSerializer)
@api_view(['GET'])
def home_view(request, pk):
	pass