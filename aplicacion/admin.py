from django.contrib import admin
from .models import Usuario, Publicacion, Categoria

admin.site.register(Usuario)
admin.site.register(Publicacion)
admin.site.register(Categoria)