from django.db import models
from django.urls import reverse

# Create your models here.
class MenuName(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.name
    
    
class MenuItem(models.Model):
    text = models.CharField(max_length=50)
    submenu = models.ForeignKey(on_delete=models.CASCADE, related_name='submenu_set',to='self',null=True, blank = True)
    name = models.OneToOneField(on_delete=models.CASCADE, to='MenuName')
    url  = models.CharField(max_length=50)
    
    def get_absolute_url(self):
        return reverse(self.url)
    
    def __str__(self) -> str:
        return self.text
    