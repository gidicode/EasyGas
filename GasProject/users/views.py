from .serializers import *
from .models import User
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
#from .serializers import MyTokenObtainPairSerializer

#list all users and create all users
class MyTokenObtainPairView(TokenObtainPairView):
    permission_classes = (AllowAny, )
    serializer_class = MyTokenObtainPairSerializer

class RegisterView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class CompleteUserRegistration(generics.UpdateAPIView):       
    permission_classes = [IsAuthenticated]
    serializer_class = CompleteRegistration

    def get_object(self):
        user = self.request.user        
        return User.objects.get(username = user)
    
class UserDetail(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = UsersSerializers

    def get_object(self):
        user = self.request.user        
        return User.objects.get(username = user)          

class EditUser(generics.UpdateAPIView):
    permission_classes = [ IsAuthenticated ]
    serializer_class = UsersSerializers

    def get_object(self):
        user  = self.request.user
        return User.objects.get(username = user)

class ChangeProfilePicture(generics.UpdateAPIView):
    permission_classes = [ IsAuthenticated, ]
    serializer_class = ChangeProfilePictures

    def get_object(self):
        user  = self.request.user
        return User.objects.get(username = user)

class ChangePassword(generics.UpdateAPIView):
    permission_classes = [ IsAuthenticated, ]
    serializer_class = ChangePasswordSerializer

    def get_object(self):
        user = self.request.user
        return User.objects.get(username = user)

