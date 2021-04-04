En este archivo, hare algunas aclaraciones generales.

* Todos los templates de las rutas estan en la carpeta Templates y estan escritos en Jinja que es una forma de escribir Python adentro de HTML y permite hacer templates sin JavaScript, es un lenguaje de Templates.

* Base.html sera el esqueleto de todos los HTML y los otros documentos sobreescribiran a este.

* Carpeta Static sirve para poner archivos JavaScript, CSS, imagenes y todo lo que es estatico y no cambia

* En un HTML puedo usar {{ }} que me permite escribir adentro codigo python adentro de eso 

* De la siguiente manera puedo pasar variables a la hora de renderizar templates: render_template("home.html", variable=5, texto="hola", boolean = True)
Dentro del template puedo usar la variable variable, la variable texto y la variable boolean. Puedo pasar tantas variables como quiera. Las puedo usar asi:{{variable}}

* ```
{% if boolean == True %}
<h1>Es true</h1>
{% else %}
<h1>Es false</h1>
{% endif %}```

* render_template es una funcion que toma HTML pero que tiene otras cosas en notacion Jinja con Python adentro y lo convierte a HTML normal.