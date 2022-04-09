from django.contrib import admin
from viewer.models import Country, City, Travel

# Register your models here.

admin.site.register(Country)
admin.site.register(City)
admin.site.register(Travel)