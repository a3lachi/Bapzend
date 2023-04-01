from django.contrib import admin
from .models import Bapz
from .models import Customer


class BapzAdmin(admin.ModelAdmin):
    list_display = ('productname','id', 'category','price', 'color','size')


class CustomerAdmin(admin.ModelAdmin) :
    list_display = ('email','pwd','frstname','lstname','usrname','id','commands','jwt')

admin.site.register(Bapz, BapzAdmin)
admin.site.register(Customer, CustomerAdmin)



# root:pass