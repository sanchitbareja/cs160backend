from django.contrib import admin
from queue.models import Queue

#register the admin site

class QueueAdmin(admin.ModelAdmin):
	list_display = ['id','user','business','time_entered_in_queue']

admin.site.register(Queue,QueueAdmin)
