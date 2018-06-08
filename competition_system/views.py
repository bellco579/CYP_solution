from django.shortcuts import render,redirect
from .models import often
from .forms import often_form
from user.models import user_action
# Create your views here.
def create_often_form(request,order):
	work_profile = user_action(request).get_workProfile()
	if work_profile:
		if request.POST:
			new_often = ofter.objects.create(worker = profile, order = order)
			form = often_form(self.request.POST,instance = new_ofter)
			if form.is_valid:
				form.save()
			else:
				new_ofter.delete()
		else:
			form = often_form()
	else:
		return redirect('login')
	return render(request,'competition_system/create_often.html', locals())
