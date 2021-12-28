from django.db import models
from productos.models import Product

class Category(models.Model):
    title = models.CharField(max_length=50)
    products = models.ManyToManyField(Product, blank=True)


    def __str__(self):
        return self.title

# Create your models here.
