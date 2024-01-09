from rest_framework import generics

from education.models import Module
from education.pagination import ListPagination
from education.permissions import IsOwner
from education.serializers import ModuleSerializer


class ModuleCreateAPIView(generics.CreateAPIView):
    serializer_class = ModuleSerializer


class ModuleListAPIView(generics.ListAPIView):
    serializer_class = ModuleSerializer
    queryset = Module.objects.all()
    pagination_class = ListPagination


class ModuleRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = ModuleSerializer
    queryset = Module.objects.all()


class ModuleUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ModuleSerializer
    queryset = Module.objects.all()
    permission_classes = [IsOwner]


class ModuleDestroyAPIView(generics.DestroyAPIView):
    serializer_class = ModuleSerializer
    queryset = Module.objects.all()
    permission_classes = [IsOwner]
