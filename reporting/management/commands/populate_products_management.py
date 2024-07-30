from django.core.management.base import BaseCommand
import random

from reporting.models import Category, Product, Supplier

class Command(BaseCommand):
    help = 'Populates database with products'

    def add_arguments(self, parser):
        parser.add_argument('n', type=int)

    def handle(self, *args, **options):
        
        """
        # Supplier #
        """
        supplier1 = Supplier.objects.get(pk=1)
        supplier2 = Supplier.objects.get(pk=2)
        supplier3 = Supplier.objects.get(pk=3)
        
        """
        # Category #
        """
        category1 = Category.objects.get(pk=1)
        category2 = Category.objects.get(pk=2)
        category4 = Category.objects.get(pk=4)
       
        """
        # Product with supplier and category 1#
        """
        for i in range(options['n']):
            
            supplier = supplier1 
            category = category1 

            product_name = 'Drill' if i == 0 else ('Analog watch' if i == 1 else ('Bicycle' if i == 2 else ('Screwdriver' if i == 3 else 'Scissors')))
            unit_price = 10 if random.randint(0, 1) == 0 else 20
            units_in_stock = 100 if random.randint(0, 1) == 0 else 200
            units_on_order = 15 if random.randint(0, 1) == 0 else 25
           
            product = Product.objects.create( 
                supplier = supplier,
                category =category,
                product_name = product_name,
                unit_price = unit_price,
                units_in_stock = units_in_stock,
                units_on_order = units_on_order
                )
            product.save()
        """
        # Product with supplier and category 2#
        """
        for i in range(options['n']):
            
            supplier = supplier2 
            category = category2 
            product_name = 'Jacket' if i == 0 else ('Shirt' if i == 1 else ('Hat' if i == 2 else ('Trousers' if i == 3 else 'Shoes')))
            unit_price = 10 if random.randint(0, 1) == 0 else 20
            units_in_stock = 100 if random.randint(0, 1) == 0 else 200
            units_on_order = 15 if random.randint(0, 1) == 0 else 25
           
            product = Product.objects.create(
                supplier = supplier,
                category =category,
                product_name = product_name,
                unit_price = unit_price,
                units_in_stock = units_in_stock,
                units_on_order = units_on_order
                )
            product.save()

        """
        # Product with supplier and category 3 & 4#
        """
        for i in range(options['n']):
            
            supplier = supplier3 
            category = category4 

            product_name = 'Gardening book' if i == 0 else ('Computer Book' if i == 1 else ('DIY Book' if i == 2 else ('Geography book' if i == 3 else 'Self help book')))
            unit_price = 10 if random.randint(0, 1) == 0 else 20
            units_in_stock = 100 if random.randint(0, 1) == 0 else 200
            units_on_order = 15 if random.randint(0, 1) == 0 else 25
           
            product = Product.objects.create(
                supplier = supplier,
                category =category,
                product_name = product_name,
                unit_price = unit_price,
                units_in_stock = units_in_stock,
                units_on_order = units_on_order
                )
            product.save()
