from django.db import models

# Create your models here.
class category(models.Model):
	name = models.CharField('specialization/academic subject', max_length=50, primary_key=True)
	class Meta:
		verbose_name = "category"
		verbose_name_plural = "category"
	def __str__(self):
		return '%s' % (self.name)

class time_type(models.Model):
    name = models.CharField(max_length=50)
    class Meta:
        verbose_name = "time_type"
        verbose_name_plural = "time_types"

    def __str__(self):
        return '%s' % (self.name)


class cost_type(models.Model):
    name = models.CharField(max_length=50)
    class Meta:
        verbose_name = "cost_type"
        verbose_name_plural = "cost_types"

    def __str__(self):
        return '%s' % (self.name)
    
