from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Pais)
admin.site.register(Propiedad)
admin.site.register(ImagenPropiedad)
admin.site.register(Contacto)
from .models import Cliente
admin.site.register(Cliente)