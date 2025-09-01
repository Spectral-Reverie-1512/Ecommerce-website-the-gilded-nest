from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('categories/', views.categories, name='categories'),
    path('sale/', views.sale, name='sale'),
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),
    path('cart/', views.cart_view, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('wishlist/', views.wishlist_view, name='wishlist'),
    path('profile/', views.profile_view, name='profile'),
    path('add-to-cart/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('signup/', views.signup_view, name='signup'),
    path('category/<slug:slug>/', views.category_detail, name='category_detail'),
    path('category/<slug:slug>/products/', views.category_products, name='category_products'),
]