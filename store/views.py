from django.shortcuts import render,HttpResponse,redirect
from django.http import HttpResponse
from .models import Product
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.
def home(request):
    products = Product.objects.all()
    context = {
        'products':products
    }
    return render(request,'home.html',context)


def about(request):
    return render(request,'about.html')


def register_user(request):
    return render(request,'register.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'You have been logged in')
            return redirect('home')
        else:
            messages.error(request,'Invalid username or password')
            return redirect('login')
    return render(request,'login.html')


def logout_user(request):
    logout(request)
    messages.success(request,'You have been logged out')
    return redirect('login')


