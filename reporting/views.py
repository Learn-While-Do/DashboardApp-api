from rest_framework import viewsets

from reporting.models import Category, Customer, Order, Product, Supplier
from reporting.serializers import CategorySerializer, CustomerSerializer, OrderSerializer, ProductSerializer, SupplierSerializer

        
class OrderViewSet(viewsets.ModelViewSet):

    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.all().order_by('-order_date')
    
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
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer