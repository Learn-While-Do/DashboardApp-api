from rest_framework import serializers
from reporting.models import Category, Customer, Order, Product, Supplier

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ['id', 
                  'customer',
                  'product',
                  'order_date',
                  'required_date',
                  'shipped_name',
                  'shipped_address',
                  'shipped_city',
                  'shipped_postal_code',
                  'shipped_country']
    
    def to_representation(self, instance):
        self.fields['custemer'] = CustomerSerializer(read_only=True)
        self.fields['product'] =  ProductSerializer(read_only=True)
        return super(OrderSerializer, self).to_representation(instance)
        
class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ['id',
                  'first_name',
                  'last_name',
                  'title',
                  'gender',
                  'address',
                  'city',
                  'region',
                  'postal_code',
                  'country',
                  'phone',
                  'email']
        

class SupplierSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Supplier
        fields = ['company_name',
                  'contact_name',
                  'contact_title',
                  'address',
                  'city',
                  'region',
                  'postal_code',
                  'country',
                  'phone',
                  'email',
                  'webpage']
        
class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id',
                  'product_name',
                  'category',
                  'unit_price',
                  'units_in_stock',
                  'units_on_order']
        
    def to_representation(self, instance):
        self.fields['category'] =  CategorySerializer(read_only=True)
        self.fields['supplier'] =  SupplierSerializer(read_only=True)
        return super(ProductSerializer, self).to_representation(instance)
    

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ['id', 
                  'name', 
                  'description']