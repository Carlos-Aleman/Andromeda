from django.db import models

# Create your models here.


class etiquetas(models.Model):
	Numero_nota = models.CharField(max_length=256)
	Nombre_cliente = models.CharField(max_length=256)
	Telefono = models.CharField(max_length=256)
	Fecha_recibido = models.CharField(max_length=256)
	Equipo = models.CharField(max_length=256)
	Trabajo = models.CharField(max_length=256)
	Quien_Trabajara_El_Equipo  = models.CharField(max_length=256)
	Prende = models.CharField(max_length=256)
	Tiene_chip_o_Sd = models.CharField(max_length=256)
	Entrego_Apagado = models.CharField(max_length=256)
	Crack = models.CharField(max_length=256)
	Precio_Reparacion = models.CharField(max_length=256)
	Descripcion_Del_Equipo= models.CharField(max_length=256)



	def __str__(self):
		return self.Numero_nota



class terminados(models.Model):
	Numero_nota_T = models.CharField(max_length=256)
	Nombre_cliente_T = models.CharField(max_length=256)
	Fecha_Entrega_T = models.CharField(max_length=256)
	Terminado_T = models.CharField(max_length=256)
	


	def __str__(self):
		return self.Numero_nota_T




# --------------------------- por si acaso

class juana(models.Model):
	content = models.CharField(max_length=256)
	apellido = models.CharField(max_length=256)
	edad = models.CharField(max_length=256)
	estatura = models.CharField(max_length=256)
	nacionalidad = models.CharField(max_length=256)
	equipo = models.CharField(max_length=256)
	universidad = models.CharField(max_length=256)
	posicion = models.CharField(max_length=256)

	timestamp = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.content


class lalala(models.Model):
	content = models.CharField(max_length=256)
	apellido = models.CharField(max_length=256)
	edad = models.CharField(max_length=256)
	estatura = models.CharField(max_length=256)
	nacionalidad = models.CharField(max_length=256)
	equipo = models.CharField(max_length=256)
	universidad = models.CharField(max_length=256)
	posicion = models.CharField(max_length=256)

	timestamp = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.content


class mamma(models.Model):
	content = models.CharField(max_length=256)
	apellido = models.CharField(max_length=256)
	edad = models.CharField(max_length=256)
	estatura = models.CharField(max_length=256)
	nacionalidad = models.CharField(max_length=256)
	equipo = models.CharField(max_length=256)
	universidad = models.CharField(max_length=256)
	posicion = models.CharField(max_length=256)

	timestamp = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.content
		