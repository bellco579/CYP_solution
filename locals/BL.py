from user.models import user_action
from django.template.context_processors import request


class IP(object):
	"""docstring for IP"""
	def __init__(self, arg):
		super(IP, self).__init__()
		self.arg = arg

class session(object):
	"""docstring for session"""
	def __init__(self, arg):
		super(session, self).__init__()
		self.arg = arg

class Profile_setting(object):
	"""docstring for Profile_setting"""
	def __init__(self, arg):
		super(Profile_setting, self).__init__()
		self.arg = arg

class controller(object):
	"""get leguaage with diffrent method"""
	def __init__(self, arg):
		super(controller, self).__init__()
	user_action = user_action
	if user_action(request).get_username:
		Profile_setting().get_lenguage()	
