from django.db import models
from business.models import Business

# Create your models here.
class Coupon(models.Model):
	message = models.TextField(blank = True, null = True)
	start = models.DecimalField(max_digits = 13, decimal_places = 10)
	end = models.DecimalField(max_digits = 13, decimal_places = 10)
	business = models.ForeignKey(Business, blank = True, null = True)

	def __unicode__(self):
		return self.business + ":" + self.message