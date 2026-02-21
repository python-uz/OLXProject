from rest_framework.serializers import ModelSerializer
from rest_framework_recursive.fields import RecursiveField
from apps.models import Category


class CategorySerializer(ModelSerializer):
    children = RecursiveField(many=True, required=False)

    class Meta:
        model = Category
        fields = ('id', 'name', 'children', 'attribute')


