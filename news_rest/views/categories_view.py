from rest_framework import viewsets
from news.models.category_model import Categories
from news_rest.serializers.categories_serializer import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer
