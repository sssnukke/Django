from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView


class TestPageView(TemplateView):
    template_name = 'home.html'

class about(TemplateView):
    template_name = 'about.html'

# Create your views here.
