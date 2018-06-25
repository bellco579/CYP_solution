from django.shortcuts import render
from user.models import user_action
# Create your views here.
def home(request):
	return render(request, 'home.html',locals())