from rest_framework import viewsets

from reporting.models import Category, Customer, Order, Product, Supplier
from reporting.serializers import CategorySerializer, CityFilterSerializer, CountryFilterSerializer, CustomerSerializer, OrderSerializer, ProductPriceFilterSerializer, ProductSerializer, SupplierSerializer

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
        
class OrderViewSet(viewsets.ModelViewSet):

    serializer_class = OrderSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ['shipped_country', 'shipped_city']
    search_fields = ['product__product_name', 'customer__last_name']

    def get_queryset(self):
        if(self.request.GET.get('order_by')) == 'order_date':
            return Order.objects.all().order_by('-order_date')
        else:
            return Order.objects.all().order_by('id')
    
class CategoryViewSet(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CustomerViewSet(viewsets.ModelViewSet):

    serializer_class = CustomerSerializer

    def get_queryset(self):
        return Customer.objects.all().order_by('country', 'last_name')
    

class SupplierViewSet(viewsets.ModelViewSet):
    
    serializer_class = SupplierSerializer

    def get_queryset(self):
        return Supplier.objects.all().order_by('country', 'company_name')
    
class ProductViewSet(viewsets.ModelViewSet):
    
    serializer_class = ProductSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ['unit_price', 'supplier__company_name']
    search_fields = ['product_name', 'category__name']

    def get_queryset(self):
        if (self.request.GET.get('order_by')) == 'unit_price':
            return Product.objects.all().order_by('unit_price')
        elif (self.request.GET.get('order_by')) == 'units_in_stock':
            return Product.objects.all().order_by('-units_in_stock')
        elif (self.request.GET.get('order_by')) == 'units_on_order':
            return Product.objects.all().order_by('-units_on_order')
        else:
            return Product.objects.all().order_by('id')

class ProductFilterViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    paginator = None

class CountryFilterViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.values('shipped_country').distinct()
    serializer_class = CountryFilterSerializer
    paginator = None
    
class CityFilterViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.values('shipped_city').distinct()
    serializer_class = CityFilterSerializer
    paginator = None

class SupplierFilterViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    paginator = None

class ProductPriceFilterViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.values('unit_price').distinct()
    serializer_class = ProductPriceFilterSerializer
    paginator = None
