from django.db import models

# Create your models here.
class Producto(models.Model):
    ID = models.IntegerField(primary_key=True)
    nombre_prod = models.CharField(max_length=250)
    descripcion_prod = models.CharField(max_length=250)
    categoria = models.CharField(max_length=50)
    cantidad_prod = models.IntegerField()
    img1_prod = models.CharField(max_length=250)
    img2_prod = models.CharField(max_length=250)
    img3_prod = models.CharField(max_length=250)
    valor = models.FloatField()