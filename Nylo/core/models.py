from django.db import models
from django.contrib.auth.models import User

class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Category_Shop(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Shop(models.Model):
    name = models.CharField(max_length=200, null=True)
    owner = models.OneToOneField(Seller, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ManyToManyField(Category_Shop, null=True, blank=True)

    def __str__(self):
        return self.name


class Category_Product(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=200, null=True)
    description = models.TextField(blank=True, null=True)
    category = models.ManyToManyField(Category_Product)

    def __str__(self):
	    return self.name


class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    description = models.TextField(blank=True, null=True)
    barnd = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True)
    upc = models.PositiveIntegerField(blank=True, null=True)
    sku = models.CharField(max_length=200, blank=True, null=True)
    category = models.ManyToManyField(Category_Product, null=True, blank=True)

    def __str__(self):
        return self.name


class Sold_Item(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name.name
