from rest_framework import generics

from users.models import User
from users.serializers import UserSerializer, AnyUserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    """Создание пользователя"""
    serializer_class = UserSerializer


class UserListAPIView(generics.ListAPIView):
    """Просмотр списка пользователей"""
    serializer_class = AnyUserSerializer
    queryset = User.objects.all()


class UserRetrieveAPIView(generics.RetrieveAPIView):
    """Просмотр пользователя"""
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserUpdateAPIView(generics.UpdateAPIView):
    """Изменение пользователя"""
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDestroyAPIView(generics.DestroyAPIView):
    """Удаление пользователя"""
    serializer_class = UserSerializer
    queryset = User.objects.all()
