from django.db import models
# from django.core.validators import MinValueValidator, MaxValueValidator

class Product(models.Model):
    PDCTname = models.CharField(max_length=50 , verbose_name=('Product name'))
    PDCTdesc = models.TextField(max_length=500 , verbose_name=('descriptions'),
                                blank=True , null=True)
    PDCTcateg = models.ForeignKey('Category' , on_delete=models.CASCADE,
                                     verbose_name=('category'),
                                     blank=True , null=True)
    PDCTimage = models.ImageField(upload_to='product/%y/%m/%d' , verbose_name=('Image'),
                                  blank=True , null=True)
    PDCTquant = models.IntegerField(verbose_name=('Quantity'),
                                    blank=True , null=True)
    PDCTquant_type = models.CharField(max_length=10 , verbose_name=('Quantity type'),
                                    blank=True , null=True)
    PDCTbrand = models.ForeignKey('settings.Brand' , on_delete=models.SET_NULL,
                                  verbose_name=('Brand'),
                                  blank=True , null=True)
    PDCTprice = models.DecimalField(decimal_places=2,
                                    max_digits=8, verbose_name=('Price'))
    PDCTcost = models.DecimalField(decimal_places=2,
                                   max_digits=8, verbose_name=('Cost'))
    PDCTcreated = models.DateTimeField(verbose_name=('Created date'))

    # PDCTdsct_prct = models.FloatField(default=0,
    #                                   validators=[MinValueValidator(0), MaxValueValidator(100)],
    #                                   verbose_name=('discount percent'))

    # def discounted_price(self):
    #     category_discount = self.PDCTcateg.CATdsct_prct
    #     product_discount = self.PDCTdsct_prct

    #     if product_discount > 0:
    #         final_discount = product_discount
    #     else:
    #         final_discount = category_discount

    #     discounted_price = self.price * (1 - final_discount)
    #     return discounted_price
    
    

    def __str__(self) -> str:
        return self.PDCTname
    


class ProductImage(models.Model):
    PDCTIproduct = models.ForeignKey(Product,
                                     on_delete=models.CASCADE,
                                     verbose_name=('Product'))    
    PDCTIimage = models.ImageField(upload_to='product/%y/%m/%d',
                                   verbose_name=('Image'),
                                   null=True,
                                   blank=True)
    def __str__(self) -> str:
        return str(self.PDCTIproduct)



class Category(models.Model):
    CATcat = models.CharField(max_length=50 , verbose_name=('Category'))
    CATpa_cat = models.ForeignKey('self',
                                  on_delete=models.CASCADE,
                                  limit_choices_to={'CATpa_cat__isnull': True},
                                  verbose_name=('Parent category'),
                                  blank=True , null=True)
    CATdesc = models.TextField(max_length=500 , verbose_name=('Description'))
    CATimage = models.ImageField(upload_to='category',
                                 verbose_name=('Category image'))

    def __str__(self) -> str:
        return str(self.CATcat)

# class Discount(models.Model):
    # DISimage = models.ImageField(upload_to='discount_images/')
    # DIScategory = models.ForeignKey('Category', on_delete=models.CASCADE)
    # DISproducts = models.ManyToManyField('Product', blank=True, limit_choices_to={'category': DIScategory})
    # DISdsct_prct = models.FloatField(default=0,
    #                                  validators=[MinValueValidator(0), MaxValueValidator(100)],
    #                                  verbose_name=('discount percent'))

    # def __str__(self):
    #     return f"Discount {self.pk}"
    

class ProductAlternative(models.Model):
    PALTRproduct = models.ForeignKey(Product, on_delete=models.CASCADE,
                                   verbose_name=('Product'))
    PALTRalternative = models.ManyToManyField(Product,
                                              related_name=('product_alternatives'))
    
    def __str__(self) -> str:
        return str(self.PALTRproduct)
    
    class Meta:
        verbose_name = ('Product alternative')
        verbose_name_plural = ('Products alternative')


