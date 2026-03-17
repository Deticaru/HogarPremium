from django.forms import modelformset_factory
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

# Create your views here.

def test_view(request):
    return HttpResponse("Hogar Premium app is working!")

def inicio(request):
    esAdmin = request.user.is_superuser
    todas_propiedades =  Propiedad.objects.filter(disponibilidadPropiedad='si')

    context={
        'es_admin': esAdmin,
        'propiedades_todas':    todas_propiedades,
    }
    return render(request, 'inmobiliaria/inicio.html', context)

def contacto(request):
    esAdmin = request.user.is_superuser

    context={
        'es_admin': esAdmin,
    }
    return render(request, 'inmobiliaria/contacto.html', context)
def ficha (request, id):
    esAdmin = request.user.is_superuser
    propiedad = get_object_or_404(Propiedad, idPropiedad=id)

    if request.method == 'POST':
        post_data = request.POST.copy()
        post_data['idPropiedadContacto'] = id
        tipo_contacto = 'coar' if propiedad.tipoPropiedad == 'ar' else 'comp'
        post_data['tipoContacto'] = tipo_contacto

        contacto_form = ContactoForm(post_data, request.FILES)

        if contacto_form.is_valid():
            contacto_form.save()

            return redirect('ficha', id=id)
        else:  
            print("Errores en contacto_form:", contacto_form.errors)
    else:
        contacto_form = ContactoForm()

    context={
        'es_admin': esAdmin,
        'propiedad': propiedad,
        'pais': propiedad.paisPropiedad,
        'contacto_form' : contacto_form,
    }
    return render(request, 'inmobiliaria/ficha.html', context)

#@login_required
def ingresar (request):
    esAdmin = request.user.is_superuser

    context={
        'es_admin': esAdmin,
    }

    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect ('inicio')
        else:
            context['error'] = "Usuario o Contraseña Inválidos."

    
    return render(request, 'inmobiliaria/ingresar.html', context)
def compra(request):
    esAdmin = request.user.is_superuser
    if request.method == 'POST':
        post_data = request.POST.copy()
        post_data['idPropiedadContacto'] = None

        contacto_form = ContactoForm(post_data, request.POST)
        if contacto_form.is_valid():
            contacto_form.save()
            messages.success(request, "¡Mensaje enviado exitosamente!")
            return redirect('compra')
        else:
            messages.error(request, "Hubo un error en el envío de su mensaje, inténtelo nuevamente más tarde.")
            print("Errores en contacto_form:", contacto_form.errors)
    else:
        contacto_form = ContactoForm()
    
    contacto_form.fields['tipoContacto'].choices = [
        ('vear', 'Busco Arrendatarios'),
        ('vent', 'Vendo Casa'),
        ('otro', 'Otro')
    ]
    
    context = {
        'es_admin': esAdmin,
        'form_html': contacto_form
    }

    return render(request,'inmobiliaria/compra.html', context)

def arriendo(request):
    esAdmin = request.user.is_superuser
    propiedadesarriendo =   Propiedad.objects.filter(tipoPropiedad='ar', disponibilidadPropiedad='si')
    context={
        'es_admin': esAdmin,
        'propiedades_arriendo': propiedadesarriendo,
    }
    return render(request,'inmobiliaria/arriendo.html', context)
def venta(request):
    esAdmin = request.user.is_superuser
    propiedadesventa =   Propiedad.objects.filter(tipoPropiedad='ve', disponibilidadPropiedad='si')
    context={
        'es_admin': esAdmin,
        'propiedades_venta': propiedadesventa,
    }
    return render(request,'inmobiliaria/venta.html', context)

@login_required
def admin_propiedades(request, accion, id):
    esAdmin = request.user.is_superuser
    todas_propiedades = Propiedad.objects.all().order_by('-idPropiedad')
    

    # Definimos el formset para imágenes con 'extra=1' para permitir agregar nuevas imágenes
    ImagenPropiedadFormSet = modelformset_factory(
        ImagenPropiedad, 
        fields=('imagenPropiedad',), 
        extra=1,  # Permite añadir un formulario en blanco para una nueva imagen
        can_delete=True  # Permite eliminar imágenes existentes
    )

    if request.method == 'POST':

        if accion == 'crear':           
            propiedad_form = PropiedadForm(request.POST)
            imagen_form     =   ImagenPropiedadForm(request.POST, request.FILES)
            imagenes_form   =   ImagenesPropiedadForm(request.POST, request.FILES)
            # imagen_formset = ImagenPropiedadFormSet(request.POST, request.FILES)
    
            if propiedad_form.is_valid():
                propiedad = propiedad_form.save()
                for f in request.FILES.getlist('imagenPropiedad'):
                    ImagenPropiedad.objects.create(idPropiedad=propiedad, imagenPropiedad=f)
                # for form in imagen_formset:
                #     if form.cleaned_data:
                #         image = form.save(commit=False)
                #         image.idPropiedad = propiedad  # Asigna la propiedad recién creada
                #         image.save()
                return redirect('admin_propiedades', accion='crear', id='0')
            
        elif accion == 'actualizar':    
            propiedad_instance = get_object_or_404(Propiedad, idPropiedad=id)
            propiedad_form = PropiedadForm(request.POST, request.FILES, instance=propiedad_instance)
            imagen_form     =   ImagenPropiedadForm()
            imagenes_form   =   ImagenesPropiedadForm(request.POST, request.FILES)
            if propiedad_form.is_valid():
                propiedad = propiedad_form.save()

                return redirect('admin_propiedades', accion='crear', id='0')
            
        elif accion == 'eliminar': 
            propiedad = get_object_or_404(Propiedad, idPropiedad=id)
            propiedad.delete()
            return redirect('admin_propiedades', accion='crear', id='0')
        
    else:
        propiedad_form = PropiedadForm()
        imagen_form = ImagenPropiedadForm()
        imagenes_form   =   ImagenesPropiedadForm()
        #imagen_formset = ImagenPropiedadFormSet(queryset=ImagenPropiedad.objects.none())

    if request.method == 'GET':
        if accion == 'crear':
            propiedad_form = PropiedadForm()
            imagen_form = ImagenPropiedadForm()
            imagenes_form   =   ImagenesPropiedadForm()

        elif accion =='actualizar':
            propiedad_instance = get_object_or_404(Propiedad, idPropiedad=id)
            propiedad_form = PropiedadForm(instance=propiedad_instance)
            imagen_form = ImagenPropiedadForm()
            imagenes_form   =   ImagenesPropiedadForm()
            
    context = {
        'accion': accion.lower(),
        'es_admin': esAdmin,
        'propiedades_todas': todas_propiedades,
        'propiedad_form': propiedad_form,
        'imagenes_form_html' :imagenes_form,
        #'imagen_formset': imagen_formset,
        'imagen_form_html': imagen_form,
    }

    return render(request, 'inmobiliaria/admin_propiedades.html', context)

@login_required
def prueba(request, accion, id):
    esAdmin = request.user.is_superuser
    contacto_form = ContactoForm()

    todos_contactos = Contacto.objects.all()
    contCompCoar = Contacto.objects.filter(tipoContacto__in=['comp', 'coar', ]).order_by('-fechaContacto')
    contVentVear = Contacto.objects.filter(tipoContacto__in=['vent', 'vear', 'otro']).order_by('-fechaContacto')

    tipo_contacto_map = {
        'comp': 'Compra',
        'coar': 'Quiere Arrendar',
        'vear': 'Busca Arrendatarios',
        'vent': 'Vende ',
        'otro': 'Otro',
    }

    for contacto in todos_contactos:
        contacto.tipoContacto = tipo_contacto_map.get(contacto.tipoContacto, contacto.tipoContacto)
    for contacto in contCompCoar:
        contacto.tipoContacto = tipo_contacto_map.get(contacto.tipoContacto, contacto.tipoContacto)
    for contacto in contVentVear:
        contacto.tipoContacto = tipo_contacto_map.get(contacto.tipoContacto, contacto.tipoContacto)


    contacto = None
    if id != '0':
        contacto = get_object_or_404(Contacto, idContacto=id)
    
    if request.method == 'GET':
        if accion == 'inicio':
            contacto_form = ContactoForm()
        if accion == 'ver':
            contacto_form = ContactoForm(instance=Contacto.objects.get(idContacto=id))
            contacto = get_object_or_404(Contacto, idContacto = id)

    context={
        'es_admin': esAdmin,
        'todos_contactos_html':    todos_contactos,
        'propiedad_html': contacto.idPropiedadContacto if contacto else None,
        'form_html': contacto_form,
        'contCompCoar_html': contCompCoar,
        'contVentVear_html': contVentVear,
    }
    return render(request, 'inmobiliaria/prueba.html', context)


@login_required
def bandeja_mensaje(request, accion, id):
    esAdmin = request.user.is_superuser
    contacto_form = ContactoForm()

    todos_contactos = Contacto.objects.all()
    contCompCoar = Contacto.objects.filter(tipoContacto__in=['comp', 'coar', ]).order_by('-fechaContacto')
    contVentVear = Contacto.objects.filter(tipoContacto__in=['vent', 'vear', 'otro']).order_by('-fechaContacto')

    tipo_contacto_map = {
        'comp': 'Compra',
        'coar': 'Quiere Arrendar',
        'vear': 'Busca Arrendatarios',
        'vent': 'Vende ',
        'otro': 'Otro',
    }

    for contacto in todos_contactos:
        contacto.tipoContacto = tipo_contacto_map.get(contacto.tipoContacto, contacto.tipoContacto)
    for contacto in contCompCoar:
        contacto.tipoContacto = tipo_contacto_map.get(contacto.tipoContacto, contacto.tipoContacto)
    for contacto in contVentVear:
        contacto.tipoContacto = tipo_contacto_map.get(contacto.tipoContacto, contacto.tipoContacto)


    contacto = None
    if id != '0':
        contacto = get_object_or_404(Contacto, idContacto=id)
    
    if request.method == 'GET':
        if accion == 'inicio':
            contacto_form = ContactoForm()
        if accion == 'ver':
            contacto_form = ContactoForm(instance=Contacto.objects.get(idContacto=id))
            contacto = get_object_or_404(Contacto, idContacto = id)
            contacto.leido = 'si'
            contacto.save()
            contacto_form.fields['codigoPaisCelular'].disabled = True

    context={
        'es_admin': esAdmin,
        'accion': accion,
        'todos_contactos_html':    todos_contactos,
        'propiedad_html': contacto.idPropiedadContacto if contacto else None,
        'form_html': contacto_form,
        'contCompCoar_html': contCompCoar,
        'contVentVear_html': contVentVear,
    }
    def __init__(self, *args, **kwargs):
        super(contacto_form, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['disabled']    
    return render(request, 'inmobiliaria/bandeja_mensaje.html', context)

def editar(request):
    esAdmin = request.user.is_superuser
    context={
        'es_admin': esAdmin,
    }
    
    return render(request, 'inmobiliaria/editar.html', context)







