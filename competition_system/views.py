from django.shortcuts import render,redirect
from .models import offer
from .forms import offer_form
from user.models import user_action
from order.models import order
# Create your views here.
def create_offer(request,order_id):
	work_profile = user_action(request).get_workProfile()
	print(work_profile)
	if work_profile:
		if request.POST:
			print(order_id)
			order_for_offer = order.objects.get(id = order_id)
			new_offer = offer.objects.create(worker = work_profile, order = order_for_offer)
			form = offer_form(self.request.POST,instance = new_offer)
			if form.is_valid:
				form.save()
			else:
				new_offer.delete()
		else:
			form = offer_form()
	else:
		return redirect('login')
	return render(request,'competition_system/create_offer.html', locals())

