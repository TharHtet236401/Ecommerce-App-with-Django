from django.shortcuts import render,HttpResponse
from django.http import HttpResponse
from .models import Product
# Create your views here.
def home(request):
    products = Product.objects.all()
    context = {
        'products':products
    }
    return render(request,'home.html',context)


def about(request):
    return render(request,'about.html')

