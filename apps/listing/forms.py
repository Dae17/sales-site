

from django.forms import ModelForm
from .models import item


class ListingForm(ModelForm):
    class Meta:
        model = item
        fields = ['item_name', 'price', 'item_discription']