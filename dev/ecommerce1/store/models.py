from django.db import models
from django.urls import reverse

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=256, db_index=True)
    slug = models.SlugField(max_length=256, unique=True)



    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('store:single_cat', args=[self.slug])

    

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product', null=True)
    title = models.CharField(max_length=256)
    brand = models.CharField(max_length=256, default='unbranded')
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=250)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='images/')

    def get_absolute_url(self):
        return reverse('store:single', args=[self.slug])

    class Meta:
        verbose_name_plural = 'products'     

    def __str__(self):
        return self.title

