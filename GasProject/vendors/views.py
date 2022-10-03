import imp
from .serializers import *
from .models import Vendors
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

class CreateVendorView(generics.ListCreateAPIView):
    queryset = Vendors.objects.all()
    permission_classes= (IsAuthenticated, )
    serializer_class = VendorsSerializers
# Create your views here.
