from django.urls import path, include

from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
   path('', views.index, name = 'index'),
   path('index/', views.index, name='index' ),
   path('login/', views.login_request, name='login'),
   path('listing/', include("apps.listing.urls"))
]