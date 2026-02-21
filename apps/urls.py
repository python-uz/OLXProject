from django.urls import path, include

from apps.views import CategoryListAPIView

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('categories/', CategoryListAPIView.as_view()),
]