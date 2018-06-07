from django.shortcuts import render,redirect
from user.models import user_action
from .create_order import create_order_class
from .forms import order_form
from user.create_profiles import create_profile
# Create your views here.
def new_order(request):
	coc = create_order_class(request)
	profile = user_action(request).get_clientProfile()
	if request.POST:
		if profile != None:

			form = coc.save_form(profile)
		else:
			profile = create_profile(user_action(request).get_profile()).client_profile()
			form = coc.save_form(profile)
		if form == False:
			err = "can't created form"
		else:
			return('/')
	form = order_form()
	return render(request,'order/create_order.html', locals())