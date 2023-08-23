from rest_framework import serializers
from news.models.category_model import Categories


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = "__all__"
