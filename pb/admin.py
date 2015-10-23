from django.contrib import admin
from pb.models import Merchent, Request, Payment, Company






class RequestAdmin(admin.ModelAdmin):
    search_fields = ['contact_num','confirmation_txid','btc_address','email_address',]


# Register your models here.
admin.site.register(Merchent)
admin.site.register(Request, RequestAdmin)
admin.site.register(Payment)
admin.site.register(Company)
