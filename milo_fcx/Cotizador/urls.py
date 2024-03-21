from django.urls import path
from. import views

urlpatterns = [
   path('Cotizador/', views.cotizador, name='cotizador'),
    
]