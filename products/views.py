from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.
def product_list(request):
    products = Product.objects.all()
    return render(request, "courses.html", {"products": products})
    
def do_search(request):
    products = Product.objects.filter(name__icontains=request.GET['q'])
    return render(request, "classes.html", {"products": products})

