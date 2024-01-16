from django.shortcuts import render
from . import models
def home(request):
    categories = models.Category.objects.all()
    return render(request, 'home.html', {
        'categories': categories
    })

def about(request):
    return render(request, 'about_us.html')


def func_category(request, category_name):
    category = models.Category.objects.get(CATcat=category_name)
    products = models.Product.objects.filter(PDCTcateg= category)
    

    return render(request, 'category_page.html', {
        'products':products,
        'category_name':category_name,
    })









# Create your views here.
