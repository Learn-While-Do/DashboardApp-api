from django.db import models

GENDER = (
    ('Masculine', 'Masculine'),
    ('Feminine', 'Feminine'),
    ('Prefer not to say', 'Prefer not to say'),
)

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)

class Supplier(models.Model):
    company_name = models.CharField(max_length=50)
    contact_name = models.CharField(max_length=50)
    contact_title = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    region = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=50)
    country = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    webpage = models.CharField(max_length=50)

class Customer(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50, choices=GENDER, default='Prefer not to say')
    title = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

class Product(models.Model):
    product_name = models.CharField(max_length=50)
    unit_price = models.IntegerField()
    units_in_stock = models.IntegerField()
    units_on_order = models.IntegerField()
    supplier = models.ForeignKey(Supplier, on_delete=models.DO_NOTHING, null=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)

    class Meta:
        ordering = ['category', 'unit_price']

class Order(models.Model):

    order_date = models.DateTimeField()
    required_date = models.DateTimeField()
    shipped_city = models.CharField(max_length=100)
    shipped_name = models.CharField(max_length=100)
    shipped_address = models.CharField(max_length=100)
    shipped_postal_code = models.CharField(max_length=100)
    shipped_country = models.CharField(max_length=100)
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)

