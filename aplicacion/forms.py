from django import forms
from django.forms.extras.widgets import SelectDateWidget

CHOICES=[(1,'Deportes'),(2,'Estudios'),(3,'Trabajos')]

class PublicacionForm(forms.Form):
	titulo = forms.CharField(required=True)
	descripcion = forms.CharField(widget=forms.Textarea, required=True)
	fecha_cierre = forms.DateField(widget=SelectDateWidget(), required=True)
	categoria = forms.ChoiceField(choices=CHOICES, required=True) 
	integrantes = forms.IntegerField(required=True)