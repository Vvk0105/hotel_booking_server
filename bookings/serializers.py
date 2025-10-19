from rest_framework import serializers
from .models import Booking

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

    def validate_phone(self, value):
        if not value.isdigit() or len(value) != 10:
            raise serializers.ValidationError('Phone number must be 10 digits')
        return value
    
    def validate_guest(self, value):
        if not value.isdigit() or value < 1:
            raise serializers.ValidationError('Guest must be atleast 1')
        return value
    
    
