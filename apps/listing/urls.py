from django.urls import path

from . import views


app_name = "listing"

urlpatterns = [
    path('', views.ListAndSearchView.as_view(), name='list'),
    path('listing/<pk>/', views.ItemDetailView.as_view(), name='detail'),
    path('create', views.ItemCreateView.as_view(), name = "create"),
    path('update/<pk>/', views.ItemUpdateView.as_view(), name= "update"),
]