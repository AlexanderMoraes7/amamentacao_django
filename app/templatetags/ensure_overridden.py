from django import template

register = template.Library()

class BlockNotOverriddenError(NotImplementedError):
    pass

@register.simple_tag
def ensure_overridden():
    '''
    Use dentro de um bloco em base.html para garantir que será sobrescrito.
    '''
    raise BlockNotOverriddenError(
            'Esse bloco deve ser sobrescrito em um template filho'
    )
