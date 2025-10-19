from django.utils.decorators import method_decorator 
from django.shortcuts import render
from rest_framework import generics
from django.views.decorators.csrf import csrf_exempt
from .models import Booking
from .serializers import BookingSerializer

# Create your views here.
@method_decorator(csrf_exempt, name='dispatch') 
class BookingListCreateView(generics.ListCreateAPIView):
    queryset = Booking.objects.all().order_by('-created_at')
    serializer_class = BookingSerializer
