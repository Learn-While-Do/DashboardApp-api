from django.core.management.base import BaseCommand
from datetime import timedelta
from django.utils import timezone
import random

from reporting.models import Order, Customer, Product

class Command(BaseCommand):
    help = 'Populates database with orders'

    def add_arguments(self, parser):
        parser.add_argument('n', type=int)

    def handle(self, *args, **options):
        
        """
        # Customer #
        """
        customer1 = Customer.objects.get(pk=1)
        customer2 = Customer.objects.get(pk=2)
        customer3 = Customer.objects.get(pk=3)
       

        """
        # Product #
        """
        product1 = Product.objects.get(pk=1)
        product2 = Product.objects.get(pk=2)
        product3 = Product.objects.get(pk=3)
       

        """
        # ORDER #
        """
        for i in range(options['n']):
            order_date = timezone.now() + timedelta(days=random.randint(1, 3))
            required_date = timezone.now() + timedelta(days=random.randint(1, 100))
            customer = customer1 if random.randint(0, 2) == 0 else customer2 if random.randint(0, 2)  == 1 else customer3
            product = product1 if random.randint(0, 2) == 0 else product2 if random.randint(0, 2)  == 1 else product3
            shipped_name = 'John Lennon' if random.randint(0, 1) == 0 else ('Paul McCartney' if random.randint(0, 1) == 0 else 'Yoko Ono')
            shipped_address = 'Abbey Road 11' if random.randint(0, 1) == 0 else ('Park Avenue 200' if random.randint(0, 1) == 0 else 'Via Pairoli 33')
            shipped_city = 'New York' if random.randint(0, 1) == 0 else ('London' if random.randint(0, 1) == 0 else 'Rome')
            shipped_postal_code = '11000' if random.randint(0, 1) == 0 else ('44100' if random.randint(0, 1) == 0 else '55220')
            shipped_country = 'USA' if random.randint(0, 1) == 0 else ('UK' if random.randint(0, 1) == 0 else 'Italy')

       
            order = Order.objects.create(
                order_date = order_date, 
                required_date = required_date,
                customer = customer, 
                product = product, 
                shipped_name = shipped_name,
                shipped_address = shipped_address,
                shipped_city = shipped_city,
                shipped_postal_code = shipped_postal_code,
                shipped_country = shipped_country)

            order.save()
           