from django.db import models
from .utils import unique_slug_generator
from django.db.models.signals import pre_save
# Create your models here.
class News(models.Model):
    slug = models.CharField(blank=True, unique=True, max_length=70)
    titulo = models.CharField(max_length=64)
    descricao = models.CharField(max_length=400)
    img_url = models.CharField(max_length=200)

    def __str__(self): 
        return self.titulo

# class Parceiros(models.Model):
#     nome = models.CharField(max_length=25,blank=True)
#     img_url = models.CharField(max_length=200)
#     def __str__(self):
#         return self.nome

# def product_pre_save_receiver(sender, instance, *args, **kwargs):
#     if not instance.slug:
#         instance.slug = unique_slug_generator(instance)

# pre_save.connect(product_pre_save_receiver, sender = News)
