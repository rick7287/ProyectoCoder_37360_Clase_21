# CLASE 20 - Playground Intermedio Parte 2

## Herencia de Templates

Usar de base determiadas cosas que estaran en todas nuestros templates.

1. Crear untemplate "padre.html". Este servira como el "template" de nustros otros templates. Aqui pondremos todos los estilos y elementos de diseño web que nuestra app/pagina va a tener en comun

2. Dentro de padre.html crear un bloque de codigo

        {% block Contenido_que_cambia %}

        {% endblock %}

    Este block es el espacio al que vamos a hacer referencia en nuestros otros templates/htmls y donde se vera el contenido particular de cada pagina

3. En nuestros templates (cursos, entregables, etc etc) borraremos todo el codigo de estilos y demas que ya vienen incluidos en padre.html. Estos son los templates "hijos"

4. Dentro de cada hijo creamos y ponemos este bloque de codigo:

        {% extends "AppCoder/padre.html" %} - Esta es la ubicacion y nombre de nuestro padre

        {% load static %} - Cargamos los static

        {% block Contenido_que_cambia %} - Nombre del bloque html donde se desplegara el contenido en el template padre

        <h1>ES UN BLOQUE</h1> - Nuestro codigo html

        {% endblock %}

5. Esto lonpodemos hacer con varios blocks de codigo, como titulos, por ejemplo:

        {% block titulo %}

        {% endblock %}

    Y lo unico que hacemos es crear varios bloques dentro del template padre que luego personalizamos en los hijos


## Navegacion entre templates desde la WEB

Vamos a crear un menu en nuestro template padre.html

1. Dentro del codigo de padre.html, ubicaremos el boton Sign Up que es parte de nuestro diseño web y lo vamos a repetir varias veces, una para cada template (cursos, estudiantes, etc)

2. La parte href= es a donde me lleva el link del boton

3. En Django, la url destino se escribe:

        {% url 'name' %}

    donde name es el name que definiremos en nuestro urls.py para cada path.

        urlpatterns = [
    
        path('curso/', curso, name='curso'),
        path('cursos/', cursos, name='cursos'),
        path('profesores/', profesores, name='profesores'),
        path('estudiantes/', estudiantes, name='estudiantes'),
        path('entregables/', entregables, name='entregables'),
        path('', inicio, name='inicio'),
        
        ]

4. Con esto tendremos un panel de navegacion que nos llevara a cada una de las paginas de nuestras vistas.

## Panel de administracion

### Creacion de Superusuario

1. Para acceder a nuestro panel de administracion en Django, usamos /admin en la url. Esta pagina de admin nos pedira un user y password

2. Para crear nuestras credenciales, paramos el server si esta corriendo, y desde la consola ejecutamos:

        python manage.py createsuperuser

3. Introducimos el username, email y password

4. Volvemos a correr el server y a cargar la pagina. Al loggearnos, podremos ver Groups y Users

### Dar de alta nuestro panel de Administracion

Esto nos permitira dar de alta nuestras paginas y modelos para administrar el flujo de datos desde la web

1. Importamos los modelos de nuestra app en el archivo admin.py de la misma app.

        from models import *   -- Importamos todos los modelos

2. Registramos los modelos en admin.py usando admin.site.register(model) donde model es el nombre del MODELO (de models.py)

        from .models import *

        # Register your models here.

        admin.site.register(Profesor)
        admin.site.register(Curso)
        admin.site.register(Estudiante)
        admin.site.register(Entregable)

3. Al loggear en la pagina de admin, ya podremos ver nuestros modelos cargados. Al hacer click en ellos, debemos poder ver los objetos(registros) que hay dentro de cada modelo (tabla de mi DB)

4. Recordando que los modelos se definen como clases, podemos agregar los metodos especiales de clases. Por ejemplo,:

        def __str__(self):
            return self.nombre + " " + str(self.comision)

    Este metodo le define como se imnprime mi clase (ya sea desde un print() o cuando se renderiza/visualiza en el navegador con Django SOLO dentro de mi admin page)

5. Ahora podemos agregar, modificar o eliminar registros (objetos) a cada modelo (tabla de la DB)

6. Tambien desde el panel de admin, podemos crear, modificar o eliminar usuarios.

    - El admins de users nos permote agregar informacion personal
    - El password se muestra encriptado
    - Puedo modificar sus permisions
    - etc etc

