from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from.models import Cartitem 
from. models import Order, Orderitem
from. models import SingleProduct
from. models import Billing
from .forms import BillingForm

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import razorpay
from django.conf import settings

# -----------------------------
# Register View
# -----------------------------
def register(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name', '').strip()
        email = request.POST.get('email', '').strip()
        username = email.split('@')[0]  # auto-generate username from email
        password = request.POST.get('password', '').strip()
        confirm_password = request.POST.get('confirm_password', '').strip()

        # Validation
        if not full_name or not email or not password:
            messages.error(request, 'All fields are required.')
            return render(request, 'register.html')

        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'register.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email is already registered.')
            return render(request, 'register.html')

        # Create user
        user = User.objects.create_user(username=username, email=email, password=password, first_name=full_name)
        user.save()
        messages.success(request, 'Account created successfully. Please login.')
        return redirect('login_view')

    return render(request, 'register.html')


# -----------------------------
# Login View
# -----------------------------
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('username', '').strip()  # email entered in login field
        password = request.POST.get('password', '').strip()

        try:
            # Find the user by email
            user_obj = User.objects.get(email=email)
            username = user_obj.username  # get the corresponding username
            user = authenticate(request, username=username, password=password)
        except User.DoesNotExist:
            user = None

        if user is not None:
            login(request, user)
            return redirect('index')  # Redirect to homepage
        else:
            messages.error(request, 'Invalid email or password.')
            return render(request, 'login.html', {'email': email})  # keep email in form

    return render(request, 'login.html')



# -----------------------------
# Logout View
# -----------------------------
@login_required
def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('login_view')


# -----------------------------
# Example Homepage (Protected)
# -----------------------------
@login_required
def index(request):
    return render(request, 'index.html')




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


from django.contrib.auth.models import User

from django.shortcuts import render,get_object_or_404
from .models import SingleProduct
def product_list(request):
    products = SingleProduct.objects.all()
    return render(request, 'men.html', {'products': products})

def product_list1(request):
    products = SingleProduct.objects.all()
    return render(request, 'women.html', {'products': products})

def product_detail(request,product_id):
    product = get_object_or_404(SingleProduct, id=product_id)
    return render(request, 'product_deatil.html', {'product': product})


# 🛒 Display cart items
# def cart(request):
#     cart_items = Cartitem.objects.all()
#     total_amount = sum(item.total_price for item in cart_items)
#     return render(request, 'cart.html', {
#         'cart_items': cart_items,
#         'total_amount': total_amount
#     })

def cart(request):
    cart_items = Cartitem.objects.all()
    total_amount = sum(item.total_price for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_amount': total_amount})



# ➕ Add a product to the cart
def add_to_cart(request, product_id):
    product = get_object_or_404(SingleProduct, id=product_id)
    cart_item, created = Cartitem.objects.get_or_create(product=product)

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart')


# update_cart_item

def update_cart_item(request, item_id):
    cart_item = get_object_or_404(Cartitem, id=item_id)

    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))

        if quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
        else:
            cart_item.delete()

    return redirect('cart')



# remove_cart_item

def remove_cart_item(request, item_id):
    cart_items =get_object_or_404(Cartitem, id=item_id)
    cart_items.delete()
    return redirect('cart')

# checkout
# def checkout(request):
#     cart_items = Cartitem.objects.all()
#     total_amount = sum(item.total_price for item in cart_items)
#     return render(request, 'checkout.html', {'cart_items': cart_items, 'total_amount': total_amount})
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Cartitem, Billing, Order, Orderitem
from .forms import BillingForm

def checkout(request):
    cart_items = Cartitem.objects.all()
    total_price = sum(item.total_price for item in cart_items)
    total_quantity = sum(item.quantity for item in cart_items)

    if total_quantity == 0:
        messages.warning(request, "Your cart is empty. Please add items to proceed to checkout.")
        return redirect('cart')

    billing_details = Billing.objects.filter(user=request.user).first()

    if request.method == 'POST':
        form = BillingForm(request.POST, instance=billing_details)
        if form.is_valid():
            billing_details = form.save(commit=False)
            billing_details.user = request.user
            billing_details.save()

            # Create order
            order = Order.objects.create(
                user=request.user.username,
                total_price=total_price,
                total_quantity=total_quantity,
                Delivery_address=billing_details.address,
                status='Processing'
            )

            # Create order items
            for item in cart_items:
                Orderitem.objects.create(
                    order=order,
                    product=item.product,
                    quantity=item.quantity,
                    price=item.product.price
                )

            # Delete only the current user's cart items
            cart_items.delete()

            messages.success(request, "Your order has been placed successfully!")
            return redirect('order_summary', order_id=order.id)
    else:
        form = BillingForm(instance=billing_details)

    return render(request, 'checkout.html', {
        'cart_items': cart_items,
        'total_price': total_price,
        'total_quantity': total_quantity,
        'form': form
    })

def order_summary(request, order_id):

    # Fetch the order
    order = Order.objects.filter(id=order_id, user=request.user).first()

    if not order:
        messages.error(request, "Order not found.")
        return redirect('cart')

    # Fetch order items
    order_items = Orderitem.objects.filter(order=order)

    # FIXED: Call the total() method
    total_price = sum(item.total() for item in order_items)
    total_quantity = sum(item.quantity for item in order_items)

    # Razorpay Client
    client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

    razorpay_order = client.order.create({
        "amount": int(total_price * 100),
        "currency": "INR",
        "payment_capture": 1
    })

    context = {
        "order": order,
        "order_items": order_items,
        "total_price": total_price,
        "total_quantity": total_quantity,
        "razorpay_order_id": razorpay_order["id"],
        "razorpay_key": settings.RAZORPAY_KEY_ID,
        "amount": int(total_price * 100),
    }

    return render(request, "order_summary.html", context)




def payment_success(request):
    payment_id = request.GET.get("payment_id")
    order_id = request.GET.get("order_id")

    if not payment_id or not order_id:
        messages.error(request, "Invalid payment response")
        return redirect("home")

    # Fetch order
    order = Order.objects.filter(id=order_id, user=request.user).first()
    if not order:
        messages.error(request, "Order not found")
        return redirect("home")

    # Mark order as paid
    order.payment_id = payment_id
    order.status = "PAID"
    order.save()

    return render(request, "payment_success.html", {
        "order": order,
        "payment_id": payment_id
    })

from django.shortcuts import render
from .models import Order, Orderitem, Billing





    # order_items = Orderitem.objects.filter(order=order_obj)

    # total_price = sum(item.quantity * item.price for item in order_items)
    # total_quantity = sum(item.quantity for item in order_items)

    # order_items_with_names = [
    #     {
    #         'productname': item.product.title,
    #         'quantity': item.quantity,
    #         'price': item.price,
    #         'total': item.quantity * item.price
    #     }
    #     for item in order_items
    # ]

    # return render(request, 'order_summary.html', {
    #     'order': order_obj,
    #     'order_items': order_items_with_names,
    #     'total_price': total_price,
    #     'total_quantity': total_quantity
    # })


from django.shortcuts import render
from .models import Order, Orderitem
from django.contrib.auth.decorators import login_required


from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Order, Orderitem

@login_required
def order_history(request):
    # Corrected: use order_date instead of created_at
    orders = Order.objects.filter(user=request.user).order_by('-order_date')

    order_data = []

    for order in orders:
        items = Orderitem.objects.filter(order=order)

        order_data.append({
            "order": order,
            "items": items,
            "total_price": sum(item.total() for item in items),
            "total_quantity": sum(item.quantity for item in items),
        })

    return render(request, "order_history.html", {"order_data": order_data})
