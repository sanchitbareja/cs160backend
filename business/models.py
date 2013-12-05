from django.db import models

# Create your models here.

ORGANIZATION_TYPES_LIST = (
	('Restaurant', 'Restaurant'),
	('Cafe', 'Cafe'),
	)

class Business(models.Model):
	name = models.TextField(blank = True, null = True)
	lat = models.DecimalField(max_digits = 13, decimal_places = 10)
	lng = models.DecimalField(max_digits = 13, decimal_places = 10)
	avg_wait_time = models.DecimalField(max_digits = 10, decimal_places = 1)
	organization_type = models.CharField(max_length=512, null=True, blank=True, choices=ORGANIZATION_TYPES_LIST)

	def __unicode__(self):
		return self.name