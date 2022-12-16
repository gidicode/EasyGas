from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from vendors import views

urlpatterns = [
    path('create-vendor-profile/', views.CreateVendorView.as_view(), name='create-vendor-page')
]

urlpatterns = format_suffix_patterns(urlpatterns)