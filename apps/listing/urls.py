from django.urls import path

from . import views

app_name = "listing"

urlpatterns = [
    path('create', views.ItemCreateView.as_view(), name = "create"),
    path('checkout', views.checkout_page, name = "checkout"),
    path('payment', views.checkout_page, name = "payment"),
    path('listing/<pk>/', views.ItemDetailView.as_view(), name='detail'),
    path('', views.list, name='list'),
]