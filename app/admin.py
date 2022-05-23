from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group
from admin_interface.models import Theme
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('s_no', 'brand', 'price')
    search_fields = ('s_no','brand')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('orderID', 'user')
    search_fields = ('orderID', 'user')

admin.site.register(UserInfo)
admin.site.register(Product,ProductAdmin)
admin.site.unregister(Group)
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(Order,OrderAdmin)
#admin.site.register(Theme)
