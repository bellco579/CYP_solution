from django.shortcuts import render,redirect
from .models import order
from user.models import user_action,Profile,worker
from .create_order import create_order_class
from .forms import order_form
from competition_system.models import offer
# Create your views here.
	
def new_order(request):
	coc = create_order_class(request)
	profile = user_action(request).get_clientProfile()
	if request.POST:
		if profile != None:
			print(profile)
			form = coc.save_form(profile)
			return redirect('/')
		else:
			error = "you don't login"
	else:
		form = order_form()
	return render(request,'order/create_order.html', locals())

def every_order(request):
	every_order = order.objects.all()
	return render(request,'order/every_order.html', locals())

def order_pp(request,order_id):
	order_item = order.objects.get(id=order_id)
	return render(request,'order/order_pp.html', locals())

def show_offer(request,order_id):
	order_item = order.objects.get(id=order_id)
	profile = user_action(request).get_profile()
	if profile == order_item.client.profile:
		every_offer = offer.objects.filter(order = order_item, status = True)
		if request.POST:
			choose_worker = request.POST.get('choose worker')
			for one in every_offer:
				if one.id != choose_worker:
					every_offer.filter(id = one.id).update(status = False)
				else:
					every_offer.filter(id = one.id).update(sign = True)
	else:
		error = "you don't login"

					# one.update(status=False)
	return render(request,'order/show_offer.html', locals())

