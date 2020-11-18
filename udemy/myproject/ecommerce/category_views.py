from django.shortcuts import render, HttpResponse

from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import View

from .models import Products

# Create your views here.

class SportCartigoryListView(ListView):

    context_object_name = 'sports'
    # template_name = 'category/sport.html'

    def get_queryset(self):

        sports= Products.objects.filter(category=Products.Sport)

        return sports

    def get_template_names(self):
        if self.request.is_ajax():
            return ['ecomm/home.html']
        return ['category/sport.html']
