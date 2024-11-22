from urllib.parse import urlparse
from .views import (
    ShopProductListView,
    ShopProductGridView,
    ShopProductDetailsView,

    )
from django.urls import path, include

# Set the app name for namespacing
app_name = "shop"


urlpatterns = [
    path("product/list/", ShopProductListView.as_view(), name="product_list"),
    path("product/grid/",ShopProductGridView.as_view(),name="product_grid"),
    path("product/<slug:slug>/details/", ShopProductDetailsView.as_view(), name="product_details"),

]