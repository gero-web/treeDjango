from django import template
from menu_items.models import  MenuName,MenuItem
from django.db import connection


register = template.Library()
@register.inclusion_tag("menu.html", takes_context=True)
def menu(context,name):
    request = context.get("request")
    path = request.get_full_path()[1:]
    print(path)
    link  = MenuItem.objects.filter(name__name=name).prefetch_related('submenu_set')
    
    print(len(connection.queries))
    return {
        "path": path,
        
        'link': link[0],
        
        
    }
