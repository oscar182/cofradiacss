from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.views.generic import FormView
from login.forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from aplicacion.models import Publicacion, Usuario
from datetime import date
from django.core.urlresolvers import reverse_lazy


import pdb #pdb.set_trace()

def login_page(request):
	message = None
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username, password=password)
			if user is not None:
				if user.is_active:
					login(request, user)
					message = "Te has identificado correctamente"
					return redirect('homepage')
				else:
					message = "Tu usuario esta inactivo"
			else:
				message = "Nombre de usuario y/o password incorrecto"
	else:
		form = LoginForm()
	return render_to_response('login.html', {'message':message, 'form': form},
		context_instance=RequestContext(request))

def homepage(request):
	p1 = Publicacion.objects.filter(categoria_id=1)
	p2 = Publicacion.objects.filter(categoria_id=2)
	p3 = Publicacion.objects.filter(categoria_id=3)

	return render_to_response('homepage.html',
		{'publi1': p1, 'publi2': p2, 'publi3': p3}, context_instance=RequestContext(request))

def logout_page(request):
	logout(request)
	return redirect('homepage')

class Register(FormView):
	template_name = 'register.html'
	form_class = RegisterForm
	success_url = reverse_lazy('register')


	def form_valid(self, form):
		user = form.save()
		usu = Usuario()
		usu.user = user
		usu.telefono = form.cleaned_data['telefono']
		usu.sexo = form.cleaned_data['sexo']
		usu.fechaNacimiento = form.cleaned_data['fecha_nacimiento']
		usu.save()

		return redirect('homepage')


"""
def register(request):	
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		data = request.POST.copy()
		if form.is_valid():
			new_user = form.save(data)
			logoid(new_user)
			return redirect('homepage')
	else:
		form = RegisterForm()
	return render_to_response('register.html', 
		{'form' : form},
		context_instance=RequestContext(request))"""
