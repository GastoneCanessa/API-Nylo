from django.urls import include, path
from rest_framework.routers import DefaultRouter
from core.api.views import *
router = DefaultRouter()
router.register(r"sellers", SellerViewSet)
router.register(r"shops", ShopViewSet)
router.register(r"products", ProductViewSet)
router.register(r"sold_items", Sold_ItemViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
