from urllib.parse import urlparse
from .views import (
    ShopProductListView,
    ShopProductGridView,

    )
from django.urls import path, include

# Set the app name for namespacing
app_name = "shop"


urlpatterns = [
    path("product/list/", ShopProductListView.as_view(), name="product_list"),
    path("product/grid/",ShopProductGridView.as_view(),name="product_grid"),

]