from django.urls import path
from . import views

urlpatterns = [
   path('Tickets/', views.tickets, name='tickets'),

]