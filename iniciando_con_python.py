# -*- coding: utf-8 -*-
"""Iniciando con Python.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lC4IO4BGnOwjKnbXUighff4gyV9O-Iww

# Iniciando con Python!

Bienvenidos al primer notebook con el que trabajaremos esta noche. En este notebook encontrarás una introducción a los conceptos  básicos de Python. Python es un lenguaje interpretado, esto hace que interactuar y aprender el lenguaje sea bastante sencillo, pues basta con ejecutar el interprete y listo, puedes empezar a enviarle expresiones que el interprete evalua como líneas de código. En la charla se hará una demostración de esto, pero en caso de que te la pierdas, aquí hay un video sencillo mostrando la interacción: https://www.youtube.com/watch?v=DtuyxfmhugQ

A medida que avances, asegúrate de guardar tu trabajo.

## El intérprete y su relación con un notebook

Como viste en la charla o en el video, el interprete es capaz de leer la línea de código que tú escribes en la terminal, interpretarla como una línea de Python y luego ejecutar el código que esta representa. A su vez, el intérprete guarda el estado de las variables que tú hayas declarado. 

Un jupyter notebook es una especie de cuaderno en el que puedes interactuar con el interprete de Python y a su vez agregar texto que describen el código que ejecutas. Un notebook tiene una secuencia de celdas las cuales pueden ser celdas con código para ejecutar o celdas con texto. El texto lo escribes en un lenguaje llamado Markdown, pero no te preocupes por estas notas ahora. 

Por otra parte, una celda con código funciona exactamente igual a una pequena terminal a través de la cual puedes hacer que el intérprete ejecute el código que quieras. Ejecutar una bloque de código en una celda en un notebook es equivalente a enviarle ese mismo código al interprete de una terminal.

## Hola mundo - Imprimir en consola
"""

print('Hola mi gente bella!')

"""También puedes guardar el texto que quieras en un variable y luego imprimir:"""

el_quijote = 'En un lugar de la Mancha, de cuyo nombre no quiero acordarme de algo ...'
print(el_quijote)

"""## 1. Números

Información cuantitativa surge en todas partes. Además de representar comandos para imprimir líneas, las expresiones pueden representar números y métodos para combinar números. La expresión `3.2500` se evalúa con el número 3.25. (Ejecuta la celda para ver)
"""

3.2500

"""Ten en cuenta que no tuvimos que agregar `print`. Cuando se ejecuta una celda de cuaderno, si la última línea tiene un valor, entonces Jupyter imprime útilmente ese valor para ti. Sin embargo, no imprimirá las líneas anteriores automáticamente. Si deseas imprimir una línea anterior, debes agregar la instrucción `print`. Ejecuta la celda a continuación para verificar."""

print(2)
3
4

"""Arriba deberías ver que 4, el valor de la última expresión, está impreso, pero 3 se pierde para siempre porque no se imprimió ni duró.

No quiere imprimir todo todo el tiempo de todos modos. Pero si sientes pena por 3, cambia la celda de arriba para imprimirla.

### 1.1. Aritmética
La línea en la celda siguiente resta. Su valor es lo que esperarías. Ejecutarlo.
"""

3.25 - 1.5

"""Muchas operaciones aritméticas básicas están integradas en Python. El operador común que difiere de la notación matemática típica es `**`, lo que eleva un número al poder del otro. Entonces, `2 ** 3` representa $ 2 ^ 3 $ y se evalúa a 8.

El orden de las operaciones es lo que aprendiste en la escuela primaria, y Python también tiene paréntesis. Por ejemplo, compare las salidas de las celdas a continuación. Usa paréntesis para un feliz año nuevo!
"""

2+6*5-6*3**2*2**3/4*7

2+(6*5-(6*3))**2*((2**3)/4*7)

"""En la notación matemática estándar, la primera expresión es

$$2 + 6 \times 5 - 6 \times 3^2 \times \frac{2^3}{4} \times 7,$$

mientras que la segunda expresión es

$$2 + (6 \times 5 - (6 \times 3))^2 \times (\frac{(2^3)}{4} \times 7).$$

** Pregunta 1.1.1. ** <br /> Escriba una expresión de Python en esta próxima celda que sea igual a $5 \times (3 \frac{10}{11}) - 49 \frac{1}{3} + 2^{.5 \times 22} - \frac{7}{33}$.    Por "$3 \frac{10}{11}$" queremos decir $3+\frac{10}{11}$, no $3 \times \frac{10}{11}$.

Reemplaza las elipsis (`...`) con tu expresión. Intenta usar paréntesis solo cuando sea necesario.

*Sugerencia:* La salida correcta debería ser un número familiar.
"""

(5 * (3 + 10/11)) - (49 + 1/3) + 2**(0.5*22) - 7/33

"""## 2. Nombres
En lenguaje natural, tenemos terminología que nos permite hacer referencia rápidamente a conceptos muy complicados. No decimos: "¡Es un mamífero grande con pelaje marrón y dientes filosos!" En cambio, solo decimos "¡Oso!"

De manera similar, una estrategia efectiva para escribir código es definir nombres para los datos a medida que los computamos, como un abogado definiría los términos de las ideas complejas al comienzo de un documento legal para simplificar el resto del escrito.

En Python, hacemos esto con * declaraciones de asignación *. Una instrucción de asignación tiene un nombre en el lado izquierdo de un signo `=` y una expresión que se evaluará a la derecha.
"""

diez = 3 * 2 + 4 +  1223423

"""Cuando ejecuta esa celda, Python primero evalúa la primera línea. Calcula el valor de la expresión `3 * 2 + 4`, que es el número 10. Luego le da a ese valor el nombre` diez`. En ese punto, el código en la celda se ejecuta.

Después de ejecutar esa celda, el valor 10 está ligado al nombre `diez`:
"""

diez

"""La afirmación `ten = 3 * 2 + 4` no afirma que` ten` ya es igual a `3 * 2 + 4`, como podríamos esperar por analogía con la notación matemática. Más bien, esa línea de código cambia lo que significa "diez"; ahora se refiere al valor 10, mientras que antes no significaba nada en absoluto.

Si los diseñadores de Python hubieran sido despiadadamente pedantes, podrían habernos hecho escribir

     defina el nombre diez para tener de ahora en adelante el valor de 3 * 2 + 4

en lugar. ¡Probablemente apreciarás la brevedad de "` = `"! Pero tenga en cuenta que este es el verdadero significado.

** Pregunta 2.1. ** <br /> Intenta escribir código que usa un nombre (como `once`) que no ha sido asignado a nada. ¡Verás un error!
"""

petro

"""Un patrón común en los cuadernos Jupyter es asignar un valor a un nombre y luego evaluar inmediatamente el nombre en la última línea de la celda para que el valor se muestre como salida."""

close_to_pi = 355/113
close_to_pi

"""Otro patrón común es que una serie de líneas en una sola celda construirá una computación compleja en etapas, nombrando los resultados intermedios."""

bimonthly_salary = 840
monthly_salary = 2 * bimonthly_salary
number_of_months_in_a_year = 12
yearly_salary = number_of_months_in_a_year * monthly_salary
yearly_salary

"""Los nombres en Python pueden tener letras (las letras mayúsculas y minúsculas son correctas y cuentan como letras diferentes), guiones bajos y números. El primer carácter no puede ser un número (de lo contrario, un nombre puede parecer un número). Y los nombres no pueden contener espacios, ya que los espacios se usan para separar partes de código entre sí.

Aparte de esas reglas, lo que nombre no importa * a Python *. Por ejemplo, esta celda hace lo mismo que la celda anterior, excepto que todo tiene un nombre diferente:
"""

a = 840
b = 2 * a
c = 12
d = c * b
d

"""** Sin embargo **, los nombres son muy importantes para que tu código * sea legible * para ti y para los demás. La celda de arriba es más corta, pero es totalmente inútil sin una explicación de lo que hace.

De acuerdo con una famosa broma entre los científicos de la computación, nombrar las cosas es uno de los dos problemas más difíciles en la informática. (Los otros dos son invalidación de memoria caché y errores "uno por uno." Y la gente dice que los científicos informáticos tienen un extraño sentido del humor ...)

**Ejercicio 2.2.** <br /> Asigne el nombre `seconds_in_a_decade` al número de segundos entre la medianoche del 1 de enero de 2010 y la medianoche del 1 de enero de 2020. Utilice Python para realizar cualquier aritmética requerida.

*Sugerencia:* Si estás atascado, averigua qué les pasó a los que nacieron el 29 de Febrero de 1996.
"""

# Change the next line so that it computes the number of
# seconds in a decade and assigns that number the name
# seconds_in_a_decade.
secs_per_day = 60 * 60 * 24
months_30_Days = 4
months_31_days = 7
months_28_days = 1
months_29_days = 1
secs_leap_year = secs_per_day * (30 * months_30_Days + 31 * months_31_days + 29 * months_29_days)
secs_regular_year = secs_per_day * (30 * months_30_Days + 31 * months_31_days + 28 * months_28_days)
leap_years_2010_2020 = 2
regular_years_2010_2020 = 8
seconds_in_a_decade = secs_leap_year * leap_years_2010_2020 + secs_regular_year * regular_years_2010_2020

# We've put this line in this cell so that it will print
# the value you've given to seconds_in_a_decade when you
# run it.  You don't need to change this.
seconds_in_a_decade

"""### 2.1. Revisar y solucionar problemas en tu código
Tienes un problema que crees puedes resolver con programación. Decides usar Python y escribes un programa para resolver tu problema. Lo corres. No sirve. Qué haces?

0. No te estreses, respira, chill. Dale un abrazo a tu mascota. 
1. Leer detalladamente lo que dice el error. No te pongas a revisar/buscar errores en el código sin saber cuál es el problema. 
2. Entender de verdad qué te está diciendo el intérprete acerca del error
3. Ir a la línea, revisar si el error está allí. Si lo está y lo encuentras, arréglalo. Si no, es posible que el error haya sido generado antes, pero se manifestó hasta que el intérprete llego a esa línea 
4. Buscar con paciencia y amor el error. 
5. Encontrar el error
6. Solucionar el error
7. Correr de nuevo el programa. Es posible que haya otro error. Vuelve al paso 0. si esto sucede.

Si ya hiciste los pasos 0. a 7. muchas veces y aún no puedes lograr que tu programa funcione, tal vez sea necesario pedir ayuda. Si tienes a alguien más experimentado cerca, pregunta! Esa persona seguro te ayudará o te guiará en la dirección correcta para resolver el error. En caso de que no pueda ayudarte, tal vez el sólo hecho de compartir tu problema ayuda a que descubras por obra y gracia de Turing el error que estás cometiendo. Esta técnica se llama Rubber Duck programming.

### 2.2. Comentarios
Puede haber notado esta línea en las celda de arriba:

     # celda con algo escrito que aun no entiendo qué hace ahí!

Eso se llama *comentario*. No hace que nada suceda en Python; Python ignora cualquier cosa en una línea después de un #. En cambio, está ahí para comunicarle algo sobre el código, el lector humano. Los comentarios son extremadamente útiles.

<img src="http://imgs.xkcd.com/comics/future_self.png" alt="comic about comments">

## 3. Llamando Funciones

La forma más común de combinar o manipular valores en Python es llamando funciones. Python viene con muchas funciones incorporadas que realizan operaciones comunes.

Por ejemplo, la función `abs` toma un único número como argumento y devuelve el valor absoluto de ese número. El valor absoluto de un número es su distancia desde 0 en la recta numérica, por lo que `abs (5)` es 5 y `abs (-5)` también es 5.
"""

abs(5)

abs(-5)

"""##### múltiples argumentos
Algunas funciones toman múltiples argumentos, separados por comas. Por ejemplo, la función incorporada `max` devuelve el argumento máximo que se le pasa.
"""

max(2, -3, 4, -5)

"""También podemos combinar funciones, tanto como queramos. Esto se llama nesting"""

max(23, 34 - 7, abs(-31))

mass_of_earth = 5.972 * 10**24

max(23, 34 - 7,mass_of_earth , abs(-31))

"""También podemos llamar funciones sobre Strings:"""

# Replace one letter
'Hello'.replace('H', 'C')

# Replace a sequence of letters, which appears twice
'hitchhiker'.replace('hi', 'ma')

# Calling replace on the output of another call to replace
'train'.replace('t', 'ing').replace('in', 'de')

"""Hay métodos para strings que no reciben parámetros:

|Method name|Value|
|-|-|
|`lower`|a lowercased version of the string|
|`upper`|an uppercased version of the string|
|`capitalize`|a version with the first letter capitalized|
|`title`|a version with the first letter of every word capitalized||

Podemos también convertir de número a string y de string a número:
"""

8 + "8"

8 + int("8")

"""Y si queremos obtener la longtitud de un string (una pregunta muy común), también podemos hacerlo:"""

a_very_long_sentence = "The representatives of the French people, organized as a National Assembly, believing that the ignorance, neglect, or contempt of the rights of man are the sole cause of public calamities and of the corruption of governments, have determined to set forth in a solemn declaration the natural, unalienable, and sacred rights of man, in order that this declaration, being constantly before all the members of the Social body, shall remind them continually of their rights and duties; in order that the acts of the legislative power, as well as those of the executive power, may be compared at any moment with the objects and purposes of all political institutions and may thus be more respected, and, lastly, in order that the grievances of the citizens, based hereafter upon simple and incontestable principles, shall tend to the maintenance of the constitution and redound to the happiness of all."
sentence_length = len('hello')
sentence_length

"""## 4. Importando Código
> Lo que ha sido será otra vez,
> lo que se ha hecho se hará de nuevo;
> no hay nada nuevo bajo el sol.

La mayoría de la programación implica un trabajo que es muy similar al trabajo que se ha hecho antes. Dado que escribir código consume mucho tiempo, es bueno confiar en el código publicado de los demás siempre que sea posible. En lugar de copiar y pegar, Python nos permite **importar** otro código, creando un **módulo** que contiene todos los nombres creados por ese código.

Python incluye muchos módulos útiles que están a solo `import` de distancia. Veremos el módulo `math` como primer ejemplo. El módulo `math` es extremadamente útil en el cálculo de expresiones matemáticas en Python.

Supongamos que queremos calcular con mucha precisión el área de un círculo con un radio de 5 metros. Para eso, necesitamos la constante $ \ pi $, que es aproximadamente 3.14. Convenientemente, el módulo `math` tiene` pi` definido para nosotros:
"""

import math as mt
radius = 5
qw = radius**2 * mt.pi

"""`pi` se define dentro de` math`, y la forma en que accedemos a los nombres que están dentro de los módulos es escribiendo el nombre del módulo, luego un punto, luego el nombre de lo que queremos:

     <nombre del módulo>. <nombre>
    
Para usar un módulo, primero debemos escribir la declaración `import <module name>`. Esa declaración crea un objeto de módulo con cosas como `pi` en él y luego asigna el nombre` matemática` a ese módulo. Arriba hemos hecho eso para `math`.

![XKCD](http://imgs.xkcd.com/comics/e_to_the_pi_minus_pi.png)

### 4.1. Importación de funciones

**Los módulos** pueden proporcionar otras cosas nombradas, incluidas **funciones**. Por ejemplo, `math` proporciona el nombre` sin` para la función seno. Al haber importado `math`, podemos escribir` math.sin(3)`para calcular el seno de 3. (Tenga en cuenta que esta función seno considera que su argumento está en [radianes] (https://en.wikipedia.org) / wiki / Radian), no grados. 180 grados son equivalentes a $ \ pi $ radianes.)

** Pregunta 4.1.1. ** <br/> Un ángulo de $\frac{\pi}{4}$-radianes (45-grados) angle forma un triángulo rectángulo con base y altura como se muestra en la figura.  Si la hipotenusa (el radio del círculo en la figura) es 1, entonces la altura es $\sin(\frac{\pi}{4})$.  Computa eso usando `sin` y `pi` del módulo `math`.  Pon el resultado en una variable llamada `sine_of_pi_over_four`.

<img src = "http://mathworld.wolfram.com/images/eps-gif/TrigonometryAnglesPi4_1000.gif">
(Fuente: [Wolfram MathWorld] (http://mathworld.wolfram.com/images/eps-gif/TrigonometryAnglesPi4_1000.gif))
"""

sine_of_pi_over_four = mt.sin(mt.pi/4)
sine_of_pi_over_four

"""## 5. Arrays
Hasta ahora, no hemos hecho mucho que no puedas hacer a mano, sin tener que preocuparte por aprender Python. Las computadoras son más útiles cuando una pequeña cantidad de código realiza mucho trabajo al * realizar la misma acción * a * muchas cosas diferentes *.

Por ejemplo, en el tiempo que lleva calcular el 18% de propina en una cuenta de restaurante, una computadora portátil puede calcular 18% de propinas por cada factura de restaurante pagada por cada humano en la Tierra ese día. (¡Eso es si eres bastante rápido para hacer aritmética en tu cabeza!)

**Arrays** es cómo ponemos muchos valores en un solo lugar para que podamos operarlos como un grupo. Por ejemplo, si `billions_of_numbers` es una matriz de números, la expresión

    .18 * billions_of_numbers

da una nueva serie de números que es el resultado de multiplicar cada número en `billions_of_numers` por .18 (18%). Los arrays no están limitados a números; también podemos poner todas las palabras de un libro en un array de stringss.

Concretamente, un array es una **colección de valores del mismo tipo**, como una columna en una hoja de cálculo de Excel.
"""

# Así se declara un array en python
cars = ["Ford", "Volvo", "BMW"]

# Para obtener el primer elemento
cars[0]

"""Como puedes ver, en Python los índices para obtener los elementos comienzan a contar en 0. Esto quiere decir que si un array tiene n elementos, podremos acceder a los índices 0, 1, ....., n-1. Esto es un concepto muy importante y aplica para la mayoría de lenguajes de programación, excepto Matlab o Julia (estos comienzan en 0 y van hasta n. Supongo que esto hace que los matemáticos o físicos no se asusten de programar pues vienen acostumbrados a escribir sumatorias desde 1)."""

# Para iterar sobre los elementos de un array
for car in cars:
  print(car)

# Para agregar un elemento a un array
cars.append("Honda")
cars

# Para eliminar un elemento de un array llamamos pop() y le pasamos el índice del elemento por parámetro
cars.pop(2)
cars

cars

# Eliminar un elemento por su valor
cars.remove("Honda")

cars

"""Qué pasa si borramos 'Honda' de un array hay más de un elemento con el valor 'Honda'?"""

ar = ['b','a', 'b','x',  'b', 'c']

ar.remove('b')
ar

# Para ordenar un array (Lo hace in place)
numbers = [1,3,67,12,67,21,43,75]
numbers.sort()
print(numbers)

"""Hay un tipo de array más poderoso y al cual podemos aplicarle más operaciones. Es el array provisto por el módulo Numpy. Se comporta igual que el array regular de python, sólo que ofrece más posibilidades al programador."""

import numpy as np
multiples_of_99 = np.arange(0,10000,99)
multiples_of_99

"""## 6. Creando nuestras propias funciones

Cuando aprendas mucho más sobre Python y quieras hacer cosas más complejas, encontrarás que Python no tiene incorporada alguna funcionalidad que necesitas. Cuando esto sucede, lo que debes hacer es implementar tú esa funcionalidad en forma de una función. Supongamos que necesitamos una función que recibe una lista de números y retorna la suma del menor con el mayor. Esta funcionalidad se puede implementar así:
"""

def sum_max_min (numbers):
    max_number = max(numbers)
    min_number = min(numbers)
     print('asdsa')
    return max_number + min_number


my_list = [2,4,87,1,13,45,100]
sum_max_min(my_list)

"""Una función puede retornar más de un valor. Esto se puede hacer de varias formas, como se puede ver en el siguiente link. https://www.geeksforgeeks.org/g-fact-41-multiple-return-values-in-python/. En realidad, retornar una lista o cualquier otro objeto que contenga los elementos es algo que pueden hacer muchos lenguajes de programación. Python tiene una manera diferente y bonita de hacer esto: tuplas (o tuples en Inglés). 

Una tupla es una secuencia de objetos de Python inmutables. Las tuplas son secuencias, como listas. Las diferencias entre tuplas y listas son que las tuplas no se pueden cambiar a diferencia de las listas y las tuplas usan paréntesis, mientras que las listas usan corchetes cuadrados.

Crear una tupla es tan simple como poner diferentes valores separados por comas. Opcionalmente, también puede poner estos valores separados por comas entre paréntesis. Por ejemplo:
"""

tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5 )
tup3 = "a", "b", "c", "d"

# así se puede acceder a los valores de las tuplas
tup2 = (1, 2, 3, 4, 5, 6, 7 )
print("tup1[0]: ", tup1[0])
print ("tup2[1:5]: ", tup2[1:5])

"""Entonces, para retornar múltiples valores en usando tuplas:"""

def sum_max_min_tuples (numbers):
    max_number = max(numbers)
    min_number = min(numbers)
    return max_number + min_number, max_number, min_number

my_list = [2,4,87,1,13,45,100]
my_tuple = sum_max_min_tuples(my_list)
print(my_tuple)

"""## 7. Un regalito: Importar y analizar datos

Un sitio web llamado [Gapminder](https://www.gapminder.org/) recopila una gran variedad de medidas de salud humana, educación y progreso. Cada medida se publica en una tabla que tiene una fila por país y una columna por año, que describe cómo la medición varía con el tiempo y el lugar.

Por ejemplo, [esta tabla](https://docs.google.com/spreadsheets/d/1kmnYQzXLGVF9RbKB3Y-WuUsJFumnE4s2UWdmlskv6r4/pub#) describe la cantidad promedio de años de escuela a la que asistieron mujeres de 25 años en adelante. La tabla tiene una fila para cada uno de 175 países y una columna para cada año desde 1970 hasta 2009. Los datos se estimaron para un estudio del [Instituto de Métricas y Evaluación de la Salud](http://www.healthmetricsandevaluation.org/) llamado "Mayor logro educativo y su impacto en la mortalidad infantil: un análisis sistemático en 175 países desde 1970 hasta 2009" ([enlace](http://www.healthmetricsandevaluation.org/resources/datasets/2010/education_attainment/education_attainment.html&sa= D & ust = 1522644678563000 & usg = AFQjCNG-Rn_hO868jLLBz6FRLT8LSqwUVA)).

Para cargar tablas en Python, primero debe importar el módulo `pandas`. La segunda línea a continuación se asegura de que los gráficos aparezcan en la pantalla cuando los crea. Solo necesita ejecutar estas líneas una vez por computadora portátil (y cada vez que reinicie su kernel).
"""

# No cambies esta celda
import pandas as pd
import matplotlib.pyplot as plt
# %matplotlib inline

"""Ahora, ejecute la siguiente celda para cargar la tabla que describe los años de escuela a los que asistieron mujeres de todo el mundo y a lo largo del tiempo. Solo se mostrarán las primeras 10 filas de la tabla."""

school = pd.read_csv('school.csv')
school

"""Miremos como le va a Colombia:"""

school.loc[school['Row Labels'] == 'Colombia']

"""Y como le va los mejores países cada 10 años?"""

school.sort_values('1970', ascending=False).loc[:, ['Row Labels', '1970','1980','1990','2000', '2009']]

"""Y a los peores, también cada 10 años?"""

school.sort_values('1970').loc[:, ['Row Labels', '1970','1980','1990','2000', '2009']]

"""Miremos cómo la métrica cambia para Colombia cada década"""

school.loc[school['Row Labels'] == 'Colombia'].sort_values('1970', ascending=False).loc[:, ['Row Labels', '1970','1980','1990','2000', '2009']]

"""Podemos crear gráficas que nos ayuden a visualizar mejor los datos que procesamos arriba. Hagamos un barchart con los resultados en 2009."""

only_2009 = school.sort_values('2009').loc[:, ['Row Labels', '2009']]

only_2009.plot(kind='barh', x='Row Labels', y='2009', figsize=(10,36))

"""Auch, No se ve muy bien debido a que son demasiados países. Analicemos sólo los  países con menos años de escolaridad"""

top_2009= only_2009.head(10).sort_values('2009')
plot_top_2009 = top_2009.plot(kind='barh' , x='Row Labels', y='2009');

# Set the y-axis label
plot_top_2009.set_ylabel("Countries")

# Set the y-axis label
plot_top_2009.set_xlabel("Years in school by 2009")

"""**Cómo se ve el panorama global de educación mundial para las mujeres?**"""

# Initialize a new figure
fig, ax = plt.subplots()

# Draw the graph
ax.plot(only_2009['Row Labels'], only_2009['2009'], linestyle='', marker='o')
plt.xticks(rotation=45)

# Set the label for the x-axis
ax.set_xlabel("Countries")

# Set the label for the y-axis
ax.set_ylabel("Years at school for women")

"""Como ves, tan sólo en el 10% de los países las mujeres van 12 años o más a la escuela. Hagamos un histograma para ver mejor este resultado:"""

bins_histogram = range(1,15)
histogram_2009 = only_2009.plot(kind='hist', bins=bins_histogram , x='Row Labels', y='2009', figsize=(10, 10),  rwidth=0.9);
# Set the y-axis label
histogram_2009.set_ylabel("Frecuency")

# Set the y-axis label
histogram_2009.set_xlabel("Years in school in 2009")

"""**Pregunta** ¿Está mejorando la educación de mujeres a medida que pasa el tiempo?"""

# obtener los datos para los anhos que quieras comparar
data_1970 = school.loc[:, [ 'Row Labels', '1970']]
histogram_1970 = data_1970.plot(kind='hist', bins=bins_histogram , x='Row Labels', y='1970', figsize=(10, 10),  rwidth=0.9);
# Set the y-axis label
histogram_1970.set_ylabel("Frecuency")

# Set the y-axis label
histogram_1970.set_xlabel("Years in school in 1970")

"""La educación para mujeres está mejorando!"""

data_1970_2009 = school.sort_values('2009').loc[:, [ 'Row Labels', '1970', '2009']]
bar = data_1970_2009.plot(kind='barh', x='Row Labels', figsize=(10,36));
# Set the y-axis label
bar.set_ylabel("Countries")

# Set the y-axis label
bar.set_xlabel("Years in school")

"""Como podemos ver, en ningún país la línea azul es más larga que la línea naranja. El panorama de educación para las chicas mejora, pero aún podemos hacer mucho."""

