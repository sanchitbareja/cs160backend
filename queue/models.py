from django.db import models
from business.models import Business
from users.models import User

# Create your models here.
class Queue(models.Model):
	user = models.ForeignKey(User, blank = True, null = True)
	business = models.ForeignKey(Business, blank = True, null = True)
	time_entered_in_queue = models.DateTimeField(auto_now = False, auto_now_add = True)

	def __unicode__(self):
		return self.user + ":" + self.business