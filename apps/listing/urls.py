from django.urls import path

from . import views

from .views import  SearchResultsView

app_name = "listing"

urlpatterns = [
    path('', views.list, name='list'),
    path('listing/<pk>/', views.ItemDetailView.as_view(), name='detail'),
    path('create', views.ItemCreateView.as_view(), name = "create"),
    path("search/", views.SearchResultsView.as_view(), name ="search_results"),
]