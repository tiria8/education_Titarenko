from rest_framework import generics

from education.models import Module
from education.pagination import ListPagination
from education.permissions import IsOwner
from education.serializers import ModuleSerializer


class ModuleCreateAPIView(generics.CreateAPIView):
    """Создание модуля"""
    serializer_class = ModuleSerializer


class ModuleListAPIView(generics.ListAPIView):
    """Просмотр списка модулей"""
    serializer_class = ModuleSerializer
    queryset = Module.objects.all()
    pagination_class = ListPagination


class ModuleRetrieveAPIView(generics.RetrieveAPIView):
    """Просмотр модуля"""
    serializer_class = ModuleSerializer
    queryset = Module.objects.all()


class ModuleUpdateAPIView(generics.UpdateAPIView):
    """Изменение модуля"""
    serializer_class = ModuleSerializer
    queryset = Module.objects.all()
    permission_classes = [IsOwner]


class ModuleDestroyAPIView(generics.DestroyAPIView):
    """Удаление модуля"""
    serializer_class = ModuleSerializer
    queryset = Module.objects.all()
    permission_classes = [IsOwner]
