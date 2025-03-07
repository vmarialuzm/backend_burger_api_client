from .models import Product
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        extra_kwargs = {
            'tipo': {'required': True},
        }

    def to_representation(self, instance):
        representation =  super().to_representation(instance)
        representation['tipo_display'] = instance.get_tipo_display()
        return representation