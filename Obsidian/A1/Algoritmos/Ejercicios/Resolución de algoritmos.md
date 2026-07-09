## E16
Eliminar palabras que se dupliquen en un texto indistinto de mayuscula y minuscula.
Necesito obtener cada palabra individual y compararla con el resto, si coincide en algun punto, debemos saltarla (no incluirla en la cadena final).

**Lógica:**
Deberíamos recolectar palabra por palabra y guardarla en una lista.
A su vez, si la palabra a analizar no esta en la lista, debemos añadirla a la cadena final, si esta en la lista, significa que es una repetida.

Pasos:
*Definir cadena, subcadena y lista.*
*Recorrer la cadena.*
	*Obtener palabra (subcadena)*
	*Verificar si existe en la lista:*
		*Si existe: pasar*
		*SI NO EXISTE: concatenar a la segunda cadena.*
			*Añadir palabra a la lista.*
*Escribir segunda cadena*.

**Codigo:

`c = input() #Recibir cadena.`

`c2 = "" #Cadena a imprimir.`

`v = [] #Lista de palabras a verificar. Si se quiere, se puede hacer por cadena.`

`s = "" #SubCadena (palabra)`

  

`for i in range(len(c)):`
	`f = False #Flag.`
	`if not c[i].isalpha() or i == len(c)-1: #Si no es una letra.`
		`if len(s) == 0:`
			`continue #Siguiente`
		`for j in range(len(v)): #Verificar lista.`
			`if s == v[j]: #Si se repite.`
				`f = True #Activamos bandera.`
				
				`s = "" #Reiniciar variable`
				
				`break #Salir.`
	
		`#Si no se encontro coincidencia.`
		`c2 = c2 + s #Conecatenar a la segunda cadena.`
		`c2 = c2 + c[i] #Conecatenar caracter especial.`
		`v.append(s) #Añadir palabra a la lista.`
		`s = "" #Reiniciar variable`
	
	`else:`
		`s = s + c[i] #Recolectar letra de la cadena.`

`print(c2)`
_**-------------------------------------------------------------------------------------**_

## E17

Cadenas de caracteres, ejercicio de inscriptacion.

Original: Hola Cómo Éstán?

Encriptado: ?-.n-.á-.t-.s-.É-.*-.o-.m-.ó-.C-.*-.a-.l-.o-.H-

- Averigurar cual es el metood de inscriptacion
- Recibir la cadena encriptada y descencriptarla mediante codigo para mostrarla.


**Logica: 
Para desencriptar, se debe limpiar el mensaje tal cual, en el se deben recolectar de derecha a izquierda los valores que no son "-." y ademas detectar cuando hay un "*" o 2 -. anidados ya que representa un espacio.

*Recibir cadena*
*definir sub cadena "sub"*

*recorrer cadena caracter por caracter:*
	*SI el caracter es "." o * Entonces concatenar un espacio en sub.*
	*SINO:* 
	 *Guardar caracter empezando de derecha a izquierda desde el penultimo caracter (len(c)-(i+2)), conectatenar a sub.*
	*Saltar 2 indices hacia la izquierda.*

*Mostrar sub*.

**Tiempo tardado: 20 minutos

`#E17 CADENAS`
`#Cadena de inscriptacion, ampleacion en obsidian.`
`c = input("Cadena encriptada: ")`
`s = "" #Cadena desencriptada.`
`k = 0 #Contador verifica espacios.`

`for i in range(len(c)):`
`if c[len(c)-(i+1)] != "." and c[len(c)-(i+1)] != "-": #Si es un caracter.`
	`if c[len(c)-(i+1)] == "*":`
		`s = s + " " #Concatenamos el espacio.`
	`else:`
		`s = s + c[len(c)-(i+1)] #Concatenamos el caracter.`
  

`print(s)`

**_-------------------------------------------------------------------------------------_**
## E18

**Actividad: El mensaje original está formado tomando la primera letra de cada palabra. Reconstruyan la frase oculta.

**Lógica:** Debemos recorrer la frase e ir recolectando las iniciales de cada palabra.

Debemos recibir la frase.
Detectar cada palabra (Mediante los espacios)
Obtener la inicial y concatenarla a una cadena.

Se puede hacer mediante detectar el siguiente caracter luego de un espacio.

**Código:
`c = input()`
`s = "" #Cadena oculta.`
`f = True #Bandera para avisar cuando se deba recuperar el caracter.`

`for i in range(len(c)):`
	`if f: #AL inicio comienza true para recuperar el primero.`
		`s = s + c[i]`
		`f = False`
	`elif c[i] == " ": #Si es un espacio.`
		`f = True #Activar bandera para recibir el proximo caracter.`
`print(s)`

**Tiempo: 15 minutos.

_-------------------------------------------------------------------------------------_

## E19
Ejercicio de listas enlazadas.

Necesito ordenar nombres mediante listas simples simulandouna lista enlazada donde:
- Tenga una lista para los nombres.
- Una para los indices de los nombres.
- Una variable que sirva como primer indice.
Se ingresan los nombres uno a uno, en el proceso se debe reordenas la lista enlazada (indices) para que, al recorrerla, la recorra en orden alfabetico.

Despues de cada ingreso se debe mostrar las listas valorde inicio y la lista segun el recorrido.

**Proceso:**
Definir las listas y variables.
Iniciar bucle mientras la entrada sea != 0:
	Recibir los nombres 
	Añadirlo a la lista de nombres.
		Analizar la lista y encontrar el primero mas grande **EX1**
			Añadirlo y modificar la lista de indices.
	Imprimir listas

**EX1**
	Si la lista no tiene contenido, se agrega inicialmente el elemento en nombres.
	Sino:
		Se debe recorrer la lista segun los indices, comparando los elementos con el ultimo nombre ingresado:
		Si hay un nombre > al ultimo nombre en la lista, se debe:
			Guardar el valor del puntero del siguiente.
			Asignar el ultimo indice (osea del ultimo nombre añadido) en esa posicion.
			Y en la ultima posicion (el ultimo indice) asignarle el valor del puntero.
		Sino, si se encuentra un "-1" osea el indice de finalizacion, se le asigna en esa posicion el ultimo indice de la lista, para de esa forma a ese ultimo indice, asignarle el -1, ya que seria el mas grande.
De esa forma, cada vez que ingrese u nuevo nombre, se compara con el resto de la lista, si llegara a ser mas chico que alguno de la lista, se reasigna el puntero para apuntar a este nuevo nombre, que a su vez este ultimo indice apuntara a su mayor. Aprovechando la facilidad de las listas entrelazadas.

**Codigo

`#E19 Listas enlazadas.`

`n = [] #Nombres.`

`id = [] #Indices.`

`ini = 0 #Variable de inicio.`

`e = "" #Input de entrada de los nombres.`

  

`while e != "0":`

`e = input() #Recibe el nombre.`

`if e == "0":`

`break #Salir del bucle si el usuario ingresa "0".`

  

`a = ini #Variable puntero.`

`id.append(-1) #Se le añade como supuesto final.`

`n.append(e)`

`for i in range(len(n)-1): #Itera la lista de nombres.`

`print(f"a = {a}, id[a] = {id[a]}, id[id[a]] = {id[id[a]]}, ITERACION: {i}")`

`if i == 0: #Comenzar con ini.`

`if n[a] > e: #Si el nombre es mayor nuevo.`

`#Cambiamos el indice del inicial al nuevo inicial.`

`id[len(n)-1] = ini`

`ini = len(n)-1`

`break #Sale`

`else: #Comprueba si es el ultimo elemento.`

`if n[id[a]] > e: #Si el nombre es mayor nuevo.`

`g = id[a] #Guardamos su puntero.`

`id[a] = len(n)-1 #Al valor antiguo le asignamos el valor del nuevo.`

`id[len(n)-1] = g #Reasignamos el anterior menor.`

`elif id[id[a]] == -1: #Si un id quedo desactualizado.`

`id[id[a]] = len(n)-1 #Se le asgina el ultimo valor.`

`a = id[a] #Avanza al siguiente elemento.`

`#Imprimir recorrido de lista.`

`print(f"Nombres: {n}, Id: {id}, Ini: {ini}")`

`print(n[ini])`

`b = ini`

`for i in range(len(n)-1):`

`print(n[id[b]])`

`b = id[b]`

**Tiempo: 1h 30min

**_-------------------------------------------------------------------------------------_**
## E20
Ordenar nombres mediante listas doblemente enlazadas, donde se pueda saber el puntero siguiente y anterior del elemento.

Consiste en el mismo ejercicio anterior #E19 pero añadiendola posibilidad de tener una lista con los indices anteriores.

Analisis:
Se debe mantener la estructura de listasentrelazadas, donde se recorre lalista entrelazada hasta encontrar un valor mayor, en ese caso el elemento en ultima posicio (el nuevo) se asigna por ese mayor en la lista de indices, y luego se asigna al mayor como siguiente de ese nuevo elemento.
Lo que necesito es añadir el seguimiento inverso, osea que en la misma posicion en otra lista, puedas acceder al elemento anterior.

Logica:
Definir listas y variables.
	Recibir nombre
	Añadir a listas
		Recuperar indice anterior en variable previa.
		Buscar elemento mayor y remplazar indices
		Añadir en la misma posicion en la lista de anteriores, el indice previo (variable previa).
	Escribir listas
	~Si ingresa un "0", salir.
Escribir listas.

**Codigo:

`#E20 Lista doblemente enlazada.`

`#Se debe almacenar y ordenar nombres mediante una lista doblemente enlazada donde exista indices de punteros posteriores y anteriores.`

`#Explicacion en obsidian.`

  

`n = [] #Nombres.`
`id = [] #Indices punteros posteriores.`
`back = [] #Indices punteros anteriores.`
`ini = 0 #Inicio lista posterior.`
`bck = 0 #Inicio lista anterior.`
`a = "" #Variable input.`

`while a != "0":`
	`a = input()`
	`if a == "0":`
		`break #Sale del bucle.`
	`n.append(a)`
	
	`#Asumimos que es el mas grande.`
	`id.append(-1)`
	`back.append(-1)`
	`b = ini #B es el inidice de recorrido.`
	`prev = b #Obtiene el indice previo (anterior).`
	
	`for i in range(len(n)):`
		`if i == 0: #Si es el inicio.`
			`if n[b] > a: #Si el nuevo es menor al ini.`
			`#Lo remplazamos.`
			`ini = len(n)-1`
			`id[len(n)-1] = 0`
			
			`#Actualizamos la lista de punteros anteriores.`
			`back[b] = len(n)-1 #Ahora hay un nuevo anterior.`
			`back[len(n)-1] = -1 #Lo asignamos como ultimo.`
			`break`
		`else:`
			`if id[b] == -1: #Si es un antiguo ultimo.`
				`#Lo apunta hacia el ultimo elemento (el nuevo).`
				`id[b] = len(n)-1`
				`#El puntero anterior del nuevo ultimo apunta al viejo ultimo.`
				`bck = len(n)-1 #Remplaza el comienzo.`
				`back[len(n)-1] = b`
				`break`
			`elif n[id[b]] > a: #Si encontro otro mayor.`
				`#Lo remplaza.`
				`c = id[b]`
				`id[b] = len(n)-1`
				`id[len(n)-1] = c`
				
				`#El viejo chico apunta al nuevo chico.`
				`back[b] = len(n)-1`
				`#Y el nuevo chico apunta a su anterior.`
				`back[len(n)-1] = prev`
				`break`
			
			`prev = b #Obtiene el indice previo (anterior).`
			`b = id[b] #Avanza en el recorrido de la lista.`

	#Imprimir datos
	`print(f"N: {n}, ID: {id}, BACK: {back}, INICIO: {ini}, BCK: {bck}")`
	`print(n[ini])`
	`b = ini`
	`for i in range(len(n)-1):`
		`print(n[id[b]])`
		`b = id[b] #Siguiente indice.`
	
	`print("---------------")`

**Tiempo: 53 Min.

**_-------------------------------------------------------------------------------------_**
## E21
Problema del preparcial para la promocion, sobre en analisis de fechas de una matriz.

Se dispone de una matriz que contiene fechas con la siguiente disposición: (la misma se ingresa for fila  columna)
Se pide:

1- Determinar si la fecha ingresada existe en la matriz. Si existe, imprimir EXISTE y la fila en la que se encuentra. Crear función: existe-fecha()

2- Si no existe, determinar la fecha más cercana menor y más cercana mayor que existan en la matriz. Crear [funciones](https://cvirtual.frvm.utn.edu.ar/mod/quiz/view.php?id=132342 "Funciones"): buscar-menor() y buscar-mayor().

Se debe analizar la fecha individualmente y si cumple con las 2 condiciones, de ser valida para la fecha de parametros y la fecha buscada, se guarda como fecha buscada.

Extensión en hoja del cuaderno.

**Codigo:**
`#E21 Parcial promocion.`

`#Determinar segun una matriz, si la fecha ingresada existe, e imprimir su fila, sino buscar fecha mayor y menor mas cercana con sus filas.`

`def buscar(m,f):`

`for i in range(len(m)): #Buscar fecha en las filas.`

`if m[i][4] == f: #Si es la misma fecha.`

`return i #Retorna el indice.`

`return -1 #Retorna error.`

  
  

`def mayor(m,f): #Fecha mayor mas cercana.`

`fb = [] #Fecha buscada.`

`index = -1 #Indice de la fecha.`

`s = "" #String a retornar.`

  

`for i in range(len(m)):`

`b = False #Bandera valido.`

`b2 = False #Bandera buscado.`

`b3 = False #Bandera de numero correcto.`

`for j in range(3):`

`k = 3-j #Itera las columnas de año, mes, y dia respectivamente.`

`if b3 == False and int(m[i][k]) < int(f[2-j]): #Si es menor a la fecha base, se descarta.`

`b = True #Activamos bandera.`

`break #Salimos de esta iteracion`

`elif fb == [] or int(m[i][k]) < int(fb[2-j]): #Si encontro una alternativa mas pequeña (trival -sin alretnativas- o logica).:`

`b2 = True #El valor encontrado es mas cercano.`

`b3 = True #Sirve para que se siga analizando mas alla del año.`

`if b == False and b2 == True: #Mientras el valor obtenido sea valido y mas cercano.`

`e = [m[i][1], m[i][2], m[i][3]] #Recolectar fecha en formato vector.`

`fb = e #Remplazamos fecha buscada.`

`index = i #Obtenemos la fila.`

`if index != -1:`

`s = m[index][4] #Obtenemos la fecha directamente.`

`return s #Retorna la fecha.`

  

`def menor(m,f): #Fecha menor mas cercana.`

`fb = [] #Fecha buscada.`

`index = -1 #Indice de la fecha.`

`s = "" #String a retornar.`

  

`for i in range(len(m)):`

`b = False #Bandera valido.`

`b2 = False #Bandera buscado.`

`b3 = False #Bandera de numero correcto.`

  

`for j in range(3):`

`k = 3-j #Itera las columnas de año, mes, y dia respectivamente.`

`if int(m[i][k]) > int(f[2-j]): #Si es mayor a la fecha base, se descarta.`

`b = True #Advertimos.`

`break #Salimos de esta iteracion`

`elif fb == [] or int(m[i][k]) > int(fb[2-j]): #Si encontro una alternativa mas grande (trival -sin alretnativas- o logica).`

`b2 = True #Habilitamos.`

`b3 = True #Sirve para que se siga analizando mas alla del año.`

`if b == False and b2 == True: #Si es valido y mas cercano:`

`e = [m[i][1], m[i][2], m[i][3]] #Recolectar fecha en formato vector.`

`fb = e #Remplazamos fecha buscada.`

`index = i #Obtenemos la fila.`

`if index != -1:`

`s = m[index][4] #Obtenemos la fecha directamente.`

`return s #Retorna la fecha.`

  

`t = int(input("Tamaño filas: "))`

`m = [[input() for _ in range(5)]for _ in range(t)]`

`print(f"Matriz: {m}")`

`f = input("Ingresar fecha: ")`

  

`a = buscar(m,f)`

`if a != -1:`

`print("EXISTE")`

`print(f"FILA: {a}")`

`else:`

`#Convertir cadena a lista.`

`e = [f[0:2],f[3:5],f[6:]]`

`#Alternativa algoritmica:`

`#e = []`

`#c = 0 #Contador vector.`

`#a = "" #Subcadena.`

`#for i in range(len(f)):`

`ma = mayor(m,e)`

`lo = menor(m,e)`

`print(f"Mayor mas cercana: {ma}")`

`print(f"Indice: {buscar(m,ma)}")`

`print(f"Menor mas cercana: {lo}")`

`print(f"Indice: {buscar(m,lo)}")`

**Tiempo: 2 horas**

**_-------------------------------------------------------------------------------------_**
## E23
Realizar programa que simule el juego 3 en raya.
Consiste en verificar reglas, turnos y patrones ganadores del juego 3 en raya en un bucle unico.

Mas expansion en papel.

**Codigo:**

`#E23 tres en raya.`
`#Consiste en simular el juego 3 en raya, con sus reglas y manteniendo un bucle constante hasta que un jugador gane.`
`#Expandido en papel.`

`def mover(p, m, tar, pos): #Se encarga de mover las fichas en la matriz.`
    `m[tar[0]][tar[1]] = py[0] #Asigna la ficha del jugador.`
    `if p <= 0: #Si esta moviendo la ficha (no tiene mas fichas).`
        `m[pos[0]][pos[1]] = 0 #Libera el lugar.`
    `return m`

`def valido(p, m, position, target): #Validar movimientos y realizarlos.`
    `#Obtener coordenadas.`
    `pos = []`
    `if len(position) > 0:`
        `pos = [int(position[0]),int(position[2])]`
    `tar = [int(target[0]),int(target[2])]`

    `if m[tar[0]][tar[1]] != 0 or (len(pos) > 0 and m[pos[0]][pos[1]] != py[0]): #Si esta ocupada o quiere mover una ficha diferente.`
        `return [] #Invalidar movimiento.`

    `if py[1] > 0 or pos[0] == pos[1]: #Si estas eligiendo o estas en el medio.`
        `#Se posiciona directamente.`
        `return mover(py[1], m, tar, pos) #Llama a funcion de mover.`
    `elif (abs(pos[0] - tar[0]) + abs(pos[1]-tar[1])) < 2: #Si no quiso mover diagonalmente.`
        `return mover(py[1], m, tar, pos) #Llama a funcion de mover.`
    `else: #Si quiso mover diagonalmente.`
        `return [] #Invalidar movimiento.`

`def ganador(m): #Validar patrones ganadores.`
    `#Comprobar patrones posibles y devolver el jugador que gano.`
    `for i in range(3): #Iterar 3 veces para validar 3 en raya.`
        `if m[i][0] == m[i][1] == m[i][2] and m[i][0] != 0:`
            `return m[i][0]`
        `elif m[0][i] == m[1][i] == m[2][i] and m[0][i] != 0:`
            `return m[0][i]`
    `if m[0][0] == m[1][1] == m[2][2] and m[0][0] != 0:`
        `return m[0][0]`
    `elif m[0][2] == m[1][1] == m[2][0] and m[0][2] != 0:`
        `return m[0][2]`
    `else: #Si ninguno gano`
        `return 0 #Retornar ninguno.`

`def cambio(p, j): #Cambiar jugador.`
    `if p[0] == 1: #Si es el primer jugador.`
        `#Cambiamos por el segundo.`
        `p[0] = 2`
        `p[1] = j[1]`
    `else:`
        `#Cambiamos por el primero.`
        `p[0] = 1`
        `p[1] = j[0]`
    
    `return p`

`f = [3,3] #Definir fichas de los 2 jugadores.`
`py = [1,3] #Nro jugador y fichas disponibles.`
`m = [[0 for _ in range(3)]for _ in range(3)]`
`g = 0 # Toma el valor del Ganador.`

`while g == 0: #Mientras no haya ganador.`
    `#Imprimir matriz.`
    `p = t = ""`
    `for i in range(3):`
        `s = "" #Imprimir matriz con formato.`
        `for j in range(3):`
            `s = s + str(m[i][j]) + " "`
        
        `print(s)`
    
    `if py[1] <= 0:`
        `p = input("Posicion ficha a eleccion. Ej: 1,0: ")`
    `t = input("Posicion del destino. Ej: 2,0: ")`

    `a = valido(py, m, p, t)`
    `if a == []:`
        `print("salteando")`
        `continue #Saltar iteracion.`
    `else:`
        `m = a #Remplazamos matriz.`
    
    `g = ganador(m)`

    `if g != 0: #Si se encontro ganador.`
        `for i in range(3):`
            `s = "" #Imprimir matriz con formato.`
            `for j in range(3):`
                `s = s + str(m[i][j]) + " "`
            `print(s)`
        `print("El ganador es el jugador: ",g)`
        `break #Sale del bucle.`

    `if f[py[0]-1] > 0: #Si el jugador tiene fichas.`
        `f[py[0]-1] -= 1 #Al jugador actual, le restamos una ficha.`
    `py = cambio(py,f)`

**Tiempo: 1 hora 30 minutos

**_-------------------------------------------------------------------------------------_**

# E26
Beecrow; aliteraciones, deteccion.

El problema consiste en detectar las aliteraciones en una cierta cadena, donde una aliteracion es cuando 2 palabras consecutivas contienen la misma inicial.
Hay que tener en cuenta una limitacion, ya que si varias palabras consecutivas tienen la misma letra de inicial solo se cuenta 1 aliteracion.
Extensión en hoja.

**Codigo:**

`#E26 Beecrow Identificar aliteraciones.`

`#Consiste en identificar iniciales de palabras consecutivas iguales.`

  

`c = input() #Obtener cadena.`

`c = c.upper() #Todos los caracteres valen lo mismo.`

`t = 0 #Total contador.`

`f = False #Flag para evitar repeticiones.`

`s = c[0] #Caracter previo.`

  

`for i in range(len(c)):`

	`if i > 0 and c[i-1] == " " and c[i] != " ": #Si encontro el inicio de la palabra.`
	
		`if s == c[i] and f == False: #Si encontro un patron y no es repetido.`
		
			`t = t+1`
			
			`f = True #Habilitar stop a la repeticion.`
		
		`elif s != c[i]: #Si rompio la secuencia.`
		
			`s = c[i] #Guardamos nuevo caracter previo.`
			
			`f = False #Reiniciamos variable bloqueo.`

`print(t) #Escribir cantidad.`


**Tiempo: 38 Min.**

**_-------------------------------------------------------------------------------------_**

# E27 
Beecrow barajar mazo de cartas.

**Mecánica:** La carta inicial va al descarte y la siguiente atrás del mazo.
**Mostrar:** cartas descartadas en orden y la ultima restante. 

Extensión en papel.


**Algoritmo Básico:**
`m = 1 #Definir cant. a barajar.`

`while m != 0:`

	`m = int(input())`
	
	`if m == 0: #Salida.`
	
		`break`
	
	`a = [0]*m #Array que almacena los valores.`
	
	`for i in range(m):`
	
		`a[i] = i+1 #Valores.`
	
	`c = "" #Descartadas.`
	
	`t = 0 #A mover.`
	
	`co = 0 #Contador.`
	
	`o = 0 #Contador de pasadas.`
	
	`while o < m-1: #Valores concatenados.`
	
		`co += 2`
		
		`o += 1 #Descartes.`
		
		`if o >= m-1:`
		
			`c = c + str(a[0]) #Valor descartado.`
		
		`else:`
		
			`c = c + str(a[0]) + ", " #Valor descartado.`
		
		`t = a[1] #Valor a mover.`
		
		`for i in range(len(a)-co): #Recorrer menos los lugares vacios.`
		
			`a[i] = a[i+2] #Mover por lugares vacios.`
		
		`a[len(a)-co] = t #Almacenar al final.`
		
		`a[(len(a)+1)-co] = 0 #Resetear.`
		
		`co -= 1 #El valor se volvio a ocupar.`
	
	  
	
	`print(f"Discarded cards: {c}")`
	
	`print(f"Remaining card: {a[0]}")`

**Algoritmo Eficiente (MATEMATICAS):**
`#HACERLO EFICIENTE Y SIN NECESIDAD DE ORDENAR: Utilizar MATEMATICAS en base a las potencias de 2. Solo realizar los descartes en base a esa potencia.`

`#Variables: Inicio; indice; potencia; valor de salteo; cadena de descartes => Estas variables son el centro de control para solo iterando linealmente, obtener los valores de descarte de forma ordenada.`

`#Se inicia en el valor de inicio, guardar en cadena de descartes, se le suma el valor de salteo y repite.`

`#Si el valor obtenido en el indice es > a "m", entonces se aumenta el valor de inicio y valor de salteo segun la potencia (va aumentando en 1 en cada final).`

`#Salir si la cant. de descartes es == a m-1.`

`#Al final mostrar cadena .`

`m = 1 #Definir cant. a barajar.`

`while m > 0:`

	`m = int(input())`
	
	`if m == 0:`
	
		`break #Terminar bucle.`
	
	`c = 1 #Contador para descartes.`
	
	`p = 0 #Potencia.`
	
	`s = "" #Cadena descartes.`
	
	`k = 1 #Contador de descartes.`
	
	`r = 0 #Valor restante.`
	
	`par = False #Bandera para saltar descartes.`
	
	`inicio = 0 #Valor donde se iniciara en la proxima etapa, para retomar los valores guardados.`
	
	`#VERIFICAR PARIDAD.`
	
	  
	
	`while k < m: #Mientras aun queden descartes.`
	
		`if par == False:`
		
			`#print("DESCARTADO: ", c)`
		
			`if k+1 == m: #Si llego al ultimo descarte valido.`
		
				`s = s + str(c) #Obtener valor descartado final.`
		
			`else:`
		
				`s = s + str(c) + ", " #Obtener valor descartado en secuencia.`
				
				`k += 1 #Valores descartados.`
		
		
		`if p == 0: #Abordar caso inicial.`
		
			`c += 2 #Saltear entre descartes.`
		
		`else:`
		
			`c += 2 ** p #Potencia de dos.`
		
			`par = not par #Vamor intercalando entre descartes y salteos.`
		
		  
		
		`if c > m: #Si termino la etapa.`
		
			`p += 1 #Aumentamos potencia.`
			
			`c = 2 ** p #Planteamos inicio.`
			
			`if p - 1 > 0: #Asignar cartas anteriores que quedaron.`
			
				`c = inicio #Reasignar inicio.`
			
			  
			
			`if par == False: #Caso general descarte.`
			
				`if p < 2:`
				
					`if m % 2 != 0: #Salteo impar.`
					
						`inicio = inicio + 2 ** p #Planteamos inicio proximo.`
					
					`else:`
					
						`inicio = 2 ** p + 2 ** p #Planteamos inicio proximo potencia.`
			
				`else:`
				
					`inicio = inicio + 2 ** p #Planteamos inicio proximo.`
			
			`#Cuando llega "true", el inicio no se modifica, ya que es una carta que se debe mantener y luego se eliminara.`
			
			`if p-1 == 0 and m % 2 != 0: #Caso inicial.`
			
				`par = True #Lo salteamos al 2 por imparidad.`
				
				`inicio = 2 ** p #Planteamos inicio (2).`
		
		`if k == m: #Si llego al valor final de descartes.`
		
			`#Obtenemos el valor final.`
			
			`if c < inicio:`
			
				`r = c #Si no quedo ninguna carta anterior.`
			
			`else:`
			
				`r = inicio #Si quedo alguna carta anterior.`
	
	`print(f"Discarded cards: {s}")`
	
	`print(f"Remaining card: {r}")`

**Tiempo: 1h 25min**
