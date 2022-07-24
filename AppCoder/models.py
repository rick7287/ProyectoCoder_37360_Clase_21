from django.db import models

# Create your models here.

class Curso(models.Model):
    nombre = models.CharField(max_length=50)
    comision = models.IntegerField()

    def __str__(self):
            return self.nombre + " " + str(self.comision)

class Estudiante(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()

    def __str__(self):
            return self.nombre + " " + str(self.apellido)

class Profesor(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
    profesion= models.CharField(max_length=30)

    def __str__(self):
            return self.nombre + " " + str(self.apellido)

class Entregable(models.Model):
    nombre= models.CharField(max_length=30)
    fechaDeEntrega = models.DateField()  
    entregado = models.BooleanField()

    def __str__(self):
            return self.nombre + " Vence: " + str(self.fechaDeEntrega)