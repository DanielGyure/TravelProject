import random
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from viewer.models import Travel, Country, City
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

# Create your views here.
class WelcomeView(TemplateView):
    template_name = 'welcome.html'

class TravelListView(ListView):
    template_name = 'travels.html'
    model = Travel
    context_object_name = 'travels'

class TravelDetailView(DetailView):
    template_name = 'travel_detail.html'
    model = Travel
    context_object_name = 'travel'

class CreateTravelView(PermissionRequiredMixin, CreateView):
    template_name = 'create_travel.html'
    model = Travel
    fields = '__all__'
    success_url = reverse_lazy('travels')
    permission_required = 'viewer.add_travel'

class UpdateTravelView(PermissionRequiredMixin, UpdateView):
    template_name = 'update_travel.html'
    model = Travel
    fields = '__all__'
    success_url = reverse_lazy('travels')
    context_object_name = 'travel'
    permission_required = 'viewer.change_travel'

class DeleteTravel(PermissionRequiredMixin, DeleteView):
    template_name = 'delete_travel.html'
    model = Travel
    context_object_name = 'travel'
    success_url = reverse_lazy('travels')
    permission_required = 'viewer.delete_travel'

class CountryListView(ListView):
    template_name = 'countries.html'
    model = Country
    context_object_name = 'countries'

class CountryDetailView(DetailView):
    template_name = 'country_detail.html'
    model = Country
    context_object_name = 'country'

class CreateCountryView(PermissionRequiredMixin, CreateView):
    template_name = 'create_country.html'
    model = Country
    fields = '__all__'
    success_url = reverse_lazy('countries')
    permission_required = 'viewer.add_country'

class UpdateCountryView(PermissionRequiredMixin, UpdateView):
    template_name = 'update_country.html'
    model = Country
    fields = '__all__'
    success_url = reverse_lazy('countries')
    context_object_name = 'country'
    permission_required = 'viewer.update_country'

class DeleteCountry(PermissionRequiredMixin, DeleteView):
    template_name = 'delete_country.html'
    model = Country
    context_object_name = 'country'
    success_url = reverse_lazy('countries')
    permission_required = 'viewer.delete_country'

class CityListView(ListView):
    template_name = 'cities.html'
    model = City
    context_object_name = 'cities'

class CityDetailView(DetailView):
    template_name = 'city_detail.html'
    model = City
    context_object_name = 'city'

class CreateCityView(PermissionRequiredMixin, CreateView):
    template_name = 'create_city.html'
    model = City
    fields = '__all__'
    success_url = reverse_lazy('cities')
    permission_required = 'viewer.add_city'

class UpdateCityView(PermissionRequiredMixin, UpdateView):
    template_name = 'update_city.html'
    model = City
    fields = '__all__'
    context_object_name = 'city'
    success_url = reverse_lazy('cities')
    permission_required = 'viewer.change_city'

class DeleteCityView(PermissionRequiredMixin, DeleteView):
    template_name = 'delete_city.html'
    model = City
    context_object_name = 'city'
    success_url = reverse_lazy('cities')
    permission_required = 'viewer.delete_city'