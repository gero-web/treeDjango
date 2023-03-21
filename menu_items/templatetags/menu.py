from django import template
from menu_items.models import  MenuName,MenuItem
from django.db import connection

register = template.Library()
@register.inclusion_tag("menu.html", takes_context=True)
def menu(context,name):
    request = context.get("request")
    path = request.path 
    
    
    link = MenuName.objects.select_related('menuitem').get(name=name)
    print(link.menuitem.name)
    return {
        "path": path,
        
        'link': link,
        
        
    }