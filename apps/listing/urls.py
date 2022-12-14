from django.urls import path

from . import views


app_name = "listing"

urlpatterns = [
    path('create', views.ItemCreateView.as_view(), name = "create"),
    path('checkout/<pk>', views.checkout_page, name = "checkout"),
    path('payment', views.payment, name = "payment"),
    path('update/<pk>/', views.ItemUpdateView.as_view(), name= "update"),
    path('listing/<pk>/', views.ItemDetailView.as_view(), name='detail'),
    path('', views.ListAndSearchView.as_view(), name='list'),
]