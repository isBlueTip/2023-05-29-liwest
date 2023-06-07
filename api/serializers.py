from rest_framework import serializers

from products.models import Product, ProductCategory, ProductGroup


class ProductCategorySerializer(serializers.ModelSerializer):
    description = serializers.CharField(required=False)
    seq = serializers.IntegerField(required=False)

    class Meta:
        model = ProductCategory
        fields = ("id", "name", "description", "seq")


class ProductGroupSerializer(serializers.ModelSerializer):
    description = serializers.CharField(required=False)
    category_name = serializers.StringRelatedField(read_only=True, source="category")
    category_id = serializers.IntegerField(write_only=True, required=True)
    seq = serializers.IntegerField(required=False)

    class Meta:
        model = ProductGroup
        fields = ("id", "category_name", "category_id", "name", "description", "seq")


class ProductSerializer(serializers.ModelSerializer):
    group_name = serializers.StringRelatedField(read_only=True, source="group")
    group_id = serializers.IntegerField(write_only=True, required=True)

    class Meta:
        model = Product
        fields = ("id", "group_name", "group_id", "name", "price", "hidden")
