from django.shortcuts import render
from django.views import View
from .models import Product
from django.views.generic import ListView,DetailView


# Create your views here.
class ProductListView(ListView):
    model = Product
    template_name='products/product_list.html'
    context_object_name = 'produits'

class ProductDetailView(DetailView):
    template_name="products/product_detail.html"
    model = Product
    context_object_name = 'product'