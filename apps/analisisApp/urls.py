"""myPage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
#from .views import vistaPrincipal,vistaEstudiante,listaEstudiante,vistaEstudianteAdministrador,listaEstudianteAdministrador,vistaArticulo,listaArticulo,vistaComentario,listaComentario,LoginView,vistaVideo
<<<<<<< HEAD
from .views import vistaPrincipal,vistaHabitacion,listaHabitacion,vistaCliente,listaCliente,LoginView,CrearUsuarioView,EditarCliente,EditarHabitacion,vistaRegistro,listaRegistro
=======
from .views import EliminarHabitacionView,vistaPrincipal,vistaHabitacion,listaHabitacion,vistaCliente,listaCliente,LoginView,CrearUsuarioView
>>>>>>> 9341be64cd0dc4cbc49e168e200c507bd10f5d32
from django.contrib.auth.views import login,logout

urlpatterns = [
	url(r'^$', vistaPrincipal.as_view()),
	url(r'^principal$', vistaPrincipal.as_view(), name = 'principal'),
    url(r'^login$', LoginView.as_view(), name = 'login'),
    
	url(r'^habitacion$', vistaHabitacion.as_view(), name = 'habitacion'),
    url(r'^listaHabitacion$', listaHabitacion.as_view(), name = 'listaHabitacion'),
    url(r'^EliminarHabitacion/(?P<pk>\d+)/$', EliminarHabitacionView.as_view(), name = 'EliminarHabitacion'),

    

    url(r'^cliente$', vistaCliente.as_view(), name = 'cliente'),
    url(r'^listaCliente$', listaCliente.as_view(), name = 'listaCliente'),

    url(r'^accounts/logout/$', logout, name = 'logout'),

    url(r'^CrearUsuario$', CrearUsuarioView.as_view(), name = 'CrearUsuario'),


    #updates
    url(r'^EditarCliente/(?P<pk>\d+)/', EditarCliente.as_view(), name = 'EditarCliente'),
    url(r'^EditarHabitacion/(?P<pk>\d+)/', EditarHabitacion.as_view(), name = 'EditarHabitacion'),


    #registro
    url(r'^registro$', vistaRegistro.as_view(), name = 'registro'),
    url(r'^listaRegistro$', listaRegistro.as_view(), name = 'listaRegistro'),
]
