from rest_framework.viewsets import ModelViewSet
from rest_framework import filters

from django_filters.rest_framework import DjangoFilterBackend

from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title','description']


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

    # Основное задание
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['products']
    search_fields = ['products__title', 'products__description']
