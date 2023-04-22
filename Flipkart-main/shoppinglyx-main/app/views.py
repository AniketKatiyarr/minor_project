from django.shortcuts import render,HttpResponse,redirect
from .models import product

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

def home(request):
    
 return render(request, 'app/home.html')

def product_detail(request):
 return render(request, 'app/productdetail.html')

def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

def mobile(request):
 return render(request, 'app/mobile.html')

def login(request):
    if request.method == 'POST':
        emaill = request.POST.get('email')
        pass11 = request.POST.get('pass1')
        
        product = authenticate(email = emaill, pass1 = pass11)
        if product is not None:
            login(request,product)
            return redirect('/profile/')
        else:
            return HttpResponse("<h1>Error in password and uername</h1>")
    
    return render(request, 'app/login.html')

def customerregistration(request):
    if request.method == 'POST':
       name = request.POST.get('name')  
       email = request.POST.get('email') 
       pass1 = request.POST.get('pass1') 
       pass2 = request.POST.get('pass2')   
    
       if pass1 != pass2:
           return HttpResponse("errroorrr 404")
       else:
           details = product(name = name,email = email,pass1 = pass1,pass2 = pass2)
           details.save()
           return redirect('/login/')
        
    return render(request, 'app/customerregistration.html')

def checkout(request):
 return render(request, 'app/checkout.html')
