from django.db import models
from django.utils.translation import ugettext_lazy as _


class Brand(models.Model):
    BNDname = models.CharField(max_length=50 , verbose_name=_('Name'),
                               blank=True, null=True)
    BNDdesc = models.TextField(max_length=500, verbose_name=_('Description'),
                               blank=True, null=True)
    
    def __str__(self) -> str:
        return str(self.BNDname)
    

class Variant(models.Model):
    VRTname = models.CharField(max_length=50 , verbose_name=_('Name'),
                               blank=True, null=True)
    VRTdesc = models.TextField(max_length=500, verbose_name=_('Description'),
                               blank=True, null=True)
    
    def __str__(self) -> str:
        return str(self.VRTname)

# Create your models here.
