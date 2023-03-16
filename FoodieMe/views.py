from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from FoodieMe.models import *
from FoodieMe.forms import *
# import datetime

### Login

def iniciar_sesion(request):
    if request.method == "POST":

        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get("username")
            contraseña = form.cleaned_data.get("password")

            user = authenticate(username=usuario, password=contraseña)

            if user:

                login(request, user)

                return render(request, "FoodieMe/inicio.html", {"mensaje1":f"Bienvenido al sitio FoodieMe{usuario}"})
                                                                
        else:

            return render(request, "FoodieMe/login_error.html", {"mensaje2":f"El Usuario y-o es incorrecto, reintentar!"})

    else:
        
        form = AuthenticationForm()

        return render(request, "FoodieMe/login.html", {"formulario":form})


def iniciar_sesion_error(request):

    return render(request, "FoodieMe/login_error.html")


def registro_usuario(request):

    if request.method == "POST":

        form = usuario_registro(request.POST)

        if form.is_valid():
            
            username =form.cleaned_data["username"]
            form.save()
            return render(request, "FoodieMe/inicio.html", {"mensaje3":"Usuario creado"})
        
    else:

        form = usuario_registro()

    return render(request, "FoodieMe/registro.html", {"formulario":form})

### Vista de paginas y sub-paginas

def inicio(request):

    return render(request, "FoodieMe/inicio.html")

def about_me(request):

    return render(request, "FoodieMe/about_me.html")

def construccion(request):

    return render(request, "FoodieMe/construccion.html")

def Admin(request):

    return render(request, "FoodieMe/admin.html")

def home_restaurantes(request):

    return render(request, "FoodieMe/restaurantes.html")

def home_experiencias(request):

    return render(request, "FoodieMe/experiencias.html")


### Create

def alta_restaurante(request):

    if request.method == 'POST':

        formulario1 = crear_restaurante(request.POST)

        if formulario1.is_valid():

            info = formulario1.cleaned_data

            resto = restaurantes(nombre_restaurante=info['nombre_restaurante'], direccion_calle=info['direccion_calle'], direccion_altura=info['direccion_altura'], direccion_ciudad=info['direccion_ciudad'], fecha_inicio_act=info['fecha_inicio_act'], tipo_restaurante=info['tipo_restaurante'])

            resto.save()

            return render(request, "FoodieMe/inicio.html")
    
    else:

        formulario1 = crear_restaurante()

    return render(request, "FoodieMe/alta_restaurante.html", {"form1":formulario1})

def alta_experiencia(request):

    if request.method == "POST":

        formulario2 = crear_experiencia(request.POST)

        if formulario2.is_valid():

            info = formulario2.cleaned_data

            exp = experiencias(nombre_restaurante_exp=info["nombre_restaurante_exp"], nombre_foodie=info["nombre_foodie"], apellido_foodie=info["apellido_foodie"], email_foodie=info["email_foodie"], fecha_experiencia=info["fecha_experiencia"], calificación_experiencia=info["calificación_experiencia"], comentarios_experiencia=info["comentarios_experiencia"])

            exp.save()

            return render(request, "FoodieMe/inicio.html")
    
    else:

        formulario2 = crear_experiencia()

    return render(request, "FoodieMe/alta_experiencia.html", {"form2":formulario2})

### Read

def leer_restaurantes(request):

    lista_restaurantes = restaurantes.objects.all()

    contexto = {"Restaurantes": lista_restaurantes}

    return render(request, "FoodieMe/leer_restaurantes.html", contexto)

### Read

def leer_experiencias(request):

    lista_experiencias = experiencias.objects.all()

    contexto = {"Experiencias": lista_experiencias}

    return render(request, "FoodieMe/leer_experiencias.html", contexto)

### Delete

def eliminar_restaurantes(request, restonombre):

    resto_borrar = restaurantes.objects.get(nombre_restaurante=restonombre)
    resto_borrar.delete()

    lista_restaurantes = restaurantes.objects.all()

    contexto = {"Restaurantes":lista_restaurantes}

    return render(request, "FoodieMe/leer_restaurantes.html", contexto)

### Update

def actualizar_restaurantes(request, restonombre):

    resto_act = restaurantes.objects.get(nombre_restaurante=restonombre)
    
    if request.method == "POST":

        formulario1 = crear_restaurante(request.POST)

        if formulario1.is_valid():

            info = formulario1.cleaned_data

            resto_act.nombre_restaurante=info['nombre_restaurante']
            resto_act.direccion_calle=info['direccion_calle']
            resto_act.direccion_altura=info['direccion_altura']
            resto_act.direccion_ciudad=info['direccion_ciudad']
            resto_act.fecha_inicio_act=info['fecha_inicio_act']
            resto_act.tipo_restaurante=info['tipo_restaurante']

            resto_act.save()

            return render(request, "FoodieMe/inicio.html")
    
    else:

            formulario1 = crear_restaurante(initial={"nombre_restaurante":resto_act.nombre_restaurante,"direccion_calle":resto_act.direccion_calle, "direccion_altura":resto_act.direccion_altura,"direccion_ciudad":resto_act.direccion_ciudad,"fecha_inicio_act":resto_act.fecha_inicio_act,"tipo_restaurante":resto_act.tipo_restaurante})

    return render(request, "FoodieMe/editar_restaurantes.html", {"form1":formulario1, "nombre_restaurante":restonombre})



### CRUD por Clases

class lista_restaurantes(ListView):

    model = restaurantes

class detalle_restaurantes(DetailView):

    model = restaurantes

class crear_resto(CreateView):

    model = restaurantes
    success_url = "FoodieMe/restaurantes/list"
    fields = ["nombre_restaurante", "direccion_calle", "direccion_altura", "direccion_ciudad", "fecha_inicio_act", "tipo_restaurante"]

class actualizar_resto (UpdateView):

    model = restaurantes
    success_url = "FoodieMe/restaurantes/list"
    fields = ["nombre_restaurante", "direccion_calle", "direccion_altura", "direccion_ciudad", "fecha_inicio_act", "tipo_restaurante"]

class borrar_resto(DeleteView):

    model = restaurantes