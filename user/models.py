from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib import auth
# from django.core.exceptions import AttributeError
from quality_data.models import category

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    def __str__(self):
    	return '%s' % (self.user)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class client(models.Model):
	profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
	order_number = models.IntegerField(default = 0)
	def __str__(self):
		return '%s,%s' % (self.profile,self.order_number)

class worker(models.Model):
	profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
	order_number = models.IntegerField(default = 0)
	def __str__(self):
		return '%s,%s' % (self.profile,self.order_number)

@receiver(post_save, sender=Profile)
def create_user_profile_subProfile(sender, instance, created, **kwargs):
    if created:
        worker.objects.create(profile=instance)
        client.objects.create(profile=instance)

@receiver(post_save, sender=Profile)
def save_user_profile_subProfile(sender, instance, **kwargs):
    instance.worker.save()
    instance.client.save()



class user_action(object):
	"""docstring for user_manipulation"""
	def __init__(self, request):
		super(user_action, self).__init__()
		self.request = request
		if request.POST:
			self.rp = request.POST

	def get_username(self):
		if auth.get_user(self.request).username:
			return self.request.user	
		else:
			return None	
	
	def get_profile(self):
		if self.get_username():
			return Profile.objects.get(id = self.get_username().id)

	def get_clientProfile(self):
		try:
			return self.get_profile().client
		except AttributeError:
					# create new profile
			return None

	def get_workProfile(self):
		try:
			return self.get_profile().worker()
		except AttributeError:
			return None


	# def get_profile(self):
	# 	if self.get_username():
	# 		try:
	# 			profile = Profile.client.get(id=self.get_username().id)				
	# 		except Exception:
	# 			profile = Profile.worker.get(id=self.get_username().id)				
	# 		return client_profile
	# 	else:
	# 		return None
