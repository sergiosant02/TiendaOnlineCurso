from django.db import models
from django.contrib.auth import get_user_model
from shop.models import Product
from django.db.models import F, Sum, FloatField
# Create your models here.

user = get_user_model()

class Order(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.id

    @property
    def total(self):
        self.orderline_set.aggregate(
            total = Sum(F("price") * F("quantity"), output_field=FloatField())
        )["total"]
    
    class Meta:
        db_table = "Pedidos"
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"
        ordering = ['id']
        
class OrderLine(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    product = models.ForeignKey(Product,  on_delete=models.CASCADE)
    order = models.ForeignKey(Order,  on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.id}: {self.quantity} -> {self.product.name}'
    
    class Meta:
        db_table = "Línea de pedidos"
        verbose_name = "Línea de pedido"
        verbose_name_plural = "Líneas de pedidos"
        ordering = ['id']