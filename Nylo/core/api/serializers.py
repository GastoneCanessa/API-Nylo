from core.models import *
from rest_framework import serializers

class SellerSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model =Seller
        fields = '__all__'

class AddressSerializzer(serializers.ModelSerializer):
    class Meta:
        model =Address
        fields = '__all__'

class ShopSerializer(serializers.ModelSerializer):

    owner = serializers.StringRelatedField(read_only=True)
    address = AddressSerializzer(read_only=True)
    class Meta:
        model =Shop
        fields = ['id', 'name', 'owner', 'category', 'address']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model =Product
        fields = '__all__'


class Sold_ItemSerializer(serializers.ModelSerializer):

    shop = serializers.StringRelatedField(read_only=True)

    class Meta:
        model =Sold_Item
        fields = '__all__'
