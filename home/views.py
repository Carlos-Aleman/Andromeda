from django.shortcuts import render, redirect
from .filters import UserFilter
from .models import etiquetas
from .forms import Formetiquetas
from .models import terminados
from .forms import FormTerminado

# Create your views here.

def index(request):
	return render(request, "home/index.html")

def inicio(request):
	queryset = terminados.objects.all() 
	context = {
	"objects": queryset

	}
	return render(request, "home/inicio.html",context)


def crearE(request):
		form = Formetiquetas(request.POST or None)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.user = request.user
			instance.save()
			return redirect('inicio')
		else:
			form = Formetiquetas()

		context= {

		"form": form

		}
		return render(request, "home/crearE.html", context)


def  ver(request):
	queryset = etiquetas.objects.all() 
	context = {
	"objects": queryset

	}
	return render(request, "home/ver.html", context)


def sacarA(request, id):
	queryset = etiquetas.objects.filter(id=id)
	context = {
		"objects": queryset
	}

	return render(request, "home/sacarA.html", context)


def updateE(request, id):
	object_etiquetas = etiquetas.objects.get(id=id)
	if request.method == "GET":
		form = Formetiquetas(instance=object_etiquetas)
	else:
		form = Formetiquetas(request.POST, instance=object_etiquetas)
		if form.is_valid():
			form.save()    #guarda el cuando se llenan todos los campos
			return redirect("inicio")
	context = {
			"form": form

			  }
	return render(request, "home/updateE.html", context)


def final(request):
		form = FormTerminado(request.POST or None)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.user = request.user
			instance.save()
			return redirect('inicio')
		else:
			form = FormTerminado()

		context= {

		"form": form

		}
		return render(request, "home/final.html", context)



def search(request):
    user_list = etiquetas.objects.all()
    user_filter = UserFilter(request.GET, queryset=user_list)
    return render(request, 'home/search.html', {'filter': user_filter})

