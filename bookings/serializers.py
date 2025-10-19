from rest_framework import serializers
from .models import Booking
from django.views.decorators.csrf import csrf_exempt

@method_decorator(csrf_exempt, name='dispatch')
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

    def validate_phone(self, value):
        if not value.isdigit() or len(value) != 10:
            raise serializers.ValidationError('Phone number must be 10 digits')
        return value
    
    def validate_guest(self, value):
        if not value.isdigit() or value < 0:
            raise serializers.ValidationError('Guest must be atleast 1')
        return value
    
    
