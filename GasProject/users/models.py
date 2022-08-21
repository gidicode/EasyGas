from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from PIL import Image
#from vendors.models import Vendors

# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=50, null=True, unique=True)
    email = models.EmailField(verbose_name='email_address', null=True, unique=True)
    state = models.CharField(max_length=50, null=True)
    lga = models.CharField(max_length=100, null=True)
    phoneNumber = models.CharField(max_length=14, null=True)
    Address = models.CharField(max_length=200, null=True)
    favourite_vendors = models.ManyToManyField('vendors.Vendors', blank=True)
    reg_complete = models.BooleanField(default=False)
    profile_picture = models.ImageField(default='default.jpg', upload_to='profile_pics/', null=True)
    date_joined = models.DateTimeField(default=timezone.now)
    vendor = models.BooleanField(default=False)

    USERNAME_FIELD =  'email'
    REQUIRED_FIELDS = ['username', 'phoneNumber']

    def __str__(self):
        return f"{self.username}"
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs) 

        img = Image.open(self.profile_picture.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.profile_picture.path)

    class Meta:
        ordering = ('-date_joined',)
    