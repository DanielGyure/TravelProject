import random
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from django.shortcuts import render
from viewer.models import Travel

# Create your views here.
class WelcomeView(TemplateView):
    template_name = 'welcome.html'

class TravelListView(ListView):
    template_name = 'travels.html'
    model = Travel
    context_object_name = 'travels'