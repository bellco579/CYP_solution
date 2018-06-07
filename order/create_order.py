from .models import order
from .forms import order_form
class create_order_class(object):
	"""docstring for create_order"""
	def __init__(self, request):
		super(create_order_class, self).__init__()
		self.request = request

	def create_order(self,profile):
		new_order = order.objects.create(client = profile,description = None)
		return  new_order


	def save_form(self,profile):
		if self.request.POST:	
			new_order = self.create_order(profile)
			form = order_form(self.request.POST,instance = new_order)
			if form.is_valid:
				form.save()
				return True
			else:
				return None


	