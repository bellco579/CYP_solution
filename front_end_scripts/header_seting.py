from django.template.context_processors import request
from user.models import user_action

def header_config(request):
	config = []
	if user_action(request).get_username():
		server_name = ["new_order","every_order","logout",]
		view_name = ["сделать заказ","все заказы","выйти",]
	else:
		server_name = ["login","register",]
		view_name = ["вход","регистрация",]

	for i in range(len(server_name)):
		config.append({
			"server_name":server_name[i],
			"view_name":view_name[i],
			})
	return {
	"header_config":config,
	}

# def header_config(request):
# 	ifLogin = [{
# 	"server_name":"new_order",
# 	"views_name":{"rus":"сделать заказ",},
# 	}
	
# 	]
# 	# list_login = ['new_order', 'every_order', 'logout']
# 	list_not_login = ['login', 'register','every_order']
# 	return {
# 	"user_logout":list_not_login,
# 	"user_login":ifLogin,

# 	}

