from django.contrib import admin
from django.urls import path,include
from menu_items.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('lil', index, name='lil'),
   
  
]
