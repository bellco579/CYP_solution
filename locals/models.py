from django.db import models
# from user.models import user_action
# Create your models here.
class lenguage(models.Model):
	name = models.CharField(max_lenght = 20)
    class Meta:
        verbose_name = "lenguage"
        verbose_name_plural = "lenguages"

    def __str__(self):
        return '%s' % (self.name)

