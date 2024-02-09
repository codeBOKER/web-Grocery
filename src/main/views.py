from django.shortcuts import render
from . import models
from .forms import SearchForm

def home(request):
    # search banner
    form = SearchForm(request.GET)
    results = []
    if form.is_valid():
        query = form.cleaned_data['query']
        results = models.Product.objects.filter(PDCTname__icontains=query)
        return render(request, 'search_page.html',{
            'form': form,
            'products': results,
            'query':query,
    })
    
     # put our categories
    categories = models.Category.objects.all()

    return render(request, 'home.html', {
        'form': form,
        'categories': categories,
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
