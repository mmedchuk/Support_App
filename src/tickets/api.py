from django.http import JsonResponse
from rest_framework import status
from rest_framework.viewsets import ViewSet

from shared.serializers import ResponseMultiSerializer, ResponseSerializer
from tickets.models import Ticket
from tickets.serializers import TicketLightSerializer, TicketSerializer

# Create your views here.


class TicketAPISet(ViewSet):
    def list(self, request):
        queryset = Ticket.objects.all()
        serializer = TicketLightSerializer(queryset, many=True)
        response = ResponseMultiSerializer({"results": serializer.data})
        return JsonResponse(response.data)

    def retrieve(self, request, id_: int):
        instance = Ticket.objects.get(id=id_)
        serializer = TicketSerializer(instance)
        response = ResponseSerializer({"result": serializer.data})
        return JsonResponse(response.data)

    def create(self, request):
        context: dict = {
            "request": self.request,
        }
        serializer = TicketSerializer(data=request.data, context=context)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = ResponseSerializer({"result": serializer.data})

        return JsonResponse(response.data, status=status.HTTP_201_CREATED)


ticket_create = TicketAPISet.as_view({"post": "create"})
tickets_list = TicketAPISet.as_view({"get": "list"})
ticket_retrieve = TicketAPISet.as_view({"get": "retrieve"})
