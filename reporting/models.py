from django.db import models

class Order(models.Model):

    amount = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    created_time = models.DateTimeField()