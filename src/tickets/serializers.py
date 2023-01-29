from rest_framework import serializers

from tickets.models import Ticket


class TicketCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        exclude = ["body", "manager"]


class TicketLightSerializer(serializers.ModelSerializer):
    customer = serializers.HiddenField(default=serializers.CurrentUserDefault())


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ["id", "header", "body", "customer"]
