from urllib.parse import urlparse
from .views import LoginView
from django.urls import path, include

# Set the app name for namespacing
app_name = "accounts"


urlpatterns = [
   path("login/", LoginView.as_view(), name= "login")

]