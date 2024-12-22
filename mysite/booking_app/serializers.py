from rest_framework import serializers
from .models import *

from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password', 'first_name', 'last_name', 'age',
                  'phone_number')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }



class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError('Неверные учетные данные')

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class UserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields ='__all__'


class UserProfileSimpleSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields =['first_name','last_name']


class HotelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields ='__all__'


class HotelImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = HotelImage
        fields = '__all__'



class RoomImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = RoomImage
        fields = ['room_image']





class RoomListSerializers(serializers.ModelSerializer):
    room_images = RoomImageSerializers(many=True,read_only=True)

    class Meta:
        model = Room
        fields = ['id','room_number','room_status','types','room_price','room_images']



class RoomDetailSerializers(serializers.ModelSerializer):
    room_images = RoomImageSerializers(many=True, read_only=True)
    class Meta:
        model =Room
        fields = ['room_number','room_status', 'room_price','all_inclusive','room_description','room_images']


class RoomSerializers(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields ='__all__'


class  ReviewSerializers(serializers.ModelSerializer):
    user_name =UserProfileSimpleSerializers()

    class Meta:
        model =  Review
        fields = ['user_name','text','parent']


class ReviewDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model =Review
        fields = '__all__'





class  BookingSerializers(serializers.ModelSerializer):
    class Meta:
        model =  Booking
        fields = '__all__'


class CountrySerializers(serializers.ModelSerializer):
   class Meta:
            model = Country
            fields = ['country_name']


class HotelDetailSerializer(serializers.ModelSerializer):
    country = CountrySerializers()
    hotel_image = HotelImageSerializers(read_only=True, many=True)
    created_date = serializers.DateField(format='%d-%m-%Y')
    owner = UserProfileSimpleSerializers()
    rooms = RoomListSerializers(many=True,read_only=True)
    reviews = ReviewSerializers(many=True,read_only=True)
    count_people = serializers.SerializerMethodField()
    avg_rating = serializers.SerializerMethodField()

    class Meta:
        model = Hotel
        fields = ['hotel_name','country','owner','hotel_description','city',
                  'hotel_video','hotel_stars','created_date',
                  'hotel_image','reviews','rooms', 'avg_rating','count_people']

    def get_avg_rating(self, obj):
            return obj.get_avg_rating()

    def get_count_people(self, obj):
            return obj.get_count_people()


class HotelListSerializer(serializers.ModelSerializer):
    created_date = serializers.DateField(format='%d-%m-%Y')
    hotel_image = HotelImageSerializers(many=True,read_only=True)
    avg_rating = serializers.SerializerMethodField()
    count_people = serializers.SerializerMethodField()


    class Meta:
        model = Hotel
        fields = ['id','hotel_name','city','address','hotel_stars',
                  'created_date','hotel_image','avg_rating', 'count_people']


    def get_count_people(self, obj):
        return obj.get_count_people()


    def get_avg_rating(self, obj):
        return obj.get_avg_rating()



class CountryDetailSerializerAPIView(serializers.ModelSerializer):
    Hotels_country = HotelListSerializer(many=True,read_only=True)

    class Meta:
        model =  Country
        fields = '__all__'


