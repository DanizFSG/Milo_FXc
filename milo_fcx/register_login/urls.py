from django.urls import path
from . import views

urlpatterns = [
   path('Registrar/', views.User_Register, name='User_Register'),
   path('Login/', views.user_login, name='login'),
   path("logout/", views.user_logout, name='logout'),
    
]