from django.views.generic import TemplateView
from django.shortcuts import render

# Create your views here.



class ShopProductListView(TemplateView):
    template_name = "shop/products-list.html"



class ShopProductGridView(TemplateView):
    template_name = "shop/products-grid.html"