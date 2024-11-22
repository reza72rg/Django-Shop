from tempfile import template

from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    )
from django.shortcuts import render
from .models import ProductModel, ProductStatusType, ProductCategoryModel


# Create your views here.



class ShopProductListView(ListView):
    template_name = "shop/products-list.html"


    def get_queryset(self):
        return  ProductModel.objects.filter(status=ProductStatusType.publish.value)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['total_items']  = self.get_queryset().count()
        return context



class ShopProductGridView(ListView):
    template_name = "shop/products-grid.html"
    paginate_by = 6

    def get_paginate_by(self, queryset):
        return self.request.GET.get('page_size', self.paginate_by)

    def get_queryset(self):
        return  ProductModel.objects.filter(status=ProductStatusType.publish.value)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_items"] = self.get_queryset().count()

        context["categories"] = ProductCategoryModel.objects.all()
        return context


class ShopProductDetailsView(DetailView):
    template_name = "shop/product-detail.html"
    queryset = ProductModel.objects.filter(
        status=ProductStatusType.publish.value)

