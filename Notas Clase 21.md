# CLASE 20 - Playground Intermedio Parte 3

## FORMULARIOS

- Son campos y un boton que hace algo
- Se pueden hacer con HTML con CSS
- Django nos da herramientas para hacer formularios sin mucho HTML

### Funcionamiento de formularios en este curso

El html recibe nuestra información por medio de la vista y su template asociado.  Al apretar un botón  esa información viaja por medio de un método GET o POST y llega al servidor, donde esos datos se manipulan.

### Creacion de un formulario para AppCoder con HTML

1. Vamos a las vistas, views.py y creamos una nueva.

2. Luego agregamos la vista a las urls.py

3. Creamos el html. (donde haremos el formulario)

    - En el curso_formulario.html, dentro del body, ponemos el siguiente bloque de codigo:

    ```html

            <form action="/AppCoder/curso_formulario/" method="POST">

                <p>Curso: <input type="text" name="curso"></p>
                <p>Comision: <input type="number" name="comision"></p>

                <input type="submit" value="Enviar"> 


            </form>
    ```

    Esto es HTML y lo que hace es crear un par de input text boxes con su respectivo name y un boton (type="submit"), pero el boton todavia no hace nada.

4. Adicionalmente y sin entran mucho en detalle, hay que agregar el token de validacion que Django exige. Este es para confirmarle a Django que los datos ingresados en el formulario son en efecto enviados por un formulario que nosotros creamos.

    ```html

        {% csrf_token %}

    ```

5. En la vista que creamos del curso_formulario, agregamos el siguiente bloque de codigo:

    ```python

        def curso_formularios(request): 

            if (request.method=='POST'):
                nombre = request.POST.get("curso")
                comision = request.POST.get("comision")
                curso= Curso(nombre=nombre, comision=comision)
                curso.save()
            
                return render (request, "AppCoder/inicio.html")   

            return render(request, "AppCoder/curso_formulario.html")

    ```

    Que esta pasando??

    - En nuestro urls.py, le dijimos Django que cuando le peguemos a la url AppCoder/curso_formulario/, vaya y ejecute la vista llamada curso_formularios(request):
    - La vista curso_formulario ejecuta el codigo que le pusimos con el IF:

        - Mientras no reciba un request tipo POST, ejecuta la opcion donde renderiza AppCoder/curso_formulario.html (te muestra la pagina html)

    - En el curso_formulario.html, creamos el form, el cual manda su data a traves del metodo POST
    - Uno de los cuadros de texto input se llama curso y el otro comision. Esas son mis variables donde se va a guardar lo que yo escriba
    - Al darle click al boto (submit), se manda la data por metodo POST.
    - Al recibir el request nuevamente, la el codigo de la vista evalua el motodo con el que se mando el request. Si es POST (si es, ya que asi lo definimos), ejecuta lo que esta dentro del IF
    - Guardamos en una variable 'nombre' el contenido del textbox llamado 'curso'
    - Guardamos en una variable 'comision' el contenido del textbox llamado 'comision'
    - Con mis dos variables, creo un objeto de la clase Curso, el cual me pide 'nombre' y 'comision', los cuales van a ser las variable que guarde desde el html
    - Guardo mi objeto en el modelo Curso (guardo mi registro en la tabal de la DB llamada Curso)
    - Le digo a Django que renderice la pagina de inicio (en realida le pude haber dicho que renderizara cualquiera)

---

### Creacion de un formulario para AppCoder con la API de Django

1. Creamos el archivo forms.py en la App

2. Importamos los forms.

    ```python

        from django import forms

    ```

3. Usamos una clase para crear un formulario. Usamos uno de los models, ya que el form es para ingresar data a algun model.

    ```python

        class Curso_Form(forms.Form):  #Esta heredando sus caracteristicas de la clase padre Forms, por lo que Curso_Form tambien es un formulario
            nombre = forms.CharField(max_length=50)
            comision = forms.IntegerField()

    ```

4. Agregamos el path a urls.py  --- Podemos crear el url/path despues de la vista o al final, despues del html

    ```python

        path('curso_form/', curso_form, name='curso_form'),
    ```

5. Modificamos la vista para que ya no reciba el html, sino el api forms

    - Primero importamos los formualrios con

        ```python

            from AppCoder.forms import Curso_Form
        
        ```

    - En el view de curso_form ponemos este bloque de codigo:

        ```python

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
                    curso.save()               #Guardamos el objeto en nuetra DB
                    return render(request, "AppCoder/inicio.html") #Renderiza la html inicio

            else:                              #Cuando el request es por GET (Ingresé mi URL y le di enter en la barra de navegacion, pidiendo (GET) algo)
                form= Curso_Form()             #Crea un formulario llamado "form" de la clase Curso_Form, aka, tiene nombre y comision - Este es un diccionario
            return render(request, "AppCoder/form_curso.html", {"formulario":form})  #Renderiza la pagina, usando el "form" como context
        #Django hace todo el trabajo de html al usar los fomrs.py

        ```

6. Recibimos en el html el formulario para renderizar el ```<form>```

    ```html

        <body>

            <h1>FORMULARIO DE CURSOS</h1>

            {% if formulario.error %}
                <p style = "color: red">Hay algo mal en el formulario</p>
            {% endif %}

            <form action="{% url 'curso_form' %}" method="POST">{% csrf_token %}

                <table>
                    {{ formulario.as_table }} <!-- el contexto que le mandamos desde la vista, rederizalo como una tabla. Django hace todo el trabajo de render-->
                </table>

                <input type="submit" value="Enviar"> 


            </form>
        </body>
    
    ```

Que esta pasando?

- Al entrar a la URL path('curso_form/', curso_form, name='curso_form'), se manda un request por metofo GET y pide se ejecute la vista curso_form
- En mi vista curso_form, el IF pregunta si el request fue por POST. De un principio, no es porque mandamos un get al entrar la URL. Por tanto, se brinca el IF y se va al ELSE
- En el ELSE primero se crea un form vacio (que es un diccionario), el cual contiene "nombre" y "comision".
- Ejecuta el return que renderiza form_curso.html usando form como contexto

- Al renderizar form_curso.html, el navegador me muestra la pagina con el form renderizado por Django
- Cuando yo meto datos a los campos vacios, son correctos y le doy enviar, se manda un request por metodo POST hacia la url indicada en mi form: form action="{% url 'curso_form' %}" method="POST". En este caso, se va a mandar a la URL curso_form; esto va a ejecutar la vista curso_form con un request tipo POST.
- En la vista, el IF pregunta si el request fue por POST. Esta ocacion si lo fue, por lo que ejecuta si codigo:
- Crea un objeto con el Curso_Form y los datos que le mandamos de la pagina, checa que form sea valido y guarda en un diccionario llamado info solo la data limpia que mandamos en el form
- Guardamos en variables independiantes los elementos del diccioanrio info (que es la data mandada desde la web) y con eso creamos un objeto Curo del modelo Curso (creamos una entrada para la DB con los datos que dicha tabla requiere)
- Guardamos el objeto en la DB
- Renderizamos la pagina de inicio (la renderizamos, pero no nos manda a la url de inicio, solo renderizamos en la url curso_form el inicio.html)

## Buscar datos de la DB con formularios

Usar un formulario para buscar algún dato en nuestra base de datos.

1. Creamos una vista, busqueda_comision(request)  

    ```python

    def busqueda_comision(request):

    return render(request, "AppCoder/form_busqueda_comision.html")

    ```

2. Registramos el url de la vista

    ```python

        path('busqueda_comision/', busqueda_comision, name='busqueda_comision'),
    ```

    - Cuando entramos a esta url, ejecuta la vista busqueda_comision, que es el renderizado de la html de abajo:

3. Creamos form_busqueda_comision.html

    ```html

        <form action="{% url 'buscar' %}" method="GET">{% csrf_token %}

            <input type="number" name="comision" id="comision"> 

            <input type="submit" value="Buscar"> 


        </form>

        {% if error %}
        <p style="color:red">{{ error }}</p>
        {% endif %}
    ```

    - Cuando le demos al boton buscar, va a enviar un request por metodo GET a mi path de la url 'buscar'
    - Al darle a la url 'buscar', va a ejecutar la vista 'buscar'

        ```python

        path('buscar/', buscar, name='buscar'),

        ```

4. Creamos la vista buscar:

    ```python

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

    ```

    - Si habia data en el cuadro de texto de la web form_busqueda_comision.html, hace lo del IF:
        - Lo del IF filtra los registros de la DB en base al dato enviado y renderiza un resultados_busqueda.html con los resultados de la busqueda

    - Si el dato del cuadro de texto de la web estaba vacio, hace lo del ELSE:
        - Lo del ELSE renderiza form_busqueda_comision.html mandando un mensaje de error en el context, permitiendome volver a ingresar data en el cuadro de texto de la web, pero desplegando el mensaje de error (ver el html, esta abajo del form)

5. Creamos resultados_busqueda.html

    ```html

    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Resultados</title>
    </head>
    <body>

        <h1>RESULTADOS DE LA BUSQUEDA</h1>

        {% if cursos %}

            {% for curso in cursos%}
                <p>{{ curso.nombre }}</p>
                <p>{{ curso.comision }}</p>
                    <br>

            {% endfor %}

        {% else %}
            <p>No hay cursos con esa comision</p>
        {% endif %}
        
        
    </body>
    </html>

    ```
