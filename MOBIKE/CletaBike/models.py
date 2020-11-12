from django.db import models
# Create your models here.
#Las ID se generan automaticamente

class Bicicleta(models.Model):
    modelo        = models.TextField(max_length=50)
    patente       = models.DecimalField(max_digits=13, decimal_places=0)
    fechaIngreso = models.DateTimeField()
    desbloqueo    = models.BooleanField()

    def __str__(self):
        return self.modelo

class Administrativo(models.Model):
    rutAdmin   = models.DecimalField(max_digits=9, decimal_places=0)
    nomAdmin   = models.TextField(max_length=50)
    telefono    = models.TextField(max_length=10)
    correo      = models.TextField(max_length=50)
    direccion   = models.TextField(max_length=100)
    
    def __str__(self):
        return self.nomAdmin
        
class Usuario(models.Model):
    dniUser    = models.DecimalField(max_digits=10, decimal_places=0)
    rutUser    = models.DecimalField(max_digits=9, decimal_places=0)
    nomUser    = models.TextField(max_length=50)
    telefono    = models.TextField(max_length=10)
    correo      = models.TextField(max_length=50)
    medioPago  = models.TextField(max_length=25)
    direccion   = models.TextField(max_length=100)
    
    def __str__(self):
        return self.nomUser

class RegistroPago(models.Model):
    dniUser    = models.ForeignKey(Usuario, blank=True, null=True, on_delete=models.SET_NULL)
    fechaPago  = models.DateTimeField(auto_now = True)
    metodoPago = models.TextField(max_length=25)

    def __str__(self):
        return self.fechaPago

class Arriendo(models.Model):
    rutUser        = models.ForeignKey(Usuario, blank=True, null=True, on_delete=models.SET_NULL)
    idRegistroPago = models.ForeignKey(RegistroPago, blank=True, null=True, on_delete=models.SET_NULL)
    idBicicleta    = models.ForeignKey(Bicicleta, blank=True, null=True, on_delete=models.SET_NULL)
    fechaPago      = models.DateTimeField(auto_now = True)
    horaArriendo   = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.rutUser
