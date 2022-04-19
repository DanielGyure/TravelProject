from django.contrib import admin
from viewer.models import Country, City, Travel, Profile, Booking

# Register your models here.

admin.site.register(Country)
admin.site.register(City)
admin.site.register(Travel)
admin.site.register(Profile)
admin.site.register(Booking)