

from django.db import models
from users.models import User
# Create your models here.

class Ticket(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    referencia = models.CharField(max_length=100)
    serial = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    garantia = models.CharField(max_length=100)
    fuente = models.BooleanField(default=False)
    hdd = models.BooleanField(default=False)
    cables = models.BooleanField(default=False)
    caja = models.BooleanField(default=False)
    defectoDelEquipo = models.TextField(max_length=2000)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    img1 = models.ImageField(upload_to='tickets/img/', blank=True)
    img2 = models.ImageField(upload_to='tickets/img/', blank=True)
    img3 = models.ImageField(upload_to='tickets/img/', blank=True)
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.name
    
    
    class meta:
        pass