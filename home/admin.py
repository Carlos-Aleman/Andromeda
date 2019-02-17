from django.contrib import admin

# Register your models here.

from .models import etiquetas
from .models import terminados

admin.site.register(etiquetas)
admin.site.register(terminados)