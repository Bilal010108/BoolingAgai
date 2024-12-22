from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django .contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator






class UserProfile(AbstractUser):
    ROLE_CHOICES = (
        ('simpleUser', 'simpleUser'),
        ('ownerUser', 'ownerUser')
    )
    user_role = models.CharField(max_length=17, choices=ROLE_CHOICES, default='clientUser')
    age = models.PositiveIntegerField(null=True, blank=True, validators=[MinValueValidator(16), MaxValueValidator(50)])
    phone_number = PhoneNumberField(null=True, blank=True, region='KG')



    def __str__(self):
       return f'{self.first_name},{self.last_name}'


class Country(models.Model):
    country_name = models.CharField(max_length=32,unique=True)

    def __str__(self):
        return self.country_name



class Hotel(models.Model):
    hotel_name = models.CharField(max_length=32)
    hotel_description = models.TextField()
    country = models.ForeignKey(Country,related_name='Hotels_country',on_delete=models.CASCADE)
    city =models.CharField(max_length=32)
    address =models.CharField(max_length=32)
    hotel_stars =models. PositiveSmallIntegerField(validators=[MinValueValidator(1),
                                               MaxValueValidator(5)])
    hotel_video = models.FileField(upload_to='hotel_image',)
    created_date = models.DateField(auto_now_add=True)
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='hotel_owner')



    def __str__(self):
        return f'{self.hotel_name},{self.country},{self.city}'


    def get_avg_rating(self):
        ratings = self.reviews.all()
        if ratings.exists():
            return round(sum([i.stars for i in ratings]) / ratings.counnt(),1)
        return  0



    def get_count_people(self):
        ratings = self.reviews.all()
        if ratings.exists():
            return ratings.connt()
        return 0




class HotelImage(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    hotel_image = models.ImageField(upload_to='hotel_image/', null=True, blank=True)



    def __str__(self):
       return f'{self.hotel_image}'




class Room(models.Model):
        room_number = models.PositiveSmallIntegerField()
        hotel_room = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name="rooms")
        created_date = models.DateTimeField(auto_now_add=True)

        TYPE_CHOICES = (
            ('люкс', 'люкс'),
            ('семеный', 'семеный'),
            ('одномкстный', 'одномкстный'),
            ('двувхмкстный', 'двухмкстный'),
        )

        types = models.CharField(max_length=32, choices=TYPE_CHOICES)

        STATUS_CHOICES = (
            ('свабоден', 'свабоден'),
            ('забранирован', 'забранирован'),
            ('занят', 'занят')
        )

        room_status = models.CharField(max_length=32, choices=STATUS_CHOICES)
        room_price =models.PositiveSmallIntegerField()
        all_inclusive =models.BooleanField(default=False)
        room_description = models.TextField()


        def __str__(self):
          return f'{self.hotel_room} - {self.room_number} - {self.room_status}'


class RoomImage(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    room_image = models.ImageField(upload_to='room_image/', null=True, blank=True)



    def __str__(self):
       return f'{self.room}'




class Review (models.Model):
    user_name = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='reviews')
    text =models.TextField(null=True,blank=True)
    stars = models.CharField(max_length=16,choices=[(i,str(i)) for i in range(1,6)])
    parent= models.ForeignKey('self', related_name='replies', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user_name},{self.hotel},{self.stars}'

    class Meta:
        unique_together = ('user_name','hotel',)




class Booking(models.Model):
   hotel_book = models.ForeignKey(Hotel,on_delete=models.CASCADE)
   room_book = models.ForeignKey(Room,on_delete=models.CASCADE)
   user_book = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
   check_in = models.DateTimeField(auto_now_add=True)
   check_out = models.DateTimeField(auto_now_add=True)
   total_price = models.PositiveSmallIntegerField(default=0)

   BOOKING_CHOICES = (
       ('отменено ', 'отменено'),
       ('подтверждено', 'подтверждено '),

   )

   status_book = models.CharField(max_length=32, choices=BOOKING_CHOICES, )

   def __str__(self):
       return  f'{self.user_book},{self.hotel_book},{self.room_book},{self.status_book}'




