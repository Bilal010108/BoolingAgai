from django.urls import path,include
from .views import *
from rest_framework import routers

router = routers.SimpleRouter()

router.register(r'booking',BookingViewSet,basename='booking')
urlpatterns = [
    path('', include(router.urls)),
    path('hotels/',HotelListAPIView.as_view(),name='hotel_list'),
    path('hotels/<int:pk>/',HotelDetailAPIView.as_view(), name='hotel_detail'),
    path('hotels_create/', HotelCreateAPIView.as_view(), name='hotel_create'),
    path('hotels_create/<int:pk>/', HotelEDITAPIiew.as_view(), name='hotel_edit'),
    path('rooms/',RoomListAPIView.as_view(),name='hotel_list'),
    path('rooms/<int:pk>/', RoomRetrieveAPIView.as_view(), name='hotel_detail'),
    path('country/', CountryListAPIView.as_view(), name='country_list'),
    path('country/<int:pk>/', CountryDetailAPIView.as_view(), name='country_detail'),
    path('user/', UserProfileListAPIView.as_view(), name='user_list'),
    path('user/<int:pk>/', UserProfileDetailAPIView.as_view(), name='user_detail'),
    path('room/create/', RoomCreateAPIView.as_view(), name='room_create'),
    path('room/create/<int:pk>/', RoomDetailAPIView.as_view(), name='room_edit '),
    path('review/create/', ReviewCreateAPIView.as_view(), name='room_create'),
    path('review/create/<int:pk>/', RoomDetailAPIView.as_view(), name='room_edit '),

    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),


]
