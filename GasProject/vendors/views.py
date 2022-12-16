import imp
from .serializers import *
from .models import Vendors
from users.models import User
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

class CreateVendorView(generics.ListCreateAPIView):
    queryset = Vendors.objects.all()
    permission_classes= (IsAuthenticated, )
    serializer_class = VendorsSerializers

    def get_object(self):
        user = self.request.user        
        return User.objects.get(username = user)
