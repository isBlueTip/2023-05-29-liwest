from django_filters import rest_framework as filters
from rest_framework import generics, mixins
from rest_framework.viewsets import GenericViewSet

from api.filters import ProductGroupFilter
from api.paginators import CustomPageNumberPagination
from api.serializers import ProductCategorySerializer, ProductGroupSerializer, ProductSerializer
from products.models import Product, ProductCategory, ProductGroup


class ProductCategoryViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet,
):
    queryset = ProductCategory.objects.order_by("seq")
    pagination_class = CustomPageNumberPagination
    serializer_class = ProductCategorySerializer

    def update(self, request, *args, **kwargs):
        kwargs["partial"] = True
        return super().update(request, *args, **kwargs)


class ProductGroupViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet,
):
    queryset = ProductGroup.objects.order_by("seq")
    serializer_class = ProductGroupSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ProductGroupFilter


class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
