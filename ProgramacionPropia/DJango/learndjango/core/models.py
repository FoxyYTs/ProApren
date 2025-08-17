from django.db import models

# Create your models here.
class Car(models.Model):
    """Model representing a car."""
    title = models.TextField(max_length=200)
    description = models.TextField(max_length=500, blank=True)
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    year = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.year}) - {self.color}"