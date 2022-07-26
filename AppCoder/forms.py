from socket import fromshare
from django import forms


class Curso_Form(forms.Form):
    nombre = forms.CharField(max_length=50)
    comision = forms.IntegerField()

class Profesor_Form(forms.Form):
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()
    profesion= forms.CharField(max_length=30)

class Estudiante_Form(forms.Form):  
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()

    
class Entregable_Form(forms.Form):
    nombre= forms.CharField(max_length=30)
    fechaDeEntrega = forms.DateField()  
    entregado = forms.BooleanField()