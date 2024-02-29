from django.contrib import admin

from apple_app.models import(
            UserProfile, Category,
            Product, Order, 
            OrderItem, Contact,
            Liked,AvailabelSize,
            Address,
            Payment,
            Coupon
            )


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(UserProfile)
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(Liked)
admin.site.register(Contact)
admin.site.register(AvailabelSize)
admin.site.register(Address)
admin.site.register(Payment)
admin.site.register(Coupon)