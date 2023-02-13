from geopy.geocoders import  Nominatim
from core.models import *
from django.db.models import Q

def lat_lon(address):
    locator = Nominatim(user_agent="myGeocoder")
    location = locator.geocode(address)
    latitude = location.latitude
    longitude = location.longitude
    return latitude, longitude

def distance_filter(request):
    latitude, longitude = lat_lon(request.data['address'])
    low_latitude = latitude - (0.01 * float(request.data['radius']))
    high_latitude = latitude + (0.01 * float(request.data['radius']))
    low_longitude = longitude - (0.01 * float(request.data['radius']))
    high_longitude = longitude + (0.01 * float(request.data['radius']))
    shops = Shop.objects.filter(Q(latitude__range=(low_latitude, high_latitude)) & Q(longitude__range=(low_longitude, high_longitude)))
    
    return shops
