
from shops.models import Products, Shops
from shops.serializers import ProductSerializer, ShopSerializer

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

LIMIT_PRODUCT_BY_SHOP = 5
LIMIT_RADIUS = 5


@api_view(['GET', 'POST'])
def search_shops_near(request, format=None):
    """List all code items, or create a new item."""
    if request.method == 'GET':
        limit_product = int(request.query_params['limit']) if 'limit' in request.query_params else LIMIT_PRODUCT_BY_SHOP
        radius = float(request.query_params['radius']) if 'radius' in request.query_params else LIMIT_RADIUS
        lat = float(request.query_params['lat']) if 'lat' in request.query_params else None
        lng = float(request.query_params['lng']) if 'lng' in request.query_params else None
        if not lat or not lng:
            return Response('Lat or lng not provided', status=status.HTTP_400_BAD_REQUEST)
        shops = Shops.objects.filter(lat__range=(lat - (radius / 100), lat + (radius / 100)), lng__range=(lng - (radius / 100), lng + (radius / 100)))

        shops_id = shops.values_list('id')
        products = Products.objects.filter(shop_id__in=shops_id).order_by('-popularity')[0:limit_product]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def search_shops_name(request, pk, format=None):
    """Retrieve, update or delete a code item."""
    try:
        shops = Shops.objects.filter(name__icontains=pk)
    except Shops.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ShopSerializer(shops, many=True)
        return Response(serializer.data)
