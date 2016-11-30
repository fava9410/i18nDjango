from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import ugettext as _, activate, get_language
from django.template import Library
from django.core.urlresolvers import resolve, reverse

def registro_usuario(request):
	mensaje = _("hola mundo")
	return render(request,"registro.html",{"mensaje":mensaje})
 

register = Library()

@register.simple_tag(takes_context=True)
def change_lang(context, lang=None, *args, **kwargs):
    """
    Get active page's url by a specified language
    Usage: {% change_lang 'en' %}
    """

    path = context['request'].path
    url_parts = resolve( path )

    url = path
    cur_language = get_language()
    try:
        activate(lang)
        url = reverse( url_parts.view_name, kwargs=url_parts.kwargs )
    finally:
        activate(cur_language)


    return "%s" % url