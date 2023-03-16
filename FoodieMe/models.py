from django.db import models

# Create your models here.

class restaurantes(models.Model):

    def __str__(self):

        return f"Nombre del Restaurante: {self.nombre_restaurante} || Tipo de Restaurante: {self.tipo_restaurante}"

    nombre_restaurante = models.CharField(max_length=60)
    direccion_calle = models.CharField(max_length=60)
    direccion_altura = models.IntegerField()
    direccion_ciudad = models.CharField(max_length=60)
    fecha_inicio_act = models.DateField(default="0000-00-00")
    tipo_restaurante = models.CharField(max_length=60)

class experiencias(models.Model):

    def __str__(self):

        return f"Nombre del Restaurante: {self.nombre_restaurante_exp} || Calificación de Experiencia: {self.calificación_experiencia}"

    nombre_restaurante_exp = models.CharField(max_length=60)
    nombre_foodie = models.CharField(max_length=30)
    apellido_foodie = models.CharField(max_length=30)
    email_foodie = models.EmailField()
    fecha_experiencia = models.DateField(default="0000-00-00")
    calificación_experiencia = models.IntegerField()
    comentarios_experiencia = models.CharField(max_length=240)

# class Profesor(models.Model):
#     nombre = models.CharField(max_length=30)
#     apellido = models.CharField(max_length=30)
#     email = models.EmailField()
#     profesion = models.CharField(max_length=30)

# class Entregable(models.Model):
#     nombre = models.CharField(max_length=30)
#     fechaDeEntrega = models.DateField(default="00/00/0000")  
#     entregado = models.BooleanField()