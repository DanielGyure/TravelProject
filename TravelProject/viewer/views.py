import random
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render

# Create your views here.
class WelcomeView(TemplateView):
    template_name = 'welcome.html'