from django.template.context_processors import request
from user.models import user_action

def header_config(request):
	if_login = [
		{
		"server_name":"new_order",
		"view_name":"создать заказ",
		}
	]	
	return {
	"header_config_if_login":if_login,
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

