from django.db import models
from django.contrib.auth.models import AbstractUser 
# Create your models here.

class User(AbstractUser):
    celular_cli = models.CharField(max_length=100, blank=True)
    Nit_cli = models.CharField(max_length=100, blank=True)
    
    

