from django.urls import path

from tickets.api import ticket_create, ticket_retrieve, tickets_list

urlpatterns = [
    path("", tickets_list),
    path("", ticket_create),
    path("<int:id_>/", ticket_retrieve),
]
