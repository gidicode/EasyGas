from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

class UsersSerializers(serializers.HyperlinkedModelSerializer):    

    class Meta:
        model = User
        fields = ['username', 'email', 'state', 'lga', 'phoneNumber', 
            'Address', 'favourite_vendors', 'profile_picture', 'reg_complete', 'vendor'
        ]
        read_only_fields = ['username', 'email', 'reg_complete', 'vendor' ]

    def update(self, instance, validated_data):        
        instance.state = validated_data.get('state', instance.state)
        instance.lga = validated_data.get('lga', instance.lga)
        instance.Address = validated_data.get('Address', instance.Address)
        instance.phoneNumber = validated_data.get('phonenUmber', instance.phoneNumber)
        #instance.profile_picture = validated_data.get('profile_picture'. instance.profile_picture)
        instance.save()
        return instance        

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
        fields = ('username', 'password', 'password2', 'email', 'vendor' )
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password field didin't match."})
        return attrs

    def create(self, validated_data):        
        user = User.objects.create(username=validated_data['username'],
            email=validated_data['email'], vendor=validated_data['vendor']      
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

    def update(self, instance, validated_data):        
        instance.state = validated_data.get('email', instance.state)
        instance.lga = validated_data.get('lga', instance.lga)
        instance.Address = validated_data.get('Address', instance.Address)
        instance.phoneNumber = validated_data.get('phonenUmber', instance.phoneNumber)
        instance.reg_complete = validated_data.get('reg_complete'. instance.reg_complete)
        instance.save()
        return instance       

class ChangeProfilePictures(serializers.ModelSerializer):    
    class Meta:
        model = User
        fields = ['profile_picture', ]

    def update(self, instance, validated_data):        
        instance.profile_picture = validated_data.get('profile_picture', instance.profile_picture)
        instance.save()
        return instance


class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True, required= True, validators = [validate_password])
    password2 = serializers.CharField(write_only = True, required= True )
    old_password = serializers.CharField(write_only = True, required= True)

    class Meta:
        model = User
        fields = 'old_password', 'password', 'password2'

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password field didin't match."})
        return attrs
    
    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError({"old_password": "Old Password is not correct"})
        return value
    
    def update(self, instance, validated_data):
        instance.set_password(validated_data['password'])
        instance.save()
        return instance