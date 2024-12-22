from .models import Hotel,Country,Room
from modeltranslation.translator import TranslationOptions,register

@register(Hotel)
class HotelTranslationOptions(TranslationOptions):
    fields = ('hotel_name', 'hotel_description', 'city', 'address')


@register(Country)
class CountryTranslationOptions(TranslationOptions):
    fields = ('country_name',)


@register(Room)
class RoomTranslationOptions(TranslationOptions):
    fields = ('room_description',)
