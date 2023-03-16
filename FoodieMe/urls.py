from django.urls import path
from django.contrib import admin
from FoodieMe import views
from django.urls import include
from django.contrib.auth.views import LogoutView

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('Appcoder/', include('Appcoder.urls'),
    # path('inicio/', views.inicio, name="inicio"),
    # path('cursos/', views.curso, name="cursos"),
    # path('estudiantes/', views.estudiante, name="estudiantes"),
    # path('profesores/', views.profesor, name="profesores"),
    # path('entregables/', views.entregable, name="entregables"),
    # path('curso_formulario/', views.curso_form, name="curso_formulario"),
    # path('estudiante_formulario/', views.estudiante_form, name="estudiante_formulario"),
    # path('profesor_formulario/', views.profesor_form, name="profesor_formulario"),
    # path('entregable_formulario/', views.entregables_form, name="entregable_formulario"),
    # path('busqueda_camada/',  views.busqueda_camada, name="busqueda_camada"),
    # path('resultados_camada/', views.resultados,name="resultados_camada"),
    # path('admin/', admin.site.urls),
    # path('admin/', include('Comidas.urls'),
    path('', views.inicio, name="inicio"),
    path('admin/', views.Admin, name="admin"),
    path('home_restaurantes/',views.home_restaurantes, name="restaurantes"),
    path('home_experiencias/',views.home_experiencias, name="experiencias"),
    path('about_me/',views.about_me, name="about_me"),
    path('construccion/',views.construccion, name="construccion"),
    path('login/',views.iniciar_sesion, name="login"),
    path('login_error/',views.iniciar_sesion_error, name="login_error"),
    path('registro/',views.registro_usuario, name="registro"),
    path("logout", LogoutView.as_view(template_name="FoodieMe/logout.html"), name="logout"),

    ###  CRUD
    path('alta_restaurante/',views.alta_restaurante, name="alta_restaurante"),
    path('leer_restaurantes/',views.leer_restaurantes, name="leer_restaurantes"),
    path('alta_experiencia/',views.alta_experiencia, name="alta_experiencia"),
    path('leer_experiencias/',views.leer_experiencias, name="leer_experiencias"),
    path('eliminar_restaurantes/<restonombre>/',views.eliminar_restaurantes, name="eliminar_restaurantes"),
    path('editar_restaurantes/<restonombre>/',views.actualizar_restaurantes, name="editar_restaurantes"),
]