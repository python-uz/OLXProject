from django.contrib import admin
from apps.models import Category, Product, ProductImage, ProductSpecification


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent']


class ProductImageTabularInline(admin.TabularInline):
    model = ProductImage
    min_num = 1
    extra = 0


class ProductSpecificationTabularInline(admin.TabularInline):
    model = ProductSpecification
    min_num = 1
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
    search_fields = ['name', 'price']
    inlines = [ProductImageTabularInline, ProductSpecificationTabularInline]