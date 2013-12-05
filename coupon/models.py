from django.db import models
from business.models import Business
from datetime import datetime, timedelta

# Create your models here.
class Coupon(models.Model):
	message = models.TextField(blank = True, null = True)
	start = models.DateTimeField(auto_now_add = False, auto_now = False, default = datetime.utcnow())
	end = models.DateTimeField(auto_now_add = False, auto_now = False, default = datetime.utcnow() + timedelta(hours = 24))
	business = models.ForeignKey(Business, blank = True, null = True)

	def __unicode__(self):
		return str(self.business) + ":" + self.message