from django.db import models
# from django.contrib.postgres.fields import JSONField
from user.models import worker
from order.models import order
from quality_data.models import time_type,cost_type
# Create your models here.
class offer(models.Model):
	time_work = models.IntegerField()
	time_type = models.ForeignKey(time_type, on_delete = True)
	work_cost = models.FloatField()
	cost_type = models.ForeignKey(cost_type, on_delete = True)
	status = models.BooleanField(default = True)
	order = models.ForeignKey(order, on_delete = True)
	worker = models.ForeignKey(worker, on_delete = True)
	class Meta:
		verbose_name = "offer"
		verbose_name_plural = "offers"	
	def __str__(self):	
		return '%s,%s,%s,%s' % (self.tyme_work, self.time_type,self.work_cost,self.cost_type)

		