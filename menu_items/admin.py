from django.contrib import admin
from menu_items.models import MenuItem,MenuName

# Register your models here.
admin.site.register(MenuName)
admin.site.register(MenuItem)