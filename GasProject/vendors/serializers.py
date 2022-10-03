from rest_framework import serializers
from .models import Vendors

class VendorsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Vendors
        fields = '__all__'

    def create(self, validated_data):
        user = self.context['request'].user
        vendor = Vendors.objects.create(**validated_data)
        vendor.save(vendor_profile = user)
        return vendor