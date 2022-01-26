""" Data Models of products application """
from django.db import models


class Category(models.Model):
    """ Category data model """
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    class Meta:
        """ Change display name in admin site """
        verbose_name_plural = 'Categories'

    def __str__(self):
        return str(self.name)

    def get_friendly_name(self):
        """ return friendly name like strign method """
        return self.friendly_name


class Product(models.Model):
    """ Product data model """
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2,
                                 null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return str(self.name)
