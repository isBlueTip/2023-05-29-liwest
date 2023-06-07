from django.db.models.deletion import ProtectedError
from django_filters import rest_framework as filters
from rest_framework import generics, mixins, status
from rest_framework.response import Response
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

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        try:
            self.perform_destroy(instance)
        except ProtectedError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_204_NO_CONTENT)


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


class ProductViewSet(
    generics.ListCreateAPIView,
    GenericViewSet,
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
