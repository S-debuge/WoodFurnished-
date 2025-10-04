from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'e commerce .html')

def cart(request):
    return render(request, 'cart.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

