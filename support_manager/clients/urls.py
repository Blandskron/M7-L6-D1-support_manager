from django.urls import path
from . import views

urlpatterns = [

    # CLIENTES
    path('clients/', views.client_list, name='client_list'),
    path('clients/create/', views.client_create, name='client_create'),
    path('clients/edit/<int:id>/', views.client_update, name='client_update'),
    path('clients/delete/<int:id>/', views.client_delete, name='client_delete'),

    # TICKETS
    path('tickets/', views.ticket_list, name='ticket_list'),
    path('tickets/create/', views.ticket_create, name='ticket_create'),
    path('tickets/edit/<int:id>/', views.ticket_update, name='ticket_update'),
    path('tickets/delete/<int:id>/', views.ticket_delete, name='ticket_delete'),
]