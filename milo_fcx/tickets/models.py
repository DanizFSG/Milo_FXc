from django.db import models
# Create your models here.

class Ticket(models.Model):
    
    name = models.CharField(max_length=100)
    correo = models.EmailField(max_length=100)
    empresa = models.CharField(max_length=100)
    referencia = models.CharField(max_length=100)
    serial = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    garantia = models.CharField(max_length=100)
    accesorios = models.CharField(max_length=100)
    fuente = models.CharField(max_length=100)
    hdd = models.CharField(max_length=100)
    cables = models.CharField(max_length=100)
    caja = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    img1 = models.ImageField(upload_to='tickets/img1/', blank=True)
    img2 = models.ImageField(upload_to='tickets/img2/', blank=True)
    img3 = models.ImageField(upload_to='tickets/img3/', blank=True)
    
    
    def __str__(self):
        return self.name
    
    
    class meta:
        pass