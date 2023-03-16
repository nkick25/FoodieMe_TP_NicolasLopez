from django import forms
from django.contrib.auth.forms import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User

class crear_restaurante(forms.Form):
    nombre_restaurante = forms.CharField()
    direccion_calle = forms.CharField()
    direccion_altura = forms.IntegerField()
    direccion_ciudad = forms.CharField()
    fecha_inicio_act = forms.DateField()
    tipo_restaurante = forms.CharField()

class crear_experiencia(forms.Form):

    nombre_restaurante_exp = forms.CharField()
    nombre_foodie = forms.CharField()
    apellido_foodie = forms.CharField()
    email_foodie = forms.EmailField()
    fecha_experiencia = forms.DateField()
    calificación_experiencia = forms.IntegerField()
    comentarios_experiencia = forms.CharField()

class usuario_registro(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label = "Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label = "Repetir la contraseña", widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = ["username", "email", "first_name", "last_name", "password1", "password2"]
