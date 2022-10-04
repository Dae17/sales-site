from django.contrib import admin
from .models import item

# Register your models here.
@admin.register(item)
class ItemAdmin(admin.ModelAdmin):
    pass