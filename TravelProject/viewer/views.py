import random
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.shortcuts import render
from viewer.models import Travel
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