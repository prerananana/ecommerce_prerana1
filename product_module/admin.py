from django.contrib import admin

# Register your models here.
from .models import Brand, Category, Product
class ProductAdmin(admin.ModelAdmin):
    list_display = ["image_tag", "name", "price", "brand", "category",]
    search_fields = ["name", "price", "brand__name", "category__name",]
    list_filter = ["brand","category",]
    #readonly_fields = ["quantity",]
class Meta:
    model = Product
admin.site.register(Product, ProductAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "is_active",]
    search_fields =["name", "is_active",]
class Meta:
    model = Category
admin.site.register(Category, CategoryAdmin)

class BrandAdmin(admin.ModelAdmin):
    list_display = ["name", "is_active",]
    search_fields =["name", "is_active",]
class Meta:
    model = Brand
admin.site.register(Brand, BrandAdmin)