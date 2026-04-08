from django.urls import path, include
from inmobiliaria import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('contacto', views.contacto, name='contacto'),
    path('login', views.ingresar, name='login'),
    path('cerrar-sesion', views.cerrar_sesion, name='cerrar_sesion'),
    path('compra/propiedad', views.compra, name='compra'),
    path('arriendo',views.arriendo, name='arriendo'),
    path('venta',views.venta, name='venta'),
    path('propiedades/<accion>/<id>', views.admin_propiedades, name='admin_propiedades'),
    path('<int:id>/', views.ficha, name='ficha'),
    path('bandeja_mensaje/<accion>/<id>', views.bandeja_mensaje, name='bandeja_mensaje' ),
]