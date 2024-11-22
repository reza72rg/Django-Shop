from urllib.parse import urlparse
from .views import (
    IndexViews,
    ContactView,
    AboutView,

)
from django.urls import path, include

# Set the app name for namespacing
app_name = "home"


urlpatterns = [
    path("", IndexViews.as_view(), name= "index"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("about/", AboutView.as_view(), name="about"),

]