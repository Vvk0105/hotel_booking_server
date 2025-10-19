from django.shortcuts import render
from rest_framework import generics
from .models import Booking
from .serializers import BookingSerializer
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
class BookingListCreateView(generics.ListCreateAPIView):
    queryset = Booking.objects.all().order_by('-created_at')
    serializer_class = BookingSerializer
