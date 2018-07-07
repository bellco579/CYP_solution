from django import forms

class login_form(forms.Form):
    username = forms.CharField(label='имя пользователя', max_length=100)
    password = forms.CharField(label='пароль',widget = forms.PasswordInput(), max_length=100)
    class META:
    	pass
