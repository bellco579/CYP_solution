from django.template.context_processors import request
from user.models import user_action

def user_and_profile(request):
	ua = user_action(request)
	username = 	ua.get_username()
	work_profile = ua.get_workProfile()
	client_profile = ua.get_clientProfile()
	
	return {
	"username":username,
	"work_profile": work_profile,
	"client_profile":client_profile,
	}
