from django.db import models

# Create your models here.


class Product (models.Model):
    product_name = models.CharField(max_lenght=20)
    price = models.IntegerField()
    sprice = models.IntegerField()