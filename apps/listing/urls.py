from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('listing/<int:id>/', views.detail, name='detail'),
    path('1/', views.detail, name = "template1"),
]