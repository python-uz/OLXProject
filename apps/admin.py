from django.contrib import admin
from django.db.models import JSONField
from django_json_widget.widgets import JSONEditorWidget
from unfold.admin import ModelAdmin, TabularInline
from apps.models import Category, Product, ProductImage, ProductSpecification


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ['name', 'parent']
    formfield_overrides = {
        JSONField: {'widget': JSONEditorWidget},
    }


class ProductImageTabularInline(TabularInline):
    model = ProductImage
    min_num = 1
    extra = 0


class ProductSpecificationTabularInline(TabularInline):
    model = ProductSpecification
    min_num = 1
    extra = 0


@admin.register(Product)
class ProductAdmin(ModelAdmin):
    list_display = ['name', 'price']
    search_fields = ['name', 'price']
    inlines = [ProductImageTabularInline, ProductSpecificationTabularInline]
