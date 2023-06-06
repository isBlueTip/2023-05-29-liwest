from rest_framework import generics, mixins, viewsets
from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import GenericViewSet

from api.paginators import CustomPageNumberPagination
from api.serializers import (
    ProductCategoryCreateSerializer,
    ProductCategorySerializer,
    ProductGroupSerializer,
    ProductSerializer,
)
from products.models import Product, ProductCategory, ProductGroup


class ProductCategoryView(
    mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, GenericViewSet
):
    queryset = ProductCategory.objects.order_by("seq")
    pagination_class = CustomPageNumberPagination

    def get_serializer_class(self):
        if self.action == "create":
            return ProductCategoryCreateSerializer
        else:
            return ProductCategorySerializer


class ProductGroupView(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet,
):
    queryset = ProductGroup.objects.all()
    serializer_class = ProductGroupSerializer


class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
