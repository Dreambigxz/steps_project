from django.shortcuts import render, HttpResponse

from django.views.generic import TemplateView, ListView, DetailView

# Create your views here.

class homeTemplate(TemplateView):

    template_name = 'rapp/index.html'