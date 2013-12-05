from django.contrib import admin
from coupon.models import Coupon

#register the admin site

class CouponAdmin(admin.ModelAdmin):
	list_display = ['id','message','start','end','business']

admin.site.register(Coupon,CouponAdmin)
