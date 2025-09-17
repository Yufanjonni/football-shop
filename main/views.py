from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render, redirect, get_object_or_404
from main.models import Product
from main.forms import ProductForm
def show_main(request):
    product_list = Product.objects.all()
    context = {
        'store_name' : 'Ryan Rapopo',
        'name' : 'Muhammad Yufan Jonni',
        'npm' : '2406408602',
        'class' : 'PBP A',
        'product_list' : product_list
    }
    return render(request, "main.html", context)

def add_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')
    
    context = {'form' : form}
    return render(request, "add_product.html", context)

def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)

    context = {'product' : product}

    return render(request, "product_detail.html", context)

def show_xml(request):
    product_list = Product.objects.all()
    xml_data = serializers.serialize("xml", product_list)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    product_list = Product.objects.all()
    json_data = serializers.serialize("json", product_list)
    return HttpResponse(json_data, content_type="application/json")

def show_xml_by_id(request, product_id):
    try:
        product_item = Product.objects.filter(pk=product_id)
        xml_data = serializers.serialize("xml", product_item)
        return HttpResponse(xml_data, content_type="application/xml")
    except:
        return HttpResponse(status=404)

def show_json_by_id(request, product_id):
    try:
        product_item = Product.objects.get(pk=product_id)
        json_data = serializers.serialize("json", [product_item])
        return HttpResponse(json_data, content_type="application/json")
    except:
        return HttpResponse(status=404)
# Create your views here.
