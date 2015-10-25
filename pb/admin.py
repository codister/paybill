from django.contrib import admin
from django.contrib.auth.models import User
from pb.models import Merchent, Request, Payment, Company
# Filters 
from django.contrib.admin import DateFieldListFilter




class RequestAdmin(admin.ModelAdmin):
    search_fields = ['contact_num','confirmation_txid','btc_address','email_address','claimer__user__username',]
    list_filter = ('is_completed', 'claimer__user__username',('date_time', DateFieldListFilter),)
    list_display = ['pk', 'contact_num', 'claimer', 'confirmation_txid',]


# Register your models here.
admin.site.register(Merchent)
admin.site.register(Request, RequestAdmin)
admin.site.register(Payment)
admin.site.register(Company)
