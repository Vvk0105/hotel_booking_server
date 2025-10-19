from rest_framework import serializers
from .models import Booking

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

    def validate_phone(self, value):
        if value and (not value.isdigit() or len(value) != 10):
            raise serializers.ValidationError('Phone number must be 10 digits')
        return value
    
    def validate_guests(self, value):
        if value < 1:
            raise serializers.ValidationError('Guest must be at least 1')
        return value