from django.contrib import admin
from orders.models import Order
from django.utils.html import format_html



@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('product', 'customer', 'quantity', 'price', 'address', 'phone', 'date', 'status', 'display_image', 'total')
    list_filter = ('status',)
    # list_editable = ('status',)
    search_fields = ('customer__first_name', 'customer__last_name', 'product__name')
    readonly_fields = ('date', 'total')

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.select_related('product', 'customer')

    def save_model(self, request, obj, form, change):
        if not change:
            obj.placeOrder()
        super().save_model(request, obj, form, change)

    def display_image(self, obj):
        if obj.product.image:
            image_url = obj.product.image.url
            return format_html('<a href="{}"><img src="{}" width="50" height="50" /></a>', image_url, image_url)
        return None

    display_image.short_description = 'Product Image'

    def total(self, obj):
        return obj.product.price * obj.quantity
    total.short_description = 'Total'



