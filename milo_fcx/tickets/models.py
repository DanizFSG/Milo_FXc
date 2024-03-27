from django.db import models
from users.models import User

# Create your models here.

class Ticket(models.Model):
    
    tickets_id = models.ForeignKey('User_tickets', on_delete=models.CASCADE)
    tickets_name = models.CharField(max_length=200)
    tickets_email = models.EmailField(max_length=200)
    tickets_empresa = models.CharField(max_length=200)
    tickets_referencia = models.CharField(max_length=200)
    tickets_serial = models.CharField(max_length=200)
    tickets_marca = models.CharField(max_length=200)
    tickets_garantia = models.CharField(max_length=200)
    tickets_fechaIN = models.DateTimeField(auto_now_add=True)
    tickets_fechaSR = models.DateTimeField(auto_now=True)
    tickets_img1 = models.ImageField(upload_to='tickets_img1', blank=True, null=True)
    tickets_img2 = models.ImageField(upload_to='tickets_img2', blank=True, null=True)