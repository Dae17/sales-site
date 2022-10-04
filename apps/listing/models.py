# Create your models here.

from django.db import models

class item(models.Model):
    item_name = models.CharField(max_length=120)
    price = models.IntegerField()
    item_discription = models.TextField()