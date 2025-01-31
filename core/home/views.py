from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from cart.cart import CartSession
# Create your views here.



class IndexViews(View):
    template_name = "home/index.html"

    def get(self, request):
        cart = CartSession(request.session)
        context = {
            "cart": cart
        }
        return render(request, self.template_name, context)


class ContactView(TemplateView):
    template_name = "home/page-contact.html"


class AboutView(TemplateView):
    template_name = "home/page-about.html"