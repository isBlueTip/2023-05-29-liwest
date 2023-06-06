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

    # def __init__(self, instance, data, **kwargs):
    #     kwargs['partial'] = True  # partial update
    #     super().__init__(instance, data, **kwargs)

    class Meta:
        model = ProductGroup
        fields = ("id", "category_name", "category_id", "name", "description", "seq")


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("group", "name", "price", "hidden")
