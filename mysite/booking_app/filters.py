from django_filters import FilterSet
from .models import Hotel,Room
from django_filters import FilterSet


class HotelFilter(FilterSet):
    class Meta:
        model = Hotel
        fields = {
            'hotel_stars': ['gt', 'lt'],
            'country': ['exact'],
            'city': ['exact'],

        }


class RoomFilter(FilterSet):
    class Meta:
        model = Room
        fields = {
            'room_price': ['gt', 'lt'],

        }
