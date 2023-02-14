from rest_framework.views import APIView
from core.api.serializers import *
from core.models import *
from rest_framework.response import Response
from django.db.models import Q
from itertools import chain
from core.api.utils import distance_filter

class FilterProduct(APIView):
    '''view che permette di filtrare i prodotti in base ala zona e al testo di ricerca,
     cercando corelazioni con il nome la descrizione e le categorie del negozio '''

    def get(self, request):
        filtered_shops = distance_filter(request)
        rsc=request.data["reserch"].split()
        pro= []
        for rsc in rsc:
            category = Category_Product.objects.filter(name__icontains = rsc )
            sold_item_zone = Sold_Item.objects.filter(shop__in = filtered_shops)
            sold_items = sold_item_zone.filter(
                Q(name__name__icontains = rsc) | Q(name__category__in = category ) | Q(name__description__icontains = rsc )
            ).distinct()
            sold  = list(chain(pro, sold_items ))
        serializer = Sold_ItemSerializer(sold, many=True)
        return Response(serializer.data)

class FilterShop(APIView):
    '''view che permette di filtrare i negozzi in base ala zona e al testo di ricerca,
     cercando corelazioni con il nome la descrizione e le categorie del negozio '''

    def get(self, request):
        rsc=request.data["reserch"].split()
        sho= []
        filtered_shops = distance_filter(request)
        for rsc in rsc:
            category = Category_Shop.objects.filter(name__icontains = rsc )
            shops = filtered_shops.filter(
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
