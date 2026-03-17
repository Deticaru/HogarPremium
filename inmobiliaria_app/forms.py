from .models import *
from django import forms
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox


class PropiedadForm(forms.ModelForm):
    propiedad_id = forms.IntegerField(widget=forms.HiddenInput(), required=False)
    class Meta:
        model = Propiedad
        fields = [
                'tituloPropiedad',
                'direccionPropiedad',
                'precioPropiedad',
                'paisPropiedad',
                'tipoPropiedad',
                'disponibilidadPropiedad',
                'habitacionesPropiedad',
                'bannosPropiedad',
                'metroscubPropiedad',
                'ofertaPropiedad',
                'descripcionPropiedad',
                'caracteristicasPropiedad',
                'jardinPropiedad',
                'patioPropiedad',
                'garagePropiedad',
                'sotanoPropiedad',
        ]
        widgets = {
            'descripcionPropiedad': forms.Textarea(),
            'caracteristicasPropiedad': forms.Textarea(),
        }
class ImagenesPropiedadForm(forms.ModelForm):
    class Meta:
        model = ImagenesPropiedad
        fields = [
            'imagen1Propiedad',
            'imagen2Propiedad',
            'imagen3Propiedad',
            'imagen4Propiedad',
            'imagen5Propiedad',
            'imagen6Propiedad',
            'imagen7Propiedad',
            'imagen8Propiedad',
            'imagen9Propiedad',
            'imagen10Propiedad',
            'imagen11Propiedad',
            'imagen12Propiedad',
            'imagen13Propiedad',
            'imagen14Propiedad',
            'imagen15Propiedad',
        ]

class ImagenPropiedadForm(forms.Form):
    imagenPropiedad =   forms.FileField(
        widget=forms.TextInput(attrs={'multiple': True, 'type': 'File', 'class': 'form-control'}),
        label=ImagenPropiedad._meta.get_field('imagenPropiedad').verbose_name
    )

ImagenPropiedadFormSet = forms.modelformset_factory(ImagenPropiedad, fields=('imagenPropiedad',), extra=1, can_delete=True)

class ContactoForm (forms.ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)
    class Meta:
        model = Contacto
        fields = [
            'idPropiedadContacto',
            'nombresContacto',
            'apellidosContacto',
            'emailContacto',
            'codigoPaisCelular',
            'celularContacto',
            'tipoContacto',
            'motivoContacto',
            'captcha',
        ]
        widgets = {
            'idPropiedadContacto': forms.HiddenInput(),
            'motivoContacto': forms.Textarea(),
            'celularContacto': forms.TextInput(attrs={
                'type': 'text',
                'oninput': "this.value = this.value.replace(/[^0-9]/g, '');",
                'inputmode': 'numeric'
            }),
            'nombresContacto': forms.TextInput(attrs={
                'type': 'text',
                'oninput': "this.value = this.value.replace(/[^a-zA-ZáéíóúÁÉÍÓÚñÑ\\s]/g, '');",
            }),
            'apellidosContacto': forms.TextInput(attrs={
                'type': 'text',
                'oninput': "this.value = this.value.replace(/[^a-zA-ZáéíóúÁÉÍÓÚñÑ\\s]/g, '');",
            }),
        }
    
    def __init__(self, *args, **kwargs):
        #super(ContactoForm, self).__init__(*args, **kwargs)
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            if self.instance and self.instance.pk:
                field.widget.attrs['readonly'] = True
            elif not self.instance.pk:
                # You can decide what to do for new instances here
                field.widget.attrs['readonly'] = False
        # Customize the label of the ForeignKey field to show codigoCelular
        self.fields['codigoPaisCelular'].label_from_instance = lambda obj: f"{obj.codigoCelular}"


# class ContactoVentaForm (forms.ModelForm):
#     captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)
#     class Meta:
#         model = Contacto
#         fields = [
#             'nombresContacto',
#             'apellidosContacto',
#             'emailContacto',
#             'codigoPaisCelular',
#             'celularContacto',
#             'tipoContacto',
#             'motivoContacto',
#             'captcha',
#         ]
#         widgets = {
#             'motivoContacto': forms.Textarea(),
#         }
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         # Customize the label of the ForeignKey field to show codigoCelular
#         self.fields['codigoPaisCelular'].label_from_instance = lambda obj: f"{obj.codigoCelular}"  
#         tipo_contacto_opciones = [
#             ('vear', 'Busco Arrendatarios'),
#             ('vent', 'Vendo mi Propiedad'),
#             ('otro', 'Otro')
#         ]
#         self.fields['tipoContacto'].choices = tipo_contacto_opciones 
#         self.fields['tipoContacto'].label = 'Tipo Contacto'                                             