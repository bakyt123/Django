from django.db import models
import datetime

from django.urls import reverse
from django.utils import timezone


class ItemStore(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    description = models.TextField()
    image = models.ImageField(upload_to='uploads/%y/%m/%d/', height_field=1000, width_field=800)
    price = models.FloatField(default=0)
    is_Activ = models.BooleanField(default=True)
    time_create = models.DateTimeField(auto_now=True)
    time_update = models.DateTimeField(timezone.now(), auto_now_add=True)
    cat = models.ForeignKey('Category', on_delete=models.CASCADE)


    def get_absolut_url(self):
        return reverse('item', kwargs={'item_slug': self.slug})

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})


class Menu(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, db_index=True)
