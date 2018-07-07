from django.shortcuts import render,render_to_response,redirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from .forms import login_form
def register(request):
	form = UserCreationForm()
	if request.POST:
		newUser = UserCreationForm(request.POST)
		if newUser.is_valid():
			newUser.save()
			username = newUser.cleaned_data['username']
			password = newUser.cleaned_data['password2']
			user = auth.authenticate(username=username, password = password)
			auth.login(request, user)
			return redirect('home')
		else:
			form = newUser
	return render(request, 'auth/register.html',locals())

def login(request):
	login_error = None
	if request.POST:
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = auth.authenticate(username=username, password = password)
		if user is not None:
			auth.login(request,user)
			return render(request, '/')
			# print(form.get('username'))
		else:
			login_error = "неверное имя пользователя или пароль"
			
	form = login_form()
	return render(request, 'auth/login.html',locals())

# def login(request):
# 	if request.POST:
# 		username = request.POST.get('username','')
# 		password = request.POST.get('password','')
# 		user = auth.authenticate(username=username, password = password)
# 		if user is not None:
# 			auth.login(request, user)
# 			return redirect('/')
# 		else:
# 			login_error = 'user in not find'
# 			return render_to_response('auth/login.html',login_error)


# 	return render(request, 'auth/login.html',locals())

def logout(request):
	auth.logout(request)
	return redirect('home')