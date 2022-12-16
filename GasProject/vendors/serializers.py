from rest_framework import serializers
from .models import Vendors

class VendorsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Vendors
        fields = [
        'business_name', 'opening_hours', 'closing_hours', 
        'vendor_profile_completed', 'gas_price', 'description'
        ]
        

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data["vendor_profile"] = user                
        vendor = Vendors.objects.create(**validated_data)      
        vendor.save()
        return vendor