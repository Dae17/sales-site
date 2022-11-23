from django.urls import path, include

from . import views 

app_name = "users"

urlpatterns = [
   path('register/', views.register_request, name='register' ),
   path('login/', views.login_request, name='login'),
   path('logout/', views.logout_request, name='logout'),
   path('<username>/', views.UserDetailView.as_view(), name= "user-detail"),
   path('propic/', views.Profileupdate, name='Propic' )
]