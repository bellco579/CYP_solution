from django.shortcuts import render,redirect
from .models import offer
from .forms import offer_form
from user.models import user_action
# Create your views here.
def create_offer(request,order):
	work_profile = user_action(request).get_workProfile()
	print(work_profile)
	if work_profile:
		if request.POST:
			new_offer = ofter.objects.create(worker = profile, order = order)
			form = offer_form(self.request.POST,instance = new_ofter)
			if form.is_valid:
				form.save()
			else:
				new_ofter.delete()
		else:
			form = offer_form()
	else:
		return redirect('login')
	return render(request,'competition_system/create_offer.html', locals())

