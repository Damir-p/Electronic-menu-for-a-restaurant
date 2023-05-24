from django.contrib import admin
from tinymce.widgets import TinyMCE
from django.db import models
from django.utils.html import format_html

from menu.models import Product, Category

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'display_image')
    list_filter = ('category',)
    search_fields = ('name', 'description')
    readonly_fields = ('image_preview',)

    def display_image(self, obj):
        if obj.image:
            image_url = obj.image.url
            return format_html('<a href="{}"><img src="{}" width="50" height="50" /></a>', image_url, image_url)
        return None

    def image_preview(self, obj):
        return obj.image.url if obj.image else ''

    display_image.short_description = 'Image'
    image_preview.short_description = 'Image Preview'


    display_image.short_description = 'Image'
    display_image.allow_tags = True

    image_preview.short_description = 'Image Preview'

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

