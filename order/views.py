from django.shortcuts import render,redirect
from user.models import user_action
from .create_order import create_order_class
from .forms import order_form
# Create your views here.
def new_order(request):
	coc = create_order_class(request)
	profile = user_action(request).get_clientProfile()
	if request.POST:
		if profile != None:
			form = coc.save_form(profile)
			if form == True:
				return redirect('/')
			else:
				error = 'your form is not valid'
		else:
			return redirect('login')
	else:
		form = order_form()
	return render(request,'order/create_order.html', locals())