from django.views.decorators.csrf import csrf_exempt
from .serializers import UsersSerializers, RegisterSerializer
from .models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from django.http import Http404
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import MyTokenObtainPairSerializer

#list all users and create all users
class MyTokenObtainPairView(TokenObtainPairView):
    permission_classes = (AllowAny, )
    serializer_class = MyTokenObtainPairSerializer

class RegisterView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class UserDetail(APIView):
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UsersSerializers(user)
        return Response(serializer.data)        

    def put(self, request, pk, format = None):
        user = self.get_object(pk)
        serializer = UsersSerializers(user, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
