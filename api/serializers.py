from rest_framework import serializers

from products.models import Product, ProductCategory, ProductGroup


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ("name", "description", "seq")


class ProductGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductGroup
        fields = ("category", "name", "description", "seq")


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("group", "name", "price", "hidden")
