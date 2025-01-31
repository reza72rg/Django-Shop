from django.urls import path, include
from .views import (
    SessionAddProduct,
    CartSummaryView,
    SessionRemoveProductView,
    SessionUpdateProductQuantityView,
    )
# Set the app name for namespacing
app_name = "cart"


urlpatterns = [
    path("session/add_product/", SessionAddProduct.as_view(), name="session_add_product"),
    path("session/remove-product/",SessionRemoveProductView.as_view(),name="session-remove-product"),
    path("session/update-product-quantity/",SessionUpdateProductQuantityView.as_view(),name="session-update-product-quantity"),
    path("summary/", CartSummaryView.as_view(), name="cart_summary"),

]