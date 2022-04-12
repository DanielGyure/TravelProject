import random
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from viewer.models import Travel, Country
from django.urls import reverse_lazy

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

class CreateTravelView(CreateView):
    template_name = 'create_travel.html'
    model = Travel
    fields = '__all__'
    success_url = reverse_lazy('travels')

class UpdateTravelView(UpdateView):
    template_name = 'update_travel.html'
    model = Travel
    fields = '__all__'
    success_url = reverse_lazy('travels')
    context_object_name = 'travel'

class DeleteTravel(DeleteView):
    template_name = 'delete_travel.html'
    model = Travel
    context_object_name = 'travel'
    success_url = reverse_lazy('travels')

class CountryListView(ListView):
    template_name = 'countries.html'
    model = Country
    context_object_name = 'countries'