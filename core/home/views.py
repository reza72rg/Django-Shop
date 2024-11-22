from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.



class IndexViews(TemplateView):
    template_name = "home/index.html"


class ContactView(TemplateView):
    template_name = "home/page-contact.html"


class AboutView(TemplateView):
    template_name = "home/page-about.html"