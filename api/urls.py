from django.urls import path

from products.views import (
    ProductCategoryListCreateView,
    ProductGroupDetailView,
    ProductGroupListCreateView,
    ProductListCreateView,
)

app_name = "api"

urlpatterns = [
    path("product-categories/", ProductCategoryListCreateView.as_view(), name="product-category-list"),
    path("product-groups/", ProductGroupListCreateView.as_view(), name="product-group-list"),
    path("product-groups/<uuid:pk>/", ProductGroupDetailView.as_view(), name="product-group-detail"),
    path("products/", ProductListCreateView.as_view(), name="product-list"),
]
