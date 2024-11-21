from urllib.parse import urlparse
from .views import *
from django.urls import path, include

# Set the app name for namespacing
app_name = "home"


urlpatterns = [
    path("", IndexViews.as_view(), name= "index")

]