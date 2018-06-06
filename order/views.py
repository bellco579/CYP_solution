from django.shortcuts import render,redirect
from user.models import user_action
from .create_order import create_order_class
from .forms import order_form
# Create your views here.
def new_order(request):
	coc = create_order_class(request)
	profile = user_action(request).get_clientProfile()
	if profile != None:
		if request.POST:
			new_order = coc.create_order(profile)
			form = order_form(request.POST,instance = new_order)
			if form.is_valid:
				form.save()
				return redirect('/')
			else:
				new_order.delete()
		else:
			form = order_form()

	return render(request,'order/create_order.html', locals())