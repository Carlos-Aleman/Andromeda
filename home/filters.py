from django.contrib.auth.models import User
import django_filters

from .models import etiquetas

class UserFilter(django_filters.FilterSet):
    class Meta:
        model = etiquetas
        fields = [
        	'Nombre_cliente',
 ]


