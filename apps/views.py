from rest_framework.generics import ListAPIView

from apps.models import Category
from apps.serializers import CategorySerializer


class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = None

