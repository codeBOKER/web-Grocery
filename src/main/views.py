from django.shortcuts import render
from . import models
def home(request):
    categories = models.Category.objects.all()
    return render(request, 'Home Page.html', {
        'categories': categories
    })

def about(request):
    return render(request, 'About Us.html')


def func_category(request, category_name):
    category = models.Category.objects.get(CATcat=category_name)
    products = models.Product.objects.filter(PDCTcateg= category)
    

    return render(request, 'Category Page.html', {
        'products':products,
        'category_name':category_name,
    })



def best_deals(request):
    return render(request, 'Best Deals.html')





# Create your views here.
