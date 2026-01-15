from django.db import models


class Product(models.Model):
    """
    Main product fields shared by all products
    Example product given: https://www.pvcfittingsonline.com/collections/pvc-gate-valves/products/2-pvc-socket-gate-valve-spears-2022-020
    """
    name = models.CharField(max_length=500)
    sku = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    main_category = models.CharField(max_length=100)            # Example: "Valves"
    subcategory = models.CharField(max_length=100)              # Example: "PVC Gate Valves"

    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)            # So we can tell when the stock/product was updated last


    
class ProductImage(models.Model):
    """Supports multiple images per product"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    is_primary = models.BooleanField(default=False)     # Explicitly set primary/thumbnail image
    display_order = models.IntegerField(default=0)      # Extendable for multiple images per product
    alt_text = models.CharField(max_length=200)         # For screen readers, SEO, and fallback

    image_url = models.URLField()                       # In a real backend system we would probably do models.ImageField with validators=[]

    class Meta:
        ordering = ['display_order']



class ProductSpecs(models.Model):
    """
    One product may have many specifications.\n
    Flexible key-value pairs to handle different product types.\n
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='specs')
    spec_name = models.CharField(max_length=100)        # Example: Max Pressure
    spec_value = models.CharField(max_length=300)       # Example: 200 PSI @ 73F

    def __str__(self):
        return f"{self.spec_name}: {self.spec_value}"   # Returns in the format - Max Pressure: 200 PSI @ 73F
    

