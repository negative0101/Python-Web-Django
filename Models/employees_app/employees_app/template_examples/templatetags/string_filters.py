from tempfile import template

register = template.Library()


@register.filter(name='capitalize')
def capitalize(value):
    """
    capitalizes the value, makes the first letter capital and lowers the rest
    * this is TExt => This is text
    """
    value = str(value)
    return value[0].upper() + value[1:].lower()
