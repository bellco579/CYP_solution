from django.db import models

# Create your models here.
class category(models.Model):
	name = models.CharField('specialization/academic subject', max_length=50, primary_key=True)
	class Meta:
		verbose_name = "category"
		verbose_name_plural = "category"
	def __str__(self):
		return '%s' % (self.name)
    