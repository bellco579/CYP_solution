from .models import order
from .forms import order_form
class create_order_class(object):
	"""docstring for create_order"""
	def __init__(self, request):
		super(create_order_class, self).__init__()
		self.request = request
		
	def save_form(self,profile):
		new_order = order.objects.create(client = profile)
		form = order_form(self.request.POST,instance = new_order)
		if form.is_valid:
			form.save()
			return True
		else:
			return None


	