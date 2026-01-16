from django.contrib import admin
from .models import Product, ProductImage, ProductSpecs


class ProductImageInline(admin.TabularInline):
    """Inline editor for product images"""
    model = ProductImage
    extra = 1
    fields = ['image_url', 'alt_text', 'is_primary', 'display_order']


class ProductSpecInline(admin.TabularInline):
    """Inline editor for product specifications"""
    model = ProductSpecs
    extra = 3
    fields = ['spec_name', 'spec_value']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Admin interface for Product model"""
    list_display = ['sku', 'name', 'main_category', 'subcategory', 'price', 'stock_quantity', 'created_at']
    list_filter = ['main_category', 'subcategory']
    search_fields = ['name', 'sku', 'description']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'sku')
        }),
        ('Categorization', {
            'fields': ('main_category', 'subcategory')
        }),
        ('Pricing & Inventory', {
            'fields': ('price', 'stock_quantity')
        }),
        ('Content', {
            'fields': ('description',)
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    inlines = [ProductImageInline, ProductSpecInline]


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    """Admin interface for ProductImage model"""
    list_display = ['product', 'is_primary', 'display_order', 'alt_text']
    list_filter = ['is_primary']


@admin.register(ProductSpecs)
class ProductSpecAdmin(admin.ModelAdmin):
    """Admin interface for ProductSpecs model"""
    list_display = ['product', 'spec_name', 'spec_value']
    search_fields = ['spec_name', 'spec_value']


