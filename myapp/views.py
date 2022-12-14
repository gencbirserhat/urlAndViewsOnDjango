from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect, HttpResponseNotFound 
from django.urls import reverse
data = {
    "telefon":"telefon kategorisindeki ürünler",
    "bilgisayar":"bilgisayar kategorisindeki ürünler",
    "elektronik":"elektronik kategorisindeki ürünler"
}

def index(request):
    list_items = ""
    category_list = list(data.keys())
    
    for category in category_list:
        redirect_path = reverse("products_by_category", args=[category])
        list_items += f"<li><a href=\"{redirect_path}\">{category}</a></li>"   
          
    html = f"<ul>{list_items}</ul>"
    return HttpResponse(html)

def details(request):
    return HttpResponse("details")

def lists(request):
    return HttpResponse("list")

def getProductsByCategoryId(request, category_id):
    
    category_list = list(data.keys())
    if category_id > len(category_list):
        return HttpResponseNotFound("kategori bulunamadı")
    else:
        category_name = category_list[category_id-1]
        redirect_path = reverse("products_by_category", args=[category_name])
        return HttpResponseRedirect(redirect_path)
    
def getProductsByCategory(request, category):
    try:
        text = data[category]
        return HttpResponse(f"<h1>{text}</h1>")
    except:
        return HttpResponseNotFound("<h1>kategori bulunamadı</h1>")

