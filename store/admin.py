from django.contrib import admin
from .models import Category, Product, Profile, Review, Coupon, Order, OrderItem, Wishlist

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','category','price','discount_price','is_active','is_new','is_bestseller')
    prepopulated_fields = {"slug": ("name",)}
    list_filter = ('category','is_active','is_new','is_bestseller')

admin.site.register(Profile)
admin.site.register(Review)
admin.site.register(Coupon)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Wishlist)