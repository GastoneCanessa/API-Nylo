from core.api.serializers import *
from core.models import *
from rest_framework import generics, mixins
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from core.api.permissions import *
from rest_framework.exceptions import ValidationError

class SellerViewSet( mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):

    queryset = Seller.objects.all()
    serializer_class = SellerSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        user = self.request.user
        review_queryset = Seller.objects.filter(user=user)
        if review_queryset.exists():
            raise ValidationError("Hai gia creato un venditore!")
        serializer.save( user=user)

class ShopViewSet(mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):

    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    permission_classes = [IsAuthorOrReadOnly, IsAuthenticated]


class ProductViewSet(mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class Sold_ItemViewSet(mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):


    queryset = Sold_Item.objects.all()
    serializer_class = Sold_ItemSerializer
    permission_classes = [IsAuthenticated]
