Aca se dictaran los ejercicios practicos diarios para repasar y consolidar los temas mediante que los repaso.
## Clasificacion de dificultad en temas:
- **Valores extremos: Repaso intenso.**
- **Derivada direccional: Intenso.**
- **Integrales dobles: Intenso.**
- Derivada funciones vectoriales: Medio/constante.
- Funciones vectoriales: Repaso basico.
	- Aqui me debo asegurar que no hay temas mas complejos, debo practicar para sacarme la duda.

### Repasos necesarios:
- En curvas de nivel, necesito practicar todas las diferentes figuras y poder determinar cual es.
- Necesito aprender a graficar la region a integrar, osea las funciones y sus valores.

---
# Dia 1
- **Función Vectorial Real ($\mathbb{R}^n \rightarrow \mathbb{R}$):** Entran varias coordenadas, pero sale **un solo número**. Es ideal para medir cosas estáticas en un mapa (ejemplo: la temperatura o la altura exacta en una coordenada).
    
- **Función Vectorial de Variable Real ($\mathbb{R} \rightarrow \mathbb{R}^n$):** Entra un solo número (generalmente el tiempo $t$) y sale **un vector o coordenada**. Sirve para trazar trayectorias o caminos (ejemplo: dónde está ubicado un dron en el segundo 5).
    
- **Campo Vectorial ($\mathbb{R}^n \rightarrow \mathbb{R}^n$):** Entra una coordenada y sale **otro vector**. Se usa para modelar flujos donde cada punto del espacio tiene una flecha con dirección y fuerza (ejemplo: el mapa de vientos en un simulador o la corriente de un río).
    

---

### 1. Ejercicio de Función Vectorial Real (Campo Escalar)

**El concepto en la vida real:** Imaginate una plancha de metal donde el calor está distribuido de forma despareja. Querés saber qué temperatura hace en un punto exacto.

**El Ejercicio:**

La temperatura en una plancha metálica está dada por la función $T(x,y) = 3x^2 + 2y$.

Calculá la temperatura exacta en la coordenada $P(2, 4)$.

**Resolución:**

Como es una función $\mathbb{R}^2 \rightarrow \mathbb{R}$, simplemente reemplazamos las variables de entrada por los números de la coordenada y resolvemos la cuenta para obtener un único valor escalar.

1. Reemplazamos $x=2$ e $y=4$:
    
    $T(2, 4) = 3(2)^2 + 2(4)$
    
2. Resolvemos:
    
    $T(2, 4) = 3(4) + 8$
    
    $T(2, 4) = 12 + 8 = \mathbf{20}$
    

**Resultado:** En la coordenada $(2,4)$, la temperatura es de $20$ grados.

---

### 2. Ejercicio de Función Vectorial de Variable Real

**El concepto en la vida real:** Tenés un auto a control remoto y querés saber exactamente en qué latitud y longitud del patio va a estar parado a los 3 segundos de haber arrancado.

**El Ejercicio:**

La posición de un objeto en movimiento depende del tiempo $t$ (medido en segundos) y está dictada por la función vectorial $\vec{r}(t) = (t^2, \quad 5t - 1)$.

Encontrá el vector de posición del objeto en el instante $t = 3$.

**Resolución:**

Acá nuestra única entrada es un escalar (el tiempo $t=3$). Lo metemos adentro de cada componente del vector para que nos devuelva la coordenada de salida.

1. Reemplazamos $t=3$ en la primera componente ($x$): $(3)^2 = 9$
    
2. Reemplazamos $t=3$ en la segunda componente ($y$): $5(3) - 1 = 15 - 1 = 14$
    

**Resultado:** A los 3 segundos, el objeto se encuentra en la coordenada $\mathbf{(9, 14)}$.

---

### 3. Ejercicio de Función de Campo (Campo Vectorial)

**El concepto en la vida real:** Estás viendo un mapa del clima en la tele. En cada ciudad del país hay dibujada una flecha que te dice hacia dónde sopla el viento y con qué fuerza.

**El Ejercicio:**

El flujo del viento en un valle está modelado por el campo vectorial $\vec{V}(x,y) = (-y, \quad x)$.

Determiná el vector del viento que está soplando exactamente sobre la coordenada $P(2, 0)$.

**Resolución:**

Acá entra un punto del plano (una coordenada) y la función te devuelve un vector (una flecha de velocidad/fuerza) .

1. Tomamos nuestra entrada $x=2$ e $y=0$.
    
2. Miramos la primera salida de la función (que dice que vale $-y$): Como $y=0$, esto nos da $0$.
    
3. Miramos la segunda salida de la función (que dice que vale $x$): Como $x=2$, esto nos da $2$.
    
4. Armamos el vector de salida: $(0, 2)$
    

**Resultado:** Si te parás en la coordenada $(2,0)$, el viento te va a pegar con un vector de fuerza $\mathbf{(0, 2)}$. O sea, un viento que no te empuja nada para los costados, pero te empuja 2 unidades directo hacia el Norte.

# Dia 2

**Resumen de la guía de práctica:**

- **Curvas de Nivel:** El objetivo es "rebanar" la función $z = f(x,y)$ para ver qué dibujos se forman en el piso.
    
- **Superficies de Nivel:** Subimos de dimensión. Ahora rebanamos $f(x,y,z) = k$ para encontrar "cáscaras" tridimensionales.
    
- **Límites y Continuidad:** Vamos a testear si la función está "rota" o es una sola pieza usando los métodos de aproximación (iterados, radiales y simultáneos).
    

---

### 1. Curvas de Nivel (En el plano $\mathbb{R}^2$)

**Problema A:** Dada la función $f(x,y) = \sqrt{100 - x^2 - y^2}$:

1. Hallá las ecuaciones de las curvas de nivel para $k = 0$, $k = 6$ y $k = 8$.
    
2. Identificá de qué figuras geométricas se trata y graficalas en un mismo plano.
    
3. Determiná el dominio de la función (el "techo" de $k$ que no podés superar).
    

**Problema B:** Dada la función $f(x,y) = y - x^2$:

1. Hallá la curva de nivel que pasa por el punto $P(2, 5)$.
    
2. Despejá $y$ para ver qué forma tiene esa curva (pista: pensá en las cónicas que vimos).
    

---

### 2. Superficies de Nivel (En el espacio $\mathbb{R}^3$)

**Problema A:** Considerá el campo escalar $f(x,y,z) = x^2 + y^2 - z$:

1. Determiná la ecuación de la superficie de nivel para $k = 4$.
    
2. Si "congelamos" la $z$ en esa superficie, ¿qué curvas de nivel verías si la miraras desde arriba?
    
3. ¿Cómo se llama esta superficie? (Usá el machete de superficies que vimos antes).
    

**Problema B:** Para la función $f(x,y,z) = 2x + 4y - z$:

1. Hallá la superficie de nivel para $k = 10$.
    
2. ¿Qué tipo de figura geométrica es? (Pista: las variables están todas lineales).
    

---

### 3. Límites y Continuidad

**Problema A (Existencia):** Calculá el siguiente límite mediante el método de los **límites sucesivos (iterados)**:

$$\lim_{(x,y) \to (0,0)} \frac{x^2 - y^2}{x^2 + y^2}$$

1. Calculá $L_1$ (primero $y \to 0$, luego $x \to 0$).
    
2. Calculá $L_2$ (primero $x \to 0$, luego $y \to 0$).
    
3. A partir de tus resultados, dictaminá si el límite doble existe.
    

**Problema B (Radial):** Probá si existe el límite de la función $f(x,y) = \frac{x \cdot y}{x^2 + y^2}$ en el origen, utilizando el método **radial** ($y = mx$).

**Problema C (Continuidad):** Analizá la continuidad de la siguiente función en el punto $(0,0)$:

$$f(x,y) = \begin{cases} \frac{x^3 + y^3}{x^2 + y^2} & \text{si } (x,y) \neq (0,0) \\ 0 & \text{si } (x,y) = (0,0) \end{cases}$$

_(Ayuda: para el límite simultáneo, probá usar coordenadas polares $x = r \cos(\theta), y = r \sin(\theta)$)._

¿Por cuál de estos te gustaría empezar a resolver para que lo vayamos controlando juntos?

# Dia 3
Seguí el orden para ir desde lo básico hasta la optimización total.

**Síntesis de los temas a ejercitar:**

- **Derivadas y Jacobiano:** Herramientas para medir el cambio en funciones escalares y vectoriales.
    
- **Diferencial e Incremento:** Aproximación lineal vs. cambio real de la función.
    
- **Gradiente y Dirección:** La brújula del máximo crecimiento y el cálculo de pendientes en cualquier sentido.
    
- **Extremos y Hessian:** Detección de puntos críticos y su clasificación en máximos, mínimos o sillas.
    
- **Lagrange:** Optimización de funciones que están "atadas" a una restricción o condición específica.
    

---

### Bloque 1: Derivadas, Jacobiano y Diferenciales

**Ejercicio 1 (Escalar):**

Dada la función $f(x, y) = \ln(x^2 + y^2)$:

1. Hallar las derivadas parciales de primer orden $f_x$ y $f_y$.
    
2. Calcular el **incremento** $\Delta f$ y el **diferencial total** $df$ al pasar del punto $A(1, 0)$ al punto $B(1.1, 0.1)$.
    

**Ejercicio 2 (Vectorial):**

Sea la función vectorial $\vec{f}: \mathbb{R}^2 \rightarrow \mathbb{R}^2$ definida por $\vec{f}(x, y) = (x^2 - y^2, 2xy)$:

1. Calcular la **Matriz Jacobiana** $J$ en cualquier punto $(x, y)$.
    
2. Evaluar $J$ en el punto $(1, 2)$.
    

---

### Bloque 2: Gradiente y Derivada Direccional

**Ejercicio 3:**

Dada la superficie $f(x, y) = x^2 e^y$:

1. Calcular el vector **gradiente** $\nabla f$ en el punto $P(2, 0)$.
    
2. Hallar la **derivada direccional** en $P$ en la dirección del vector $\vec{v} = (3, 4)$. _Ojo acá:_ acordate de normalizar el vector para que sea un versor $\hat{u}$.
    
3. ¿Cuál es la dirección de **máximo crecimiento** en $P$ y cuál es el valor de esa pendiente máxima?.
    

---

### Bloque 3: Valores Extremos (Sin Restricciones)

**Ejercicio 4:**

Hallar y clasificar los puntos críticos de la función:

$$f(x, y) = x^3 + 3xy^2 - 15x - 12y$$

1. Encontrá los **puntos críticos** igualando el gradiente a cero ($\nabla f = \vec{0}$).
    La cantidad de puntos criticos puede variar, ya que puede no haber, como pueden ser infinitos.
    Depende las formas de encontrarlos: Igualando a "0" o buscando una forma de que la funcion devuelva un indeterminacion.
    Se despejan las funciones derivadas igualadas a cero y se realiza un sistema de ecuaciones y luego se opera hasta llegar a el resultado de las raices.
    **Definición de Punto Crítico (PC):** Es un punto (x0​,y0​) del dominio donde se da una de dos situaciones: el gradiente es cero (∇f=0) o el gradiente no existe (∄∇f).
2. Armá la matriz **Hessiana** y calculá su determinante $D$ para cada punto.
    
3. Clasificá cada punto como **mínimo relativo, máximo relativo o punto silla**.
    

---

### Bloque 4: Extremos Condicionados (Lagrange)

**Ejercicio 5:**

Se desea encontrar los puntos más altos y más bajos de una placa circular cuya temperatura está dada por $T(x, y) = xy + 20$.

La placa ocupa la región definida por la restricción $x^2 + y^2 = 8$.

1. Planteá el sistema de ecuaciones usando el método de los **Multiplicadores de Lagrange**: $\nabla T = \lambda \nabla g$ (siendo $g$ la restricción).
    
2. Hallar los puntos $(x, y)$ que cumplen el sistema.
    
3. Determinar cuáles son los **extremos absolutos** evaluando la función $T$ en esos puntos.

## Integrales dobles:
### Ejercicio 1: Volumen en Regiones Rectangulares

Calculá el volumen del sólido formado por la superficie $f(x, y) = 1 - 6x^2y$ sobre la región rectangular definida por $0 \le x \le 2$ y $-1 \le y \le 1$.

> **Tip:** Como es un rectángulo, podés aplicar el Teorema de Fubini e integrar en el orden que más te guste ($dxdy$ o $dydx$), el resultado no debería cambiar.

---

### Ejercicio 2: Volumen Verticalmente Simple (Tipo I)

Evaluar la integral doble $\iint (x + 2y) dA$ donde la región $R$ está limitada por la parábola $y = x^2$ y la recta $y = x + 2$.

1. **Paso 1**: Identificá los puntos de intersección para fijar los límites de $x$.
    
2. **Paso 2**: Definí quién es el "piso" ($g_1$) y quién es el "techo" ($g_2$) en el eje $y$.
    
3. **Asociación**: Imaginalo como calcular el peso de una chapa que no tiene un espesor parejo, sino que se va haciendo más pesada (la función $x + 2y$) a medida que te alejás del origen.
    

---

### Ejercicio 3: Volumen Horizontalmente Simple (Tipo II)

Evaluar la integral doble de la función $f(x, y) = 1 + x + y$ en la región $R$ limitada por las rectas $y = -x$, $y = x$ e $y = 2$.

- Para que sea **Horizontalmente Simple**, tenés que despejar $x$ en función de $y$ en las rectas.
    
- Planteá la integral externa con los límites constantes de $y$ (de $0$ a $2$) y la interna con las funciones de $x$.
    

---

### Ejercicio 4: Cálculo de Área

Hallar el área del recinto (Dominio B) limitado por la parábola $y = \frac{x^2}{2}$ y la recta superior $y = 2$.

- Recordá que para que el resultado sea un área, la función dentro de la integral debe ser $f(x, y) = 1$.
    
- **Planteo**: $A = \iint_D dA = \int_{a}^{b} dx \int_{g_1(x)}^{g_2(x)} dy$.
    

---

### Ejercicio de "Final": Combinado

Calculá el volumen del sólido limitado en la parte superior por el plano $z = 2 - x - 2y$ y en el plano $xy$ por la región limitada por los ejes y la recta $y = -\frac{1}{2}x + 1$.

- **Resultado esperado**: $2/3$.
    
- Este ejercicio es clave porque te obliga a dibujar la región en el plano $xy$ antes de siquiera tocar la integral.
    

**Ojo al piojo:** No te olvides de lo que hablamos antes; si pifiás el orden de las funciones en los límites (ponés la de arriba abajo), el volumen te va a dar negativo y en el parcial te van a mirar con cara de pocos amigos.