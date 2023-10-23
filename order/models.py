from django.db import models
from django.contrib.auth.models import User
from product.models import Product

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User, related_name="orders", on_delete=models.CASCADE)
    paid_amount = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    phone = models.CharField(max_length=13, blank=True, null=True)
    card_number = models.CharField(max_length=100, blank=True, null=True)
    card_name = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)
    def __str__(self):
        return self.user.username

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="orders", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='orders', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.id