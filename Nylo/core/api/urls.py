from django.urls import include, path
from rest_framework.routers import DefaultRouter
from core.api.views import *
from core.api.filters import *

router = DefaultRouter()
router.register(r"sellers", SellerViewSet)
router.register(r"shops", ShopViewSet)
router.register(r"products", ProductViewSet)
router.register(r"sold_items", Sold_ItemViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path('filter/products/<str:rsc>', FilterProduct.as_view(), name="filter_products" ),
    path('filter/shops/<str:rsc>', FilterShop.as_view(), name="filter_shops" ),
]
