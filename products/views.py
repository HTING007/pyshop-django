from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Product


def index(request):
    products = Product.objects.all()
    return render(request, 'index.html',
                  {'products':products})

def new(request):
    return HttpResponse('New product')

def detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'detail.html', {'product': product})

def index(request):
    query = request.GET.get('q')

    if query:
        products = Product.objects.filter(name__icontains=query)
    else:
        products = Product.objects.all()

    return render(request,'index.html',{
        'products': products,
        'query': query
    })

def index(request):
    category = request.GET.get('category')
    products = Product.objects.all()

    if category:
        products = products.filter(category=category)

    return render(request,'index.html',{
        'products': products,
        'category': category
    })