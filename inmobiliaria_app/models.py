from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator 
from django.utils import timezone

# Create your models here.

class Pais(models.Model):
    TIPO_MONEDA_OPCIONES = {
        ('uf', 'UF'),
        ('eu', 'EURO'),
    }

    nombrePais      = models.CharField(max_length=50, unique=True, verbose_name='Nombre de País')
    iconoPais       = models.ImageField(upload_to='imagenes/', verbose_name='Icono de País')
    tipoMoneda      = models.CharField(max_length=2, choices=TIPO_MONEDA_OPCIONES, verbose_name='UF o EURO')
    codigoCelular   = models.CharField(max_length=4, verbose_name='Código de País')

    def __str__(self):
        return self.nombrePais

class Propiedad(models.Model):
    TIPO_PROPIEDAD_OPCIONES = [
        ('ar', 'Arriendo'),
        ('ve', 'Venta'),
    ]
    DISPONIBLE_OPCIONES = [
        ('si', 'Disponible'),
        ('no', 'No Disponible'),
    ]
    JARDIN_OPCIONES = [
        ('si', 'Si tiene Jardín'),
        ('no', 'No tiene Jardín'),
    ]
    PATIO_OPCIONES = [
        ('si', 'Si tiene Patio'),
        ('no', 'No tiene Patio'),
    ]
    GARAGE_OPCIONES = [
        ('si', 'Si tiene Garage'),
        ('no', 'No tiene Garage'),
    ]
    SOTANO_OPCIONES = [
        ('si', 'Si tiene Sótano'),
        ('no', 'No tiene Sótano'),
    ]

    idPropiedad                 = models.AutoField(primary_key=True, verbose_name='ID')
    tituloPropiedad             = models.CharField(max_length=100, verbose_name='Titulo de Propiedad')
    direccionPropiedad          = models.CharField(max_length=100, verbose_name='Dirección de Propiedad')
    descripcionPropiedad        = models.CharField(max_length=1500, verbose_name='Descripción de Propiedad')
    caracteristicasPropiedad    = models.CharField(max_length=1500, verbose_name='Características de Propiedad', null=True)
    precioPropiedad             = models.IntegerField(validators=[MinValueValidator(1)], verbose_name='Precio de Propiedad') # PRECIO EN UF # PROBAR API https://api.cmfchile.cl/documentacion/UF.html
    paisPropiedad               = models.ForeignKey(Pais, on_delete=models.CASCADE, verbose_name='País de Propiedad')
    tipoPropiedad               = models.CharField(
        max_length=2,
        choices=TIPO_PROPIEDAD_OPCIONES,
        verbose_name='Arriendo o Venta'
    )
    disponibilidadPropiedad     = models.CharField(
        max_length=2,
        choices=DISPONIBLE_OPCIONES,
        verbose_name='Disponibilidad'
    )
    habitacionesPropiedad       = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], verbose_name='Cantidad de Habitaciones')
    bannosPropiedad             = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], verbose_name='Cantidad de Baños')
    metroscubPropiedad          = models.IntegerField(validators=[MinValueValidator(1)], verbose_name='Metros Cuadrados de Propiedad')
    jardinPropiedad            = models.CharField(
        max_length=2,
        choices=JARDIN_OPCIONES,
        verbose_name='¿Tiene Jardín?'
    )
    patioPropiedad            = models.CharField(
        max_length=2,
        choices=PATIO_OPCIONES,
        verbose_name='¿Tiene Patio?'
    )
    garagePropiedad            = models.CharField(
        max_length=2,
        choices=GARAGE_OPCIONES,
        verbose_name='¿Tiene Garage?'
    )
    sotanoPropiedad            = models.CharField(
        max_length=2,
        choices=SOTANO_OPCIONES,
        verbose_name='¿Tiene Sótano?'
    )

    ofertaPropiedad             = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], verbose_name='% de Oferta') 

    # '0' es SIN oferta
    # Se deberá mostrar un checkbox que es para indicar si hay oferta o no.
    # Al tener seleccionado el checkbox, dará la opción de indicar el porcentaje de descuento
    # Si no está seleccionado, se determinará automáticamente como 0 (sin oferta).
    
    def __str__(self):
        return "ID: "+ str(self.idPropiedad)+" Propiedad:"+str(self.tituloPropiedad)

class ImagenesPropiedad(models.Model):
    #FULL MONO
    idPropiedad                 =   models.ForeignKey(Propiedad, on_delete=models.CASCADE, related_name='origen', to_field='idPropiedad')
    imagen1Propiedad            =   models.ImageField(upload_to='imagenes/', verbose_name='Portada', null=True)
    imagen2Propiedad            =   models.ImageField(upload_to='imagenes/', verbose_name='Imagen de Propiedad', null=True)
    imagen3Propiedad            =   models.ImageField(upload_to='imagenes/', verbose_name='Imagen de Propiedad', null=True)
    imagen4Propiedad            =   models.ImageField(upload_to='imagenes/', verbose_name='Imagen de Propiedad', null=True)
    imagen5Propiedad            =   models.ImageField(upload_to='imagenes/', verbose_name='Imagen de Propiedad', null=True)
    imagen6Propiedad            =   models.ImageField(upload_to='imagenes/', verbose_name='Imagen de Propiedad', null=True)
    imagen7Propiedad            =   models.ImageField(upload_to='imagenes/', verbose_name='Imagen de Propiedad', null=True)
    imagen8Propiedad            =   models.ImageField(upload_to='imagenes/', verbose_name='Imagen de Propiedad', null=True)
    imagen9Propiedad            =   models.ImageField(upload_to='imagenes/', verbose_name='Imagen de Propiedad', null=True)
    imagen10Propiedad           =   models.ImageField(upload_to='imagenes/', verbose_name='Imagen de Propiedad', null=True)
    imagen11Propiedad           =   models.ImageField(upload_to='imagenes/', verbose_name='Imagen de Propiedad', null=True)
    imagen12Propiedad           =   models.ImageField(upload_to='imagenes/', verbose_name='Imagen de Propiedad', null=True)
    imagen13Propiedad           =   models.ImageField(upload_to='imagenes/', verbose_name='Imagen de Propiedad', null=True)
    imagen14Propiedad           =   models.ImageField(upload_to='imagenes/', verbose_name='Imagen de Propiedad', null=True)
    imagen15Propiedad           =   models.ImageField(upload_to='imagenes/', verbose_name='Imagen de Propiedad', null=True)
    

class ImagenPropiedad(models.Model):
    idPropiedad                 = models.ForeignKey(Propiedad, on_delete=models.CASCADE, related_name='images', to_field='idPropiedad')
    imagenPropiedad             = models.ImageField(upload_to='imagenes/', verbose_name='Imagen/es de Propiedad')

    def __str__(self):
        return "Imagen de propiedad ID: "+str(self.idPropiedad)

class Contacto(models.Model):
    TIPO_CONTACTO_OPCIONES = [
        ('comp', 'Compra'),
        ('coar', 'Compra Arriendo'),
        ('vear', 'Venta Arriendo'),
        ('vent', 'Venta'),
        ('otro', 'Otro')
    ]

    tipo_leido_opciones = [
        ('no', 'No Leído'),
        ('si', 'Leído')
    ]
    
    idContacto              = models.AutoField(primary_key=True, verbose_name='ID de Contacto')
    nombresContacto         = models.CharField(max_length=200, verbose_name='Nombres de Contacto')
    apellidosContacto       = models.CharField(max_length=200, verbose_name='Apellidos de Contacto')
    emailContacto           = models.CharField(max_length=200, verbose_name='Correo de Contacto')
    celularContacto         = models.CharField(validators=[MinLengthValidator(7)], max_length=12 ,verbose_name='Celular')
    motivoContacto          = models.CharField(max_length=1500, verbose_name='Motivo de Contacto') # Aquí va el mensaje que hará el Cliente.
    codigoPaisCelular       = models.ForeignKey(Pais, on_delete=models.CASCADE, verbose_name='Código País')
    fechaContacto           = models.DateField(default=timezone.now, verbose_name='Fecha de Contacto')
    leido                   = models.CharField(
        max_length=2,
        verbose_name='Leído / No Leído',
        choices = tipo_leido_opciones,
        null = True,
        default='no'
    )

    tipoContacto            = models.CharField(
        max_length=4, 
        verbose_name='Venta / Busca Arrendatarios / Otro',
        choices=TIPO_CONTACTO_OPCIONES)

    idPropiedadContacto     = models.ForeignKey(Propiedad, on_delete=models.SET_NULL , verbose_name='ID de Propiedad por Contacto', null=True, blank=True)

    def __str__(self):
        return "Contacto de "+ str(self.nombresContacto)+str(self.apellidosContacto)+", email: "+str(self.emailContacto)+", Celular: "+str(self.celularContacto)
    


class Carrusel(models.Model):
    idCarrusel = models.AutoField(primary_key=True, verbose_name='ID')
    imagenCarrusel = models.ImageField(upload_to='imagenes/', verbose_name='Imagen/es de carrusel')
    tituloCarrusel = models.CharField(max_length=200, verbose_name='tituloCarrusel')
    descripcionCarrusel = models.CharField(max_length=1500, verbose_name='Motivo de Contacto') # Aquí va el mensaje que hará el Cliente.

    def __str__(self):  
        return self.tituloCarrusel