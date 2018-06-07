from django.db import models
from quality_data.models import category
from user.models import client,worker
# Create your models here.
class order(models.Model):
	client = models.ForeignKey(client, on_delete=True)
	name = models.CharField('order name', max_length=50,default = None, null = True)
	description = models.TextField(default = None, null = True)
	category = models.ForeignKey(category, on_delete = True,default = None, null = True)
	
	class Meta:
		verbose_name = "order"
		verbose_name_plural = "orders"
	
	def __str__(self):
		return '%s' % (self.name)
	
class competition(models.Model):
	order = models.ForeignKey(order, on_delete = True)
	# work profile
	prise = models.FloatField('work price')
	time = models.IntegerField('day number')
	choose = models.BooleanField(default = False)	
	class Meta:
		verbose_name = "competition"
		verbose_name_plural = "competitions"
	
	def __str__(self):
		return '%s,%s' % (self.prise, self.time)
    	