from rest_framework import serializers

from products.models import Product, ProductCategory, ProductGroup


class ProductCategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=False)
    description = serializers.CharField(required=False)
    seq = serializers.IntegerField(required=False)

    class Meta:
        model = ProductCategory
        fields = ("id", "name", "description", "seq")


class ProductCategoryCreateSerializer(serializers.ModelSerializer):
    description = serializers.CharField(required=False)
    seq = serializers.IntegerField(required=False)

    class Meta:
        model = ProductCategory
        fields = ("id", "name", "description", "seq")


class ProductGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductGroup
        fields = ("id", "category_id", "name", "description", "seq")


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("group", "name", "price", "hidden")
