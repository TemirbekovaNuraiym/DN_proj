from django.contrib import admin
from .models import Product, Category, ProductImage, Basket

# product/admin.py


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price', 'quantity', 'created_at', 'image')

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'image')

@admin.register(Basket)
class BascetAdmin(admin.ModelAdmin):
    list_display = ('product', 'price',)
    search_fields = ('price',)






# admin.site.register(Product, ProductAdmin)
# admin.site.register(Category)
# admin.site.register(ProductImage)
# admin.site.register(Basket)