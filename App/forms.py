from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Files_up


class CustomUser(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email', 'password1','password2']

class FilesForm(forms.ModelForm):
	class Meta:
		model = Files_up
		fields = ('Nombre_archivo', 'Descarga_archivo')

class SelectFile(forms.Form):
	nombre_analisis = forms.CharField(max_length = 100)
	seleccionar_archivo = forms.ModelChoiceField(queryset=Files_up.objects.all())