
from django.shortcuts import render
from .forms import TicketForm
# Create your views here.
def tickets(request):

         
    return render(request, 'tickets.html')