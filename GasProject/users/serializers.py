from rest_framework import serializers
from .models import User

class UsersSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'state', 'lga', 'phoneNumber', 
            'Address', 'favourite_vendors', 'profile_picture'
        ]