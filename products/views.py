from rest_framework import generics

from api.serializers import ProductCategorySerializer, ProductGroupSerializer, ProductSerializer
from products.models import Product, ProductCategory, ProductGroup


class ProductCategoryListCreateView(generics.ListCreateAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer


class ProductGroupListCreateView(generics.ListCreateAPIView):
    queryset = ProductGroup.objects.all()
    serializer_class = ProductGroupSerializer


class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductGroupDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductGroup.objects.all()
    serializer_class = ProductGroupSerializer
