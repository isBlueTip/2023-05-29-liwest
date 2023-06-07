from django.urls import include, path
from rest_framework import routers

from products.views import ProductCategoryViewSet, ProductGroupViewSet, ProductViewSet

app_name = "api"
router = routers.DefaultRouter()
router.register("product-categories", ProductCategoryViewSet, basename="product-categories")
router.register("product-groups", ProductGroupViewSet, basename="product-groups")
router.register("products", ProductViewSet, basename="products")

urlpatterns = [
    path("", include(router.urls)),
]
