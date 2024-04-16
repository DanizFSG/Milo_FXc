from django import forms
from .models import Ticket



class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ('name', 'correo', 'empresa','referencia','serial','marca', 'garantia', 'fuente', 'hdd', 'cables', 'caja', 'img1', 'img2', 'img3')