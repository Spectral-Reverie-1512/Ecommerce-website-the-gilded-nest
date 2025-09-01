from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category, Order, OrderItem, Wishlist, Coupon, Profile
from .forms import SignUpForm, ReviewForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import Category, Product
from .models import Wishlist


def wishlist_view(request):
    wishlist_items = Wishlist.objects.filter(user=request.user)
    return render(request, 'store/wishlist.html', {'wishlist_items': wishlist_items})

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category)
    return render(request, 'store/category_detail.html', {
        'category': category,
        'products': products
    })

def site_context(request):
    return {
        'site_name': 'The Gilded Nest',
        'primary_color': "#654A40",
        'accent_color': "#CAB1A5"
    }

def category_products(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category)
    ctx = {
        'category': category,
        'products': products,
    }
    ctx.update(site_context(request))
    return render(request, 'store/category_products.html', ctx)

def home(request):
    new_arrivals = Product.objects.filter(is_new=True, is_active=True)[:6]
    bestsellers = Product.objects.filter(is_bestseller=True, is_active=True)[:6]
    reviews = [r for r in Product.objects.filter(is_active=True).order_by('-created_at')[:3]]

    ctx = {
        'new_arrivals': new_arrivals,
        'bestsellers': bestsellers,
        'reviews': reviews,
        'primary_color': '#ff6600'
    }

    ctx.update(site_context(request))
    return render(request, 'store/home.html', ctx)


def about(request):
    ctx = {'about_text': "Handmade boho jewelry, decor and candles crafted with love. Small-batch, sustainable materials."}
    ctx.update(site_context(request))
    return render(request, 'store/about.html', ctx)

def categories(request):
    cats = Category.objects.all()
    ctx = {'categories': cats}
    ctx.update(site_context(request))
    return render(request, 'store/categories.html', ctx)

def sale(request):
    products = Product.objects.filter(discount_price__isnull=False, is_active=True)
    ctx = {'sale_products': products}
    ctx.update(site_context(request))
    return render(request, 'store/sale.html', ctx)

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)
    review_form = ReviewForm()
    if request.method == 'POST' and request.user.is_authenticated:
        review = ReviewForm(request.POST)
        if review.is_valid():
            r = review.save(commit=False)
            r.product = product
            r.user = request.user
            r.save()
            return redirect('store:product_detail', slug=slug)
    ctx = {'product': product, 'review_form': review_form}
    ctx.update(site_context(request))
    return render(request, 'store/product_detail.html', ctx)

def _get_order(request):
    order_id = request.session.get('order_id')
    if order_id:
        try:
            return Order.objects.get(id=order_id, paid=False)
        except Order.DoesNotExist:
            pass
    if request.user.is_authenticated:
        order = Order.objects.create(user=request.user)
    else:
        order = Order.objects.create(user=None)
    request.session['order_id'] = order.id
    return order

def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    order = _get_order(request)
    
    qty = int(request.POST.get('qty', 1))
    
    item, created = OrderItem.objects.get_or_create(order=order, product=product)
    if not created:
        item.quantity += qty
    else:
        item.quantity = qty
    item.save()
    
    return redirect('store:cart')

@login_required
def cart_view(request):
    order = _get_order(request)
    ctx = {'order': order}
    ctx.update(site_context(request))
    return render(request, 'store/cart.html', ctx)

def remove_from_cart(request, item_id):
    item = get_object_or_404(OrderItem, id=item_id)
    item.delete()
    return redirect('store:cart')

def wishlist_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    items = Wishlist.objects.filter(user=request.user)
    ctx = {'items': items}
    ctx.update(site_context(request))
    return render(request, 'store/wishlist.html', ctx)

@login_required
def profile_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    orders = Order.objects.filter(user=request.user)
    ctx = {'profile': profile, 'orders': orders}
    ctx.update(site_context(request))
    return render(request, 'store/profile.html', ctx)

def checkout(request):
    order = _get_order(request)
    if request.method == 'POST':
        order.paid = True
        order.transaction_id = 'TXN' + str(order.id)
        order.save()
        del request.session['order_id']
        return render(request, 'store/checkout_success.html', {'order': order})
    ctx = {'order': order}
    ctx.update(site_context(request))
    return render(request, 'store/checkout.html', ctx)

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home') 
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})