from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet, OrderDetailViewSet

router = DefaultRouter()
router.register(r'orders', OrderViewSet)
router.register(r'orderdetails', OrderDetailViewSet)

urlpatterns = [
    path('', include(router.urls)),
]