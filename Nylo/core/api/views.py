from core.api.serializers import *
from core.models import *
from rest_framework import generics, mixins
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from core.api.permissions import *
from rest_framework.exceptions import ValidationError
from django.shortcuts import get_object_or_404

class SellerViewSet( mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):

    queryset = Seller.objects.all()
    serializer_class = SellerSerializer
    permission_classes = [IsAuthor, IsAdminUser]

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

    def perform_create(self, serializer):
        owner = get_object_or_404(Seller, user = self.request.user)
        review_queryset = Shop.objects.filter(owner=owner)
        if review_queryset.exists():
            raise ValidationError("Hai gia creato un negozio!")
        serializer.save( owner=owner)


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
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        owner = get_object_or_404(Seller, user = self.request.user)
        shop = get_object_or_404(Shop, owner = owner)
        # review_queryset = Shop.objects.filter(owner=owner)
        # if review_queryset.exists():
        #     raise ValidationError("Hai gia creato un negozio!")
        serializer.save( shop=shop)
