from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.


class Home(ListView):
    def get(self, request):
        template_name = "Principal/home.html"
        context = {}
        return render(request, template_name, context)

class About(ListView):
    def get(self, request):
        template_name="Principal/about.html"
        context= {}
        return render(request, template_name, context)

# Create your views here.
