from django.views.decorators.csrf import csrf_exempt
from .serializers import UsersSerializers
from .models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

#list all users and create all users

class UserList(APIView):
    def get(self, request, format=None):
        users = User.objects.all()        
        serializer = UsersSerializers(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UsersSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

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
