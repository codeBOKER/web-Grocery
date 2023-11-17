from django.db import models
from django.utils.translation import ugettext_lazy as _

class User(models.Model):
    USRname = models.CharField(max_length=50, verbose_name=_('Name'))
    USRemail = models.TextField(max_length=100, verbose_name=_('Email'))
    # USRpassword  = models.p
# Create your models here.
