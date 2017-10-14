#para el logueo de los usuarios
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login
from django.views.generic import FormView
#estas tres lineas

from django.contrib.auth.models import User


from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,ListView,DeleteView
from .models import habitacion,cliente
from .forms import habitacionForm,clienteForm
# Create your views here.

class vistaPrincipal(TemplateView):
	template_name = 'principal.html'

#habitacion
class vistaHabitacion(CreateView):
	template_name = 'habitacion.html'
	form_class =  habitacionForm
	success_url = reverse_lazy('analisis:principal')

class listaHabitacion(ListView):
	template_name = 'listaHabitacion.html'
	model = habitacion

	def get_queryset(self):
		return habitacion.objects.all()
#end habitacion

#cliente
class vistaCliente(CreateView):
	template_name = 'cliente.html'
	form_class =  clienteForm
	success_url = reverse_lazy('analisis:principal')

class listaCliente(ListView):
	template_name = 'listaCliente.html'
	model = cliente

	def get_queryset(self):
		return cliente.objects.all()
#end cliente

#login
class LoginView(FormView):
	template_name = 'login.html'
	form_class = AuthenticationForm
	success_url = reverse_lazy('analisis:principal')

	def form_valid(self, form):
		login(self.request, form.get_user())
		return super(LoginView, self).form_valid(form)

class vistaVideo(TemplateView):
	template_name = 'video.html'
#end logout

#create user
class CrearUsuarioView(CreateView):
	model = User
	template_name = 'CrearUsuario.html'
	form_class = UserCreationForm
	success_url = reverse_lazy('analisis:principal')


class EliminarHabitacionView(DeleteView):
	template_name = 'eliminar.html'
	model = habitacion
	success_url = reverse_lazy('analisis:principal')
	
#end create user
'''
usuario:	jennifer
contrasena:	aimeaime
e-mail:		jennifer@gmail.com
e-mail:		luis17velasquez@gmail.com
''' 