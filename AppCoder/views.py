from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import *
from AppCoder.forms import *

# Create your views here.

'''
def curso(self):

    curso = Curso(nombre = 'Django', comision = 939393)
    curso.save()
    texto = f"Curso creado: {curso.nombre} {curso.comision}"

    return HttpResponse(texto)

def cursos(request):
    return render (request, 'AppCoder/cursos.html')

def profesores(request):
    return render (request, 'AppCoder/profesores.html')

def estudiantes(request):
    return render (request, 'AppCoder/estudiantes.html')

def entregables(request):
    return render (request, 'AppCoder/entregables.html')

  
def curso_formulario(request): 

    if (request.method=='POST'):
            nombre = request.POST.get("curso")
            comision = request.POST.get("comision")
            curso= Curso(nombre=nombre, comision=comision)
            curso.save()
            
            return render (request, "AppCoder/curso_formulario.html")   

    return render(request, "AppCoder/curso_formulario.html")   VISTA PARA FORMULARIOS HTML
    
'''

def inicio(request):
    return render (request, 'AppCoder/inicio.html')


def curso_form(request):

    if (request.method == "POST"):     #Cuando el request es por POST (manda algo)
        form =Curso_Form(request.POST) #Crea un formulario llamado "form"
        print(form)
        if form.is_valid():            #Si lo que se ingreso en el formulario es valido, corre:
            info = form.cleaned_data   #Obten los valores de lo ingresado en el cuadro de texto y los guarda en un dicc llamado "info"
            print(info)
            nombre= info["nombre"]     #de info saca el valor de "nombre" - Recordemos que "nombre" es uno de los valores de nuestro form
            comision= info["comision"] #de info saca el valor de "comision" - Recordemos que "comision" es uno de los valores de nuestro form
            curso = Curso(nombre=nombre, comision=comision)  #Creamos un objeto del modelo Curso con las variable que sacamos arriba
            curso.save()               #FGuardamos el objeto en nuetra DB
            return render(request, "AppCoder/inicio.html") #Renderiza la html inicio

    else: # Cuando el request es por GET (Ingresé mi URL y le di enter en la barra de navegacion, pidiendo (GET) algo)
        form= Curso_Form()  #Crea un formulario llamado "form" de la clase Curso_Form, aka, tiene nombre y comision - Este es un diccionario
    return render(request, "AppCoder/cursos.html", {"formulario":form})  #renderiza la pagina, usando el "form" como context
    #Django hace todo el trabajo de html al usar los fomrs.py

def profesor_form(request):

    if (request.method == "POST"):     
        form =Profesor_Form(request.POST) 
        print(form)
        if form.is_valid():            
            info = form.cleaned_data   
            print(info)
                        
            nombre= info["nombre"]
            apellido= info["apellido"]
            email= info["email"]
            profesion= info["profesion"]
            
            profesor = Profesor(nombre=nombre, apellido=apellido, email=email, profesion=profesion)  
            profesor.save()               
            return render(request, "AppCoder/inicio.html") 

    else: 
        form= Profesor_Form()  
    return render(request, "AppCoder/profesores.html", {"formulario":form})


def estudiante_form(request):

    if (request.method == "POST"):     
        form =Estudiante_Form(request.POST) 
        print(form)
        if form.is_valid():            
            info = form.cleaned_data   
            print(info)
                        
            nombre= info["nombre"]
            apellido= info["apellido"]
            email= info["email"]
            
            
            estudiante = Estudiante(nombre=nombre, apellido=apellido, email=email)  
            estudiante.save()               
            return render(request, "AppCoder/inicio.html") 

    else: 
        form= Estudiante_Form()  
    return render(request, "AppCoder/estudiantes.html", {"formulario":form})  



def entregable_form(request):

    if (request.method == "POST"):     
        form =Entregable_Form(request.POST) 
        print(form)
        if form.is_valid():            
            info = form.cleaned_data   
            print(info)
                        
            nombre= info["nombre"]
            fechaDeEntrega= info["fechaDeEntrega"]
            entregado= info["entregado"]
            
            
            entregable = Entregable(nombre=nombre, fechaDeEntrega=fechaDeEntrega, entregado=entregado)  
            entregable.save()               
            return render(request, "AppCoder/inicio.html") 

    else: 
        form= Entregable_Form()  
    return render(request, "AppCoder/entregables.html", {"formulario":form})  
    

def busqueda_comision(request):

    return render(request, "AppCoder/form_busqueda_comision.html")


def buscar(request):

    if request.GET['comision']:                        #Si me trajo algo en comision, filtra la DB y renderiza los resultados en una html
        comi=request.GET['comision']
        cursos = Curso.objects.filter(comision=comi)  #En mi modelo Curso, en los objetos, filtra lo que en el atributo 'comision'
                                                          # tenga lo que jale (get) del request desde la web
                                                          # OSEA, En mi tabla Curso de la DB, busca en los registros (objetos) que en la columna 'comision' tenga lo de la var 'comision'

        # cursos es una lista de los objetos cursos que coinciden con la condicion del filter. Si no hay ninguno, trae una lista vacia

        return render(request, 'AppCoder/resultados_busqueda.html', {'cursos':cursos})  ## Renderiza una html donde me muestre los resultados que encontro
        #return render(request, 'AppCoder/form_busqueda_comision.html', {'cursos':cursos})

    else: # request.GET['variable'] es 1 cuando var!= vacio, por tanto, cuando var = vacio, da false y se ejecuta este else
        return render(request, 'AppCoder/form_busqueda_comision.html', {'error': 'No se ingreso ninguna comision'})



'''
    comision=request.GET.get('comision')
    respuesta = f'Estoy buscando la camada numero: {comision}'
    return HttpResponse(respuesta)
'''
