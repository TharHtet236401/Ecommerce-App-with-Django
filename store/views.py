from django.shortcuts import render,HttpResponse,redirect
from django.http import HttpResponse
from .models import Product
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import SignUpForm
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
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1') 
            user = authenticate(username=username,password=password)
            login(request,user)
            messages.success(request, 'Account created successfully! Welcome to our platform.')
            return redirect('home')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    if field == '__all__':  # Non-field errors (like password mismatch)
                        messages.error(request, error)
                    else:
                        messages.warning(request, f"{field}: {error}")
            return redirect('register')
    else:
        form = SignUpForm()
        return render(request,'register.html',{'form':form})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request, 'You have been logged in successfully!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password. Please try again.')
            return redirect('login')
    return render(request,'login.html')


def logout_user(request):
    logout(request)
    messages.info(request, 'You have been logged out successfully.')
    return redirect('login')


