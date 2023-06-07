from django_filters import rest_framework as filters

from products.models import Product, ProductGroup


class ProductGroupFilter(filters.FilterSet):
    categories_id = filters.NumberFilter(field_name="category_id")

    class Meta:
        model = ProductGroup
        fields = ["categories_id"]
