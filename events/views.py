from django.shortcuts import render
from rest_framework.viewsets import ViewSet, ModelViewSet
from .serializers import EventSerializer, ReservationSerializer
from .models import Event, Reservation
from rest_framework.decorators import action
from rest_framework.response import Response
from typing import override
from rest_framework import status




# Create your views here.
class EventViewSet(ModelViewSet):
    serializer_class = EventSerializer

    @override
    def create(self, request, *args, **kwargs):
        many = isinstance(request.data, list)
        serializer = self.serializer_class(data=request.data, many=many)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get_queryset(self):
        self.queryset = Event.objects.all()
        status_param = self. request.query_params.get('status')
        venue_param = self.request.query_params.get('venue')

        if status_param:
            self.queryset= self.queryset.filter(status = status_param)
        if venue_param:
            self.queryset = self.queryset.filter(venue__icontains = venue_param)
        return self.queryset

#**ReservationViewSet — filter by event_id, custom cancel action**

class ReservationViewSet(ModelViewSet):
    serializer_class = ReservationSerializer

    def get_queryset(self):
        self.queryset = Reservation.objects.all()
        event_id = self.request.query_params.get('event')
        if event_id:
            self.queryset= self.queryset.filter(event_id=event_id)
        return self.queryset
    
    #@action — detail=True means URL is /reservations/{id}/cancel/
    @action(detail= True, methods=['POST'])
    def cancel(self, request, pk = None):
        reservation = self.get_object()
        if reservation.status == 'cancelled':
            return Response({'error':'Already cancelled'}, status = 400)
        reservation.event.available_seats +=reservation.seats_reserved
        reservation.event.save()
        reservation.status = 'cancelled'
        reservation.save()
        return Response(self.get_serializer(reservation).data)
    


    
