from django.shortcuts import render
from django.views.generic import View
from .models import Product


class Home(View):
    def get(self,request):
        return render(request,'shop.html')

    def post(self,request):
        Product.objects.create(product_name=request.POST['product_name'])
        return render(request,'shop.html')
