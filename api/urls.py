from django.urls import include, path
from rest_framework import routers

from products.views import ProductCategoryView, ProductGroupView  # ProductGroupDetailView,; ProductGroupListCreateView,

app_name = "api"
router = routers.DefaultRouter()
router.register("product-categories", ProductCategoryView, basename="product-categories")
router.register("product-groups", ProductGroupView, basename="product-groups")

urlpatterns = [
    path("", include(router.urls)),
    # path("product-categories/", ProductCategoryListCreateView.as_view(), name="product-category-list"),
    # path("product-categories/<int:pk>/", ProductCategoryListCreateView.as_view(), name="product-category-detail"),
    # path("product-groups/", ProductGroupListCreateView.as_view(), name="product-group-list"),
    # path("product-groups/<uuid:pk>/", ProductGroupDetailView.as_view(), name="product-group-detail"),
    # path("products/", ProductListCreateView.as_view(), name="product-list"),
]
