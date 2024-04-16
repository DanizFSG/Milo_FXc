
from django.shortcuts import render
from .forms import TicketForm
# Create your views here.
def tickets(request):
    if request.method == 'POST':
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request,  "exitoso")
        else:
            return render(request, 'tickets.html')
  
    return render(request, 'tickets.html')