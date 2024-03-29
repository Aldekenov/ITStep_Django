from django.db import models
from django.core import validators
from django.contrib.auth.models import User

class Profile(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, default='+79999999999')
    is_banned = models.BooleanField(default=False)
    img = models.ImageField(upload_to='product', null=True, blank=True, verbose_name='Аватар', default='ava.png')