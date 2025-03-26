from django.db import models
from products.models import Product

class Order(models.Model):
    ESTADOS = [
        ("pending", "Pendiente"),
        ("in_preparation", "En preparación"),
        ("ready", "Listo para entregar"),
        ("cancelled", "Cancelado")
    ]
    client = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=ESTADOS, default="pending")
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Orden {self.id} - {self.client}"
    
class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="details")
    producto = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="order_details")
    qty = models.PositiveIntegerField(default=1)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.qty} x {self.producto.name}"
    
    def save(self, *args, **kwargs):
        self.subtotal = self.qty * self.producto.price
        super().save(*args, **kwargs)
