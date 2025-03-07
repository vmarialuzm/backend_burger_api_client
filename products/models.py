from django.db import models

class Product(models.Model):
    TIPOS = [
        ("desayuno", "Desayuno"),
        ("almuerzo", "Almuerzo"),
        ("cena", "Cena")
    ]

    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    tipo = models.CharField(max_length=10, choices=TIPOS, default="desayuno")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
