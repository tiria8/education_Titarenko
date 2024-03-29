from django.urls import path, include

from education.apps import EducationConfig
from education.views import ModuleUpdateAPIView, ModuleDestroyAPIView, ModuleRetrieveAPIView, ModuleListAPIView, ModuleCreateAPIView


app_name = EducationConfig.name

urlpatterns = [
    path('module/create/', ModuleCreateAPIView.as_view(), name='module-create'),
    path('module/', ModuleListAPIView.as_view(), name='module-list'),
    path('module/<int:pk>/', ModuleRetrieveAPIView.as_view(), name='module-get'),
    path('module/update/<int:pk>/', ModuleUpdateAPIView.as_view(), name='module-update'),
    path('module/delete/<int:pk>/', ModuleDestroyAPIView.as_view(), name='module-delete'),
]
