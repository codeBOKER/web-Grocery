from django.db import models
from django.utils.translation import ugettext_lazy as _

class Product(models.Model):
    PDCTname = models.CharField(max_length=50 , verbose_name=_('Product name'))
    PDCTdesc = models.TextField(max_length=500 , verbose_name=_('descriptions'),
                                blank=True , null=True)
    PDCTcateg = models.ForeignKey('Category' , on_delete=models.CASCADE,
                                     verbose_name=_('category'),
                                     blank=True , null=True)
    PDCTimage = models.ImageField(upload_to='product/%y/%m/%d' , verbose_name=_('Image'),
                                  blank=True , null=True)
    PDCTquant = models.IntegerField(verbose_name=_('Quantity'),
                                    blank=True , null=True)
    PDCTquant_type = models.CharField(max_length=10 , verbose_name=_('Quantity type'),
                                    blank=True , null=True)
    PDCTbrand = models.ForeignKey('settings.Brand' , on_delete=models.SET_NULL,
                                  verbose_name=_('Brand'),
                                  blank=True , null=True)
    PDCTprice = models.DecimalField(decimal_places=2,
                                    max_digits=8, verbose_name=_('Price'))
    PDCTcost = models.DecimalField(decimal_places=2,
                                   max_digits=8, verbose_name=_('Cost'))
    PDCTcreated = models.DateTimeField(verbose_name=_('Created date'))
    

    def __str__(self) -> str:
        return self.PDCTname
    


class ProductImage(models.Model):
    PDCTIproduct = models.ForeignKey(Product,
                                     on_delete=models.CASCADE,
                                     verbose_name=_('Product'))    
    PDCTIimage = models.ImageField(upload_to='product/%y/%m/%d',
                                   verbose_name=_('Image'),
                                   null=True,
                                   blank=True)
    def __str__(self) -> str:
        return str(self.PDCTIproduct)



class Category(models.Model):
    CATcat = models.CharField(max_length=50 , verbose_name=_('Category'))
    CATpa_cat = models.ForeignKey('self',
                                  on_delete=models.CASCADE,
                                  limit_choices_to={'CATpa_cat__isnull': True},
                                  verbose_name=_('Parent category'),
                                  blank=True , null=True)
    CATdesc = models.TextField(max_length=500 , verbose_name=_('Description'))
    CATimage = models.ImageField(upload_to='category',
                                 verbose_name=_('Category image'))

    def __str__(self) -> str:
        return str(self.CATcat)
    
class ProductAlternative(models.Model):
    PALTRproduct = models.ForeignKey(Product, on_delete=models.CASCADE,
                                   verbose_name=_('Product'))
    PALTRalternative = models.ManyToManyField(Product,
                                              related_name=_('product_alternatives'))
    
    def __str__(self) -> str:
        return str(self.PALTRproduct)
    
    class Meta:
        verbose_name = _('Product alternative')
        verbose_name_plural = _('Products alternative')


