from django.contrib import admin

from author.models import HotelBookingData, UserAccount
# Register your models here.

admin.site.register(UserAccount)
admin.site.register(HotelBookingData)