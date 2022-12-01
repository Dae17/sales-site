# Create your models here.

from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class item(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="items")

    item_name = models.CharField(max_length=120)
    price = models.IntegerField()
    item_discription = models.TextField()
    photo = models.ImageField(upload_to='items')
    # is_sold = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('apps:listing:detail', args=(self.pk, ))

    def __str__(self) -> str:
        return self.item_name