from django.http import HttpResponse, Http404
from aplicacion.models import Publicacion, Usuario, Postulante
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.template import RequestContext
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from aplicacion.forms import PublicacionForm

@login_required
def publi_detalle(request, publi_id):
	publi = Publicacion.objects.get(id=publi_id)
	return render_to_response('publi_detalle.html',	{'publi':publi}, 
		context_instance=RequestContext(request))

@login_required
def publi_listar(request, publi_id):
	publis = Publicacion.objects.filter(categoria_id=publi_id)
	return render_to_response('publi_listar.html', {'publis':publis}, 
		context_instance=RequestContext(request))

@login_required
def perfil_usuario(request, usu_id):
	usuario = Usuario.objects.get(id=usu_id)
	return render_to_response('perfil_usuario.html', {'usuario':usuario},
		context_instance=RequestContext(request))

@login_required
def crear_publi(request):
	form = PublicacionForm()
	return render_to_response('crear_publi.html', {'form':form},
		context_instance=RequestContext(request))

@login_required
def admin_usuario(request):
	return render_to_response('admin_usuario.html',
		context_instance=RequestContext(request))

@login_required
def publi_Creada(request,user_id):
	publis = Publicacion.objects.filter(usuario=user_id)
	
	return render_to_response('publi_listar.html', {'publis':publis}, 
		context_instance=RequestContext(request))

@login_required#todavia no anda
def buscar(request):
	publis = Publicacion.objects.filter(nombre__contains=request.get['buscar'])
	return render_to_response('publi_listar.html',{'publis':publis},
		context_instance=RequestContext(request))

@login_required
def postularse(request,user_id,publi_id):
	p = Postulante(usuario_id=user_id,publicacion_id=publi_id)
	p.save()
	return render_to_response('homepage.html',
		context_instance=RequestContext(request))

@login_required
def publi_postuladas(request,user_id):
	postulaciones = Publicacion.objects.filter(usuario_id=user_id)
	publis = list()
	for postulacion in postulaciones:
		valor = postulacion.usuario_id
		print postulacion.usuario_id
		publi = Publicacion.objects.get(id = 2)
		if (publi != None):
			publis.append(publi)

	return render_to_response('publi_listar.html', {'publis':publis},
		context_instance=RequestContext(request))

