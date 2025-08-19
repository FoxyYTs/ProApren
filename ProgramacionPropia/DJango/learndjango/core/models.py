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
    
class Publisher(models.Model):
    """Model representing a publisher."""
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Author(models.Model):
    """Model representing an author."""
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Profile(models.Model):
    Author = models.OneToOneField(Author, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    
class Book(models.Model):
    """Model representing a book."""
    title = models.CharField(max_length=200)
    author = models.ManyToManyField(Author, related_name="libros")
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    