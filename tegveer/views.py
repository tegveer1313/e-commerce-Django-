from django.shortcuts import render
from .models import Product, Product2, bags
from django.http import HttpResponse
from collections import OrderedDict

def index(request):
    products = Product.objects.all()
    n = len(products)
    params={'product': products}
    print(params)
    return render(request, "index.html", params)


def about(request):
    return render(request, "about.html")

def shoes(request):
    prod = Product2.objects.all()
    n = len(prod)
    params2={'product': prod}
    return render(request, "Shoes.html", params2)

def Bags(request):
    bag = bags.objects.all()
    n = len(bag)
    params2={'product': bag}
    return render(request, "bags.html", params2)

def contact(request):
    if request.method == 'POST':
     email = request.POST.get("email", None)
     print(email)
    return render(request, "contact.html")

def tracker(request):
    return HttpResponse("We are at tracker")

def search(request):
    return HttpResponse("We are at search")

def productView(request, myid):
    product=Product.objects.filter(id=myid)
    prod=Product2.objects.filter(id=myid)
    print(product)
    print(prod)
    return render(request, "productlayout.html", {'product':product[0], 'prod':product[0]})

def prodView(request, myid):
    prod=Product2.objects.filter(id=myid)
    print(prod)
    return render(request, "shoeslayout.html", {'prod':prod[0]})

def bagsView(request, myid):
    bag=bags.objects.filter(id=myid)
    print(bag)
    return render(request, "bagslayout.html", {'bags':bag[0]})

def checkout(request):
    return HttpResponse("We are at checkout")
