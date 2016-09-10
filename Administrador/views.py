from django.shortcuts import render
from django.views.generic import ListView, 
from .forms import RegistrationForm

# Create your views here.


class Panel(ListView):
    def get(self, request):
        template_name = "Administrador/panel.html"
        context = {}
        return render(request, template_name, context)

class Registro(View):
	def get (self,request):
		template_name = "Administrador/Registro.html"
		context={
		'from':form,
		}
		return render(request, template_name,context)
		