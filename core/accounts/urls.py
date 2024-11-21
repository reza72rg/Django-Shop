from django.urls import path, include
from .views import LoginView, LogoutView


# Set the app name for namespacing
app_name = "accounts"


urlpatterns = [
   path("login/", LoginView.as_view(), name= "login"),
   path("logout/", LogoutView.as_view(), name= "logout"),

]