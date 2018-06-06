from .models import order
class create_order_class(object):
	"""docstring for create_order"""
	def __init__(self, request):
		super(create_order_class, self).__init__()
		self.request = request

	def create_order(self,profile):
		new_order = order.objects.create(client = profile,description = None)
		return  new_order