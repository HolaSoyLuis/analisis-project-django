from django import forms
#from django import forms.ModelForm
from .models import habitacion,cliente,registro

class habitacionForm(forms.ModelForm):
	class Meta:
		model = habitacion
		fields = '__all__'

class clienteForm(forms.ModelForm):
	class Meta:
		model = cliente
		fields = '__all__'

class registroForm(forms.ModelForm):
	class meta:
		model = registro
		fields = '__all__'

