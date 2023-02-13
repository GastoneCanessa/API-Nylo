from core.models import *
from rest_framework import serializers

class SellerSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model =Seller
        fields = '__all__'

class ShopSerializer(serializers.ModelSerializer):

    owner = serializers.StringRelatedField(read_only=True)
    latitude = serializers.StringRelatedField(read_only=True)
    longitude = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model =Shop
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model =Product
        fields = '__all__'


class Sold_ItemSerializer(serializers.ModelSerializer):

    shop = serializers.StringRelatedField(read_only=True)

    class Meta:
        model =Sold_Item
        fields = '__all__'
