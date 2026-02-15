from django import forms
from .models import Client, Ticket

# Formularios basados en ORM (MVC - capa vista/modelo)
class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'email', 'phone']


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['client', 'title', 'description', 'status']