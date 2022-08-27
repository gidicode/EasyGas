from asyncore import write
import email
from pyexpat import model
from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

class UsersSerializers(serializers.HyperlinkedModelSerializer):    

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'state', 'lga', 'phoneNumber', 
            'Address', 'favourite_vendors', 'profile_picture', 'reg_complete',
        ]

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)
        token['username'] = user.username
        return token


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators = [UniqueValidator(queryset = User.objects.all())]
    )
    username = serializers.CharField(
        required=True,
        validators = [UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', )

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password field didin't match."})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'],
            email=validated_data['email'],            
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class CompleteRegistration(serializers.ModelSerializer):
    state = serializers.CharField(required = True)
    lga = serializers.CharField(required = True)
    Address = serializers.CharField(required = True)
    phoneNumber = serializers.CharField(required = True)    
    class Meta:
        model = User
        fields = ('state', 'lga', 'Address', 'phoneNumber', 'reg_complete')

    def create(self, validated_data):
        id = validated_data['id']
        user = User.objects.filter(pk = id).update(
            state = validated_data['state'],
            lga = validated_data['lga'],
            Address = validated_data['Address'],
            phoneNumber = validated_data['phoneNumber'],
            reg_complete = validated_data['reg_complete']
        )
        user.save()
        return user