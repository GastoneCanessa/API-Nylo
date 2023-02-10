from rest_framework.views import APIView
from core.api.serializers import *
from core.models import *
from rest_framework.response import Response
from django.db.models import Q
from itertools import chain

class FilterProduct(APIView):
    def get(self, request, rsc):
        # category = get_object_or_404(Category_Product, name = rsc)
        rsc=rsc.split()
        print(rsc)
        pro= []
        for rsc in rsc:

            category = Category_Product.objects.filter(name__icontains = rsc )
            products = Product.objects.filter(Q(name__icontains = rsc) | Q(category__in = category ) | Q(description__icontains = rsc )).distinct()
            pro  = list(chain(pro, products))
            print(pro)

        serializer = ProductSerializer(pro, many=True)
        return Response(serializer.data)
