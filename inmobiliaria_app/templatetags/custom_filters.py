from django import template

register = template.Library()

@register.filter
def acortar_descripcion(value, max_lenght=130):
    if len(value) > max_lenght:
        return value[:max_lenght] + '...'
    return value
@register.filter
def acortar_titulo(value, max_lenght=60):
    if len(value) > max_lenght:
        return value[:max_lenght] + '...'
    return value
@register.filter
def formatear_dinero_uf(value):
    value = round(value)
    value = f'UF {value:,}'
    value = value.replace(',', '.')
    return value
@register.filter
def formatear_dinero_euro(value):
    value = round(value)
    value = f'€{value:,}'
    value = value.replace(',', '.')
    return value
@register.filter
def formatear_descuento(value):
    value = f'-{value}%'
    return value

@register.filter
def descuento_propiedad(precio, descuento):
    return precio-(precio*(descuento/100))