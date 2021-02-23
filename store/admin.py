from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from store.models import Account,Product,Purchase
admin.site.site_header="Admin Panel"
class AccountAdmin(UserAdmin):
    list_display = ('email','first_name','last_name','date_joined','last_login','is_staff','is_admin','contact')
    search_fields = ('email','username')
    readonly_fields = ('last_login','date_joined')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
admin.site.register(Account,AccountAdmin)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name','product_quantiy','product_brand','product_added_on','product_price','product_is_avaliable')
    search_fields = ('product_name',)
    readonly_fields = ('product_added_on',)
class PurchaseAdmin(admin.ModelAdmin):
    list_display=(
    'product_purchased',
    'purchased_by',
    'purchased_on',
    'purchased_quantity')
    readonly_fields = ('purchased_on',)


admin.site.register(Product,ProductAdmin)

admin.site.register(Purchase,PurchaseAdmin)
