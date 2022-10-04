# Create your models here.

from django.db import models
from django.contrib.auth import get_user_model


class item(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    item_name = models.CharField(max_length=120)
    price = models.IntegerField()
    item_discription = models.TextField()