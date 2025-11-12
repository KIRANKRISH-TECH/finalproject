from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('full_name', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '').strip()
        confirm_password = request.POST.get('confirm_password', '').strip()

        if not username or not email or not password:
            messages.error(request, 'All fields are required.')
        elif password != confirm_password:
            messages.error(request, 'Passwords do not match.')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'Full name already exists.')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists.')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.success(request, 'Account created successfully! Please login.')
            return redirect('login_view')

    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')


def index(request):
    return render(request, 'index.html')

def men(request):
    return render(request, 'men.html')

def women(request):
    return render(request, 'women.html')

def kids(request):
    return render(request, 'kids.html') 

def shoes(request):
    return render(request, 'shoes.html')

def contact(request):
    return render(request, 'contact.html')




from django.shortcuts import render,get_object_or_404
from .models import SingleProduct
def product_list(request):
    products = SingleProduct.objects.all()
    return render(request, 'men.html', {'products': products})


def product_detail(request,product_id):
    product = get_object_or_404(SingleProduct, id=product_id)
    return render(request, 'product_deatil.html', {'product': product})

