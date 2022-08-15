from pyexpat import model
from  rest_framework import serializers
from .models import GasOrder

class GasOrderSerializer(serializers.HyperlinkedModelSerializer):
    customer = serializers.ReadOnlyField(source = 'customer.username')
    
    class Meta:
        model = GasOrder
        fields = ['customer', 'order_price', 'date_created', 'status',
            'total_KG', 'date_canceled', 'date_delivered'
        ]