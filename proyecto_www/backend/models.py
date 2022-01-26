from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.

class usuario (models.Model):

    rol= models.CharField(max_length=20)
    nombre= models.CharField(max_length=30)
    contrasena= models.CharField(max_length=30)

class cliente (models.Model):

    cedula = models.IntegerField(validators=[MaxValueValidator(10000000000000)])

class sede (models.Model):

    nombre= models.CharField(max_length=50)
    direccion= models.CharField(max_length=50)

class caja (models.Model):

    numero_caja = models.IntegerField(validators=[MaxValueValidator(100)])
    tipo = models.CharField(max_length=20)

class turno (models.Model):

    codigo= models.CharField(max_length=5)
    priodidad = models.BooleanField()
    tipo = models.CharField(max_length=20)
    fecha = models.DateTimeField()
    id_sede_caja = models.ForeignKey()

class sede_caja (models.Model):

    id_sede = models.ForeignKey()
    id_caja = models.ForeignKey()

class atencion (models.Model):

    id_cliente = models.ForeignKey()
    id_turno = models.ForeignKey()
    id_sede_caja = models.ForeignKey()

class usuario_sede_caja (models.Model):
    id_usuario = models.ForeignKey()
    id_sede_caja = models.ForeignKey()
    fecha = models.DateTimeField()




