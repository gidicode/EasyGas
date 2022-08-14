from django.db import models
from users.models import User
from django.utils import timezone
from PIL import Image
# Create your models here.

class Vendors(models.Model):    
    vendor_profile = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True
    )
    business_name = models.CharField(max_length=50, null=True, unique=True)
    saved_customers = models.ManyToManyField(User, blank=True, related_name='Saved_Cus')
    opening_hours = models.TimeField(auto_now=False)
    closing_hours = models.TimeField(auto_now=False)
    verified = models.BooleanField(default=False)
    company_banner =  models.ImageField(upload_to='profile_pics/', null=True)
    vendor_profile_completed = models.BooleanField(default=False)
    gas_price = models.DecimalField(max_digits= 5, decimal_places=2)
    description = models.CharField(max_length= 200, null=True)
    created_at =  models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.business_name}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs) 

        img = Image.open(self.company_banner.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.company_banner.path)

    class Meta:
        ordering = ('-created_at',)
    