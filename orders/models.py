from django.db import models
from products.models import Product

class Order(models.Model):
    ESTADOS = [
        ("pendiente", "Pendiente"),
        ("entregado", "Entregado")
    ]
    client = models.CharField(max_length=100)
    status = models.CharField(max_length=10, choices=ESTADOS, default="pendiente")
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


#front me envia
pedidos = {
    "order": [
        # "products": [
        #     {
        #         "qty": 2,
        #         "product": {
        #             "id": 2,
        #             "name": "café americano",
        #             "price": "5.00",
        #             "image": "http://127.0.0.1:8000/media/products/cafe_americano.jpg",
        #             "tipo": "desayuno",
        #             "created_at": "2025-03-07T16:27:40.442440Z",
        #             "updated_at": "2025-03-07T16:27:40.442440Z",
        #             "tipo_display": "Desayuno",
        #         },

        #     }
        # ]

        {
            "id": 1,
            "name": "hamburguesa",
            "price": "10.00",
            "image": "http://127.0.0.1:8000/media/products/hamburguesa.jpg",
            "tipo": "desayuno",
            "created_at": "2025-03-07T16:23:22.222386Z",
            "updated_at": "2025-03-07T16:23:22.223401Z",
            "tipo_display": "Desayuno"
        },
        {
            "id": 4,
            "name": "sandwich jamón y queso",
            "price": "6.00",
            "image": "http://127.0.0.1:8000/media/products/sandwich.jpg",
            "tipo": "desayuno",
            "created_at": "2025-03-07T16:28:29.082652Z",
            "updated_at": "2025-03-08T02:02:55.484485Z",
            "tipo_display": "Desayuno"
        },
        {
            "id": 3,
            "name": "jugo natural",
            "price": "8.00",
            "image": "http://127.0.0.1:8000/media/products/jugo.jpg",
            "tipo": "desayuno",
            "created_at": "2025-03-07T16:28:03.133431Z",
            "updated_at": "2025-03-08T02:04:28.828521Z",
            "tipo_display": "Desayuno"
        },
        {
            "id": 1,
            "name": "hamburguesa",
            "price": "10.00",
            "image": "http://127.0.0.1:8000/media/products/hamburguesa.jpg",
            "tipo": "desayuno",
            "created_at": "2025-03-07T16:23:22.222386Z",
            "updated_at": "2025-03-07T16:23:22.223401Z",
            "tipo_display": "Desayuno"
        },
        {
            "id": 1,
            "name": "hamburguesa",
            "price": "10.00",
            "image": "http://127.0.0.1:8000/media/products/hamburguesa.jpg",
            "tipo": "desayuno",
            "created_at": "2025-03-07T16:23:22.222386Z",
            "updated_at": "2025-03-07T16:23:22.223401Z",
            "tipo_display": "Desayuno"
        },
        {
            "id": 1,
            "name": "hamburguesa",
            "price": "10.00",
            "image": "http://127.0.0.1:8000/media/products/hamburguesa.jpg",
            "tipo": "desayuno",
            "created_at": "2025-03-07T16:23:22.222386Z",
            "updated_at": "2025-03-07T16:23:22.223401Z",
            "tipo_display": "Desayuno"
        }
    ],
    "cliente": "Tuco"
}

#backend hace
#crea una instancia del modelo Order
#order = Order.objects.create(client=pedidos.cliente)

#crear order_detail
#for producto in pedidos.order:

#    order_detail = OrderDetail.objects.create(order=order, producto=producto.id, qty=producto.qty)

