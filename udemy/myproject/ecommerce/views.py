from django.shortcuts import render, HttpResponse

from django.views.generic import TemplateView, ListView, DetailView

from .models import Products

# Create your views here.






class HomeListView(ListView):

    model = Products
    context_object_name = 'products'
    template_name = 'ecomm/home.html'

    # def get(self, request, *args, **kwargs):
    #
    #     if self.request.method == 'GET':
    #
    #         pass
    #
    #     return 'yes'




class ProductDetailView(TemplateView):

    template_name = 'ecomm/product-details.html'

    # def get(self, request, *args, **kwargs):
    #
    #     if self.request.method == 200:
    #         print('yes')

