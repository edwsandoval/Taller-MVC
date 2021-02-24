from django.db import models

class tipodocumento(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=150)

class ciudad(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length=150)
    descripcion = models.CharField(max_length=150)


class persona(models.Model):
    id = models.AutoField(primary_key = True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    correo = models.EmailField(max_length=254)
    usuario = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    contraseña = models.CharField(max_length=100)
    fechaNacimiento = models.DateField((""), auto_now=False, auto_now_add=False)
    idTipoDocumento = models.ForeignKey(tipodocumento, on_delete=models.CASCADE)
    lugarResidencia = models.ForeignKey(ciudad, on_delete=models.CASCADE)
    documento = models.CharField(max_length=30)

def __str__(self):
    return self.nombres

 
# Create your models here.
