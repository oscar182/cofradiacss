from django import forms
from django.contrib.auth.forms import UserCreationForm 
from django.forms.extras.widgets import SelectDateWidget

CHOICES=[('Hombre','Hombre'),('Mujer','Mujer')]

class LoginForm(forms.Form):
	username = forms.CharField(required=True)
	password = forms.CharField(widget=forms.PasswordInput(), required=True)

class RegisterForm(UserCreationForm):
	fecha_nacimiento = forms.DateField(widget=SelectDateWidget(), required=True)
	telefono = forms.CharField()
	sexo = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), required=True) 
	
	