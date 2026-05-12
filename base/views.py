from django.shortcuts import render
from django.views import View
from products.models import Product

# Create your views here.
class HomeView(View):
    def get(self,request):
        return render(request,'base/home.html',{})

class ProductListView(View):
    def get(self,request):
        products = Product.objects.all()
        return render(request,'product_list.html', {'products': products})

class ProductDetailView(View):
    def get(self,request,pk):
        product = Product.objects.get(id=pk)
        return render(request,'product_detail.html', {'product': product})        
