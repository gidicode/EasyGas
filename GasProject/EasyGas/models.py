from email.headerregistry import Address
from django.db import models
from users.models import User
from django.utils import timezone

class GasOrder(models.Model):
    customer = models.OneToOneField(
        User, 
        on_delete=models.CASCADE, 
        primary_key=True
    )
    order_price = models.DecimalField(max_digits= 5, decimal_places=2)
    date_created = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=100, null=True)
    total_KG =models.IntegerField(default=0)
    date_canceled = models.DateTimeField(auto_now=False)
    date_delivered = models.DateTimeField(auto_now=False)

    def __str__(self):
        return f"{self.customer}"

    class Meta:
        ordering = ('-date_created',)
    
