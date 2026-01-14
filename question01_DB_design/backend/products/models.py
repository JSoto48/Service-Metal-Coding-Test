from django.db import models


class BaseProduct(models.Model):
    """Base product fields shared by all products"""
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sku = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    # in_stock = models.BooleanField(default=True)  maybe int for count of products in stock?
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        abstract = True

    

    
