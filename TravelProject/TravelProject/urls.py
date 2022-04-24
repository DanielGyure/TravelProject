"""TravelProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from viewer.views import (
    WelcomeView, TravelListView, TravelDetailView, CreateTravelView,
    UpdateTravelView, DeleteTravel, CountryListView, CountryDetailView, CreateCountryView,
    UpdateCountryView, DeleteCountry, CityListView, CityDetailView, CreateCityView, UpdateCityView,
    DeleteCityView, RegisterUser, BookTravel, ContactView, BookingListView, UserBookingListView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', WelcomeView.as_view(), name="welcome"),
    path('travels', TravelListView.as_view(), name="travels"),
    path('travels/my_booking', UserBookingListView.as_view(), name='user_booking'),
    path('travels/<int:pk>', TravelDetailView.as_view(), name='travel_detail'),
    path('travels/create', CreateTravelView.as_view(), name='create_travel'),
    path('travels/<int:pk>/update', UpdateTravelView.as_view(), name='update_travel'),
    path('travels/<int:pk>/delete', DeleteTravel.as_view(), name="delete_travel"),
    path('countries', CountryListView.as_view(), name="countries"),
    path('countries/<int:pk>', CountryDetailView.as_view(), name='country_detail'),
    path('countries/create', CreateCountryView.as_view(), name='create_country'),
    path('countries/<int:pk>/update', UpdateCountryView.as_view(), name='update_country'),
    path('countries/<int:pk>/delete', DeleteCountry.as_view(), name="delete_country"),
    path('cities', CityListView.as_view(), name="cities"),
    path('cities/<int:pk>', CityDetailView.as_view(), name='city_detail'),
    path('cities/create', CreateCityView.as_view(), name='create_city'),
    path('cities/<int:pk>/update', UpdateCityView.as_view(), name='update_city'),
    path('cities/<int:pk>/delete', DeleteCityView.as_view(), name='delete_city'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', RegisterUser.as_view(), name='register'),
    path('travels/<int:pk>/booking', BookTravel.as_view(), name="book_travel"),
    path('contact', ContactView.as_view(), name="contact"),
    path('bookings', BookingListView.as_view(), name='bookings'),
    path('captcha/', include('captcha.urls')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )