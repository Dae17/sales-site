from django.urls import path

from . import views

app_name = "listing"

urlpatterns = [
    path('', views.list, name='list'),
    path('listing/<int:id>/', views.detail, name='detail'),
    path('create', views.ItemCreateView.as_view(), name = "create"),
]