from django.db import models

# Create your models here.
class Product(models.Model):
    name  = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=200, decimal_places=2)
    sale_start = models.DateField()
    sale_end = models.DateField()
    
    def is_on_sale(self):
        return False
    def current_price(self):
        return 12.0

class ShoppingCart(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)

class ShoppingCartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    shopping_cart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE)
    quantity = models.IntegerField()