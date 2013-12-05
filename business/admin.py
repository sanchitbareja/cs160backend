from django.contrib import admin
from business.models import Business

#register the admin site

class BusinessAdmin(admin.ModelAdmin):
	list_display = ['id','name','lat','lng','avg_wait_time','organization_type', 'organization_subtype']

admin.site.register(Business,BusinessAdmin)
