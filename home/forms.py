from django import forms

from .models import etiquetas
from .models import terminados


class Formetiquetas(forms.ModelForm):
	Numero_nota = forms.CharField(widget=forms.TextInput(attrs={"class": "form form-control"}))
	Nombre_cliente = forms.CharField(widget=forms.TextInput(attrs={"class": "form form-control"}))
	Telefono = forms.CharField(widget=forms.TextInput(attrs={"class": "form form-control"}))
	Fecha_recibido = forms.CharField(widget=forms.TextInput(attrs={"class": "form form-control"}))
	Equipo = forms.CharField(widget=forms.TextInput(attrs={"class": "form form-control"}))
	Trabajo = forms.CharField(widget=forms.TextInput(attrs={"class": "form form-control"}))
	Quien_Trabajara_El_Equipo  = forms.CharField(widget=forms.TextInput(attrs={"class": "form form-control"}))
	Prende = forms.CharField(widget=forms.TextInput(attrs={"class": "form form-control"}))
	Tiene_chip_o_Sd = forms.CharField(widget=forms.TextInput(attrs={"class": "form form-control"}))
	Entrego_Apagado = forms.CharField(widget=forms.TextInput(attrs={"class": "form form-control"}))
	Crack = forms.CharField(widget=forms.TextInput(attrs={"class": "form form-control"}))
	Precio_Reparacion = forms.CharField(widget=forms.TextInput(attrs={"class": "form form-control"}))
	Descripcion_Del_Equipo= forms.CharField(widget=forms.Textarea(attrs={"class": "form form-control"}))
	
	class Meta:
		model = etiquetas
		fields = [
	
		"Numero_nota",
		"Nombre_cliente",
		"Telefono",
		"Fecha_recibido",
		"Equipo",
		"Trabajo",
		"Quien_Trabajara_El_Equipo",
		"Prende",
		"Tiene_chip_o_Sd",
		"Entrego_Apagado",
		"Crack",
		"Precio_Reparacion",
		"Descripcion_Del_Equipo",
		
		]

class FormTerminado(forms.ModelForm):
	Numero_nota_T = forms.CharField(widget=forms.TextInput(attrs={"class": "form form-control"}))
	Nombre_cliente_T = forms.CharField(widget=forms.TextInput(attrs={"class": "form form-control"}))
	Fecha_Entrega_T = forms.CharField(widget=forms.TextInput(attrs={"class": "form form-control"}))
	Terminado_T = forms.CharField(widget=forms.TextInput(attrs={"class": "form form-control"}))
	
	class Meta:
		model = terminados
		fields = [
	
		"Numero_nota_T",
		"Nombre_cliente_T",
		"Fecha_Entrega_T",
		"Terminado_T",
		
		]

