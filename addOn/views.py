from django.shortcuts import render
from django.views.generic import TemplateView, CreateView

from addOn.models import ContactUsModel, LoginModel, RegModel
from addOn.forms import ContactUsForm, LoginForm, RegForm


# Create your views here.


class AboutUsPageView(TemplateView):
    template_name = 'aboutus.html'


class CreateContactView(CreateView):
    template_name = 'contactus.html'
    model = ContactUsModel
    form_class = ContactUsForm
    success_url = '/'


class HomePageView(TemplateView):
    template_name = 'home.html'


class LoginPageView(CreateView):
    template_name = 'login.html'
    model = LoginModel
    form_class = LoginForm
    success_url = '/'


class RegPageView(CreateView):
    template_name = 'reg.html'
    model = RegModel
    form_class = RegForm
    success_url = '/'


class DemoPageView(TemplateView):
    template_name = 'demo.html'
