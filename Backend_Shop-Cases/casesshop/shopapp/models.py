from django.db import models
from django.utils.text import slugify

from .import price_choise
# Create your models here.


class Category(models.Model):
    content = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128, blank=True, null=True)

    def __str__(self):
        return self.content

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.content)
        super(Category, self).save(*args, **kwargs)


class Index_Phonto(models.Model):
    title = models.CharField(max_length=128)
    image = models.ImageField(upload_to='static/images', null=True)

    def __str__(self):
        return self.title


class Orders(models.Model):
    title = models.CharField(max_length=128)
    price = models.IntegerField()
    price_type = models.CharField(max_length=3, choices=price_choise())
    link = models.URLField()
    image = models.ImageField(upload_to='static/images', null=True)

    def __str__(self):
        return self.title
