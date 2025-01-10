from django.db import models

# Create your models here.
class Usuarios(models.Model):
    ID = models.IntegerField(primary_key=True)
    NOMBRE = models.CharField(max_length=50)
    P_APELLIDO = models.CharField(max_length=50)
    S_APELLIDO = models.CharField(max_length=50)
    USUARIO = models.CharField(max_length=50)
    CORREO = models.CharField(max_length=50)
    CLAVE = models.CharField(max_length=50)
