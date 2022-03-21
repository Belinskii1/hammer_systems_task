from rest_framework.decorators import api_view
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.response import Response
from rest_framework import filters, generics, status, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.shortcuts import get_object_or_404
from django.contrib.auth.tokens import default_token_generator

from .serializers import UserSerializer, TokenSerializer
from api.models import ActivationCode, User
from .exseptions import CodeDoesNotExist


@api_view(['POST'])
@permission_classes([AllowAny])
def get_confirmation_code(request):
    """API создает пользователя и отправляет код подверждения=токен"""
    serializer = UserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    username = serializer.data.get('username')
    user, created = User.objects.get_or_create(telephone_number=username)
    if not created:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    code = ActivationCode.objects.create(user=user)
    return Response({'Ваш код активации': str(code.code)}, status=status.HTTP_200_OK)


@api_view(['POST', 'DELETE'])
@permission_classes([AllowAny])
def check_activation_code(request):
    serializer = TokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    code = get_object_or_404(
        ActivationCode,
        code=serializer.data.get('code')
    )
    if not code:
        return Response("код не существует")
    user = code.user
    code.delete()
    token = default_token_generator.make_token(user)
    return Response({'Ваш токен': str(token)}, status=status.HTTP_200_OK)
