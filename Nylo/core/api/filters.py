from rest_framework.views import APIView
from core.api.serializers import *
from core.models import *
from rest_framework.response import Response
from django.db.models import Q
from itertools import chain

class FilterProduct(APIView):
    def get(self, request, rsc):
        rsc=rsc.split()
        pro= []
        for rsc in rsc:
            category = Category_Product.objects.filter(name__icontains = rsc )
            products = Product.objects.filter(
                Q(name__icontains = rsc) | Q(category__in = category ) | Q(description__icontains = rsc )
            ).distinct()
            pro  = list(chain(pro, products))
        serializer = ProductSerializer(pro, many=True)
        return Response(serializer.data)

class FilterShop(APIView):
    def get(self, request, rsc):
        rsc=rsc.split()
        sho= []
        for rsc in rsc:
            category = Category_Shop.objects.filter(name__icontains = rsc )
            shops = Shop.objects.filter(
                Q(name__icontains = rsc) | Q(category__in = category )
            ).distinct()
            sho  = list(chain(sho, shops))

            """
             (per evitare di non avere riscontri quando si compiono errori di battitura tipo ggiardino)??
             provare ad estrarre tutti i valori come {nome, categoria} poi ciclarli
             e testare se sono all'interno delle parole della lista di ricerca, se ci sono
             dei riscontri inserili in una lista gli id dei riscontri per poi creare una query da serializzare
            """
            # print(bool(sho))
            # if not sho :
            #     qry = Shop.objects.values('name')
            #     print(qry)

        serializer = ShopSerializer(sho, many=True)
        return Response(serializer.data)

class FilterZone(APIView):
    pass
    
