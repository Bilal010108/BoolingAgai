from django.shortcuts import render

from .filters import HotelFilter
from .serializers import *
from rest_framework import viewsets, status, generics, permissions
from .models import *
from django_filters.rest_framework import  DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .permissioms import CheckCreateHotel
from .pagination import HotelNumberPagination
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken


class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CustomLoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception:
            return Response({'detail': 'Неверные учетные данные'}, status=status.HTTP_401_UNAUTHORIZED)

        user = serializer.validated_data
        return Response(serializer.data, status=status.HTTP_200_OK)


class LogoutView(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data['refresh']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class UserProfileListAPIView(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializers

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)


class UserProfileDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializers

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)


class HotelCreateAPIView(generics.ListCreateAPIView):
    serializer_class = HotelSerializers
    permissions = [CheckCreateHotel]


    def get_queryset(self):
        return Hotel.objects.filter(owner=self.request.user)


class HotelImageViewSet(viewsets.ModelViewSet):
    queryset = HotelImage.objects.all()
    serializer_class =HotelImageSerializers



class HotelListAPIView(generics.ListAPIView)  :
    queryset = Hotel.objects.all()
    serializer_class = HotelListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter,OrderingFilter]
    filterset_class = HotelFilter
    search_fields = ['hotel_name']
    pagination_class = HotelNumberPagination




class HotelDetailAPIView(generics.RetrieveAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelDetailSerializer




class HotelEDITAPIiew(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = HotelSerializers
    permissions = [CheckCreateHotel]


    def get_queryset(self):
        return Hotel.objects.filter(owner=self.request.user)



class RoomImageViewSet(viewsets.ModelViewSet):
    queryset =RoomImage.objects.all()
    serializer_class =RoomImageSerializers



class RoomListAPIView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomListSerializers



class RoomRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomDetailSerializers



class RoomCreateAPIView(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializers



class RoomDetailAPIView(generics.RetrieveAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomDetailSerializers



class ReviewCreateAPIView(generics.ListCreateAPIView):
    queryset = Review .objects.all()
    serializer_class =ReviewSerializers


class ReviewDetailAPIView(generics.RetrieveAPIView):
     queryset = Review.objects.all()
     serializer_class = ReviewDetailSerializers


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializers


class CountryListAPIView(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializers


class CountryDetailAPIView(generics.RetrieveAPIView):
    queryset = Country.objects.all()
    serializer_class = CountryDetailSerializerAPIView


