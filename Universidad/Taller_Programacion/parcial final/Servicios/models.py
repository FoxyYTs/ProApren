from django.db import models

class Plan(models.Model):
    ID = models.IntegerField(primary_key=True)
    NOMBRE = models.CharField(max_length=250)
    TIPO = models.CharField(max_length=250)
    DESCRIPCION = models.CharField(max_length=250)
    PRECIO = models.IntegerField()
