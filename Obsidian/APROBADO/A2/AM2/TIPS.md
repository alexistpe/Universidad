Aqui se detallaran una serie de tips generales de las matematicas, y reglas clave que se utilizan para realizar y simplificar operaciones mas complejas.
## Guia de propiedades basicas de la matematica
> **Potencias:** Reglas para combinar exponentes (sumar en productos, restar en divisiones, multiplicar en potencias de potencias).
    
- **Límites:** El comportamiento de las funciones cuando te acercás a un punto, respetando las operaciones básicas.
    
- **Fracciones:** Cómo operar "paquetes" de números, desde la suma cruzada hasta la multiplicación directa.
    
- **Divisiones:** El arte de repartir el denominador (distributiva) y simplificar términos.
	
- Logaritmos: Calcula el exponente al que se debe elevar la base para obtener el resultado.

---

#### 1. Propiedades de las Potencias (El motor del álgebra)

Para laburar con derivadas parciales, estas reglas son la posta para simplificar antes de derivar:

- **Producto de igual base:** $x^a \cdot x^b = x^{a+b}$
    
- **Cociente de igual base:** $\frac{x^a}{x^b} = x^{a-b}$
    
- **Potencia de otra potencia:** $(x^a)^b = x^{a \cdot b}$
    
- **Distributiva (SOLO en producto y división):** $(x \cdot y)^a = x^a \cdot y^a$ y $(\frac{x}{y})^a = \frac{x^a}{y^a}$.
    
- **Exponente negativo:** $x^{-a} = \frac{1}{x^a}$ (Esto te salva la vida para derivar fracciones como potencias).
    
- **Exponente fraccionario:** $x^{a/b} = \sqrt[b]{x^a}$ (Clave para funciones como la que vimos de la raíz cúbica).
    

---

#### 2. Propiedades de los Límites (El borde de la función)

Si el límite de $f(x,y)$ y $g(x,y)$ existe, entonces se portan bien:

- **Suma y Resta:** $\lim (f \pm g) = \lim f \pm \lim g$
    
- **Producto:** $\lim (f \cdot g) = \lim f \cdot \lim g$
    
- **Cociente:** $\lim (\frac{f}{g}) = \frac{\lim f}{\lim g}$ (siempre que el de abajo no sea cero).
    
- **Constante:** $\lim (k \cdot f) = k \cdot \lim f$
    
- **Potencia:** $\lim (f^g) = (\lim f)^{\lim g}$
    

> **Ojo en Análisis II:** Para que el límite exista en varias variables, te tiene que dar lo mismo por **cualquier camino** que elijas. Si por dos caminos distintos te da diferente, chau, no hay límite.

---

#### 3. Fracciones y Divisiones (Repartiendo el bardo)

- **Suma/Resta (Mariposa):** $\frac{a}{b} \pm \frac{c}{d} = \frac{ad \pm bc}{bd}$
    
- **Multiplicación (Derecho):** $\frac{a}{b} \cdot \frac{c}{d} = \frac{a \cdot c}{b \cdot d}$
    
- **División (Cruzado o "Oreja"):** $\frac{a}{b} : \frac{c}{d} = \frac{a \cdot d}{b \cdot c}$
    
- **Distributiva del denominador:** $\frac{a + b}{c} = \frac{a}{c} + \frac{b}{c}$.
    - _Importante:_ Al revés **NUNCA** se puede: $\frac{c}{a+b} \neq \frac{c}{a} + \frac{c}{b}$.

---
#### Guía de Propiedades de los Logaritmos

Che Alexis, estas son las herramientas que te van a salvar las papas cuando tengas que descular integrales o despejar variables en el parcial de la UTN.

1. **Logaritmo de la unidad**
    $$\log_b(1) = 0$$
    Cualquier número (base) elevado a la $0$ siempre te va a dar $1$.
2. **Logaritmo de la base**
    $$\log_b(b) = 1$$
    En ingeniería vas a ver mucho el logaritmo natural ($\ln$): $\ln(e) = 1$, porque la base es el mismo número $e$.
3. **Logaritmo de un producto**
    $$\log_b(M \cdot N) = \log_b(M) + \log_b(N)$$
    Si tenés cosas multiplicándose adentro, las podés separar sumando.
4. **Logaritmo de un cociente**
    $$\log_b\left(\frac{M}{N}\right) = \log_b(M) - \log_b(N)$$
    Esta es clave. La usamos recién para resolver la integral de $\frac{1}{x+1} - \frac{1}{x+2}$ y llegar al resultado final de $\ln(25/24)$.
5. **Logaritmo de una potencia**
    $$\log_b(M^k) = k \cdot \log_b(M)$$
    Esta es la propiedad "baja-exponente". En los ejercicios de **Extremos Condicionados**, cuando tenés algo como $e^x = e^{2-x}$, aplicás $\ln$ a ambos lados y los exponentes bajan para que los puedas despejar tranqui.
6. **Logaritmo de una raíz**
    $$\log_b(\sqrt[n]{M}) = \frac{1}{n} \log_b(M)$$
    Acordate que una raíz es lo mismo que un exponente fraccionario ($M^{1/n}$), así que es una derivada de la propiedad anterior.
7. **Cambio de base**
    $$\log_b(a) = \frac{\log_c(a)}{\log_c(b)}$$
    Generalmente se usa para pasar todo a base $e$ ($\ln$) o base $10$, que son las que manejan las calculadoras y los lenguajes de programación que usás en Sistemas.

---



## Encontrar fracciones para cualquier entero
El mecanismo es muy simple, consiste en poner el numero en el numerador y decimos en el denominador:
- Obtener numero original entero sin comas: 
	- Ubicar en el numerador.
- Obtener cantidad de numeros luego de la coma en el numero original.
	- Poner un uno seguido por esa cantidad en "ceros".

Mediante este proceso se puede convertir cualquier numero en fraccion, permitiendo simplificarlo luego mediante divisiones sucesivas en ambos miembros (numerador y denominador).

Ejemplos: 
- 1,58 = 158/100 = 79/50
- Se ponen ceros despues del uno segun la cantidad de numeros luego de la coma en el numero original.
- Consiste en una division basica en base a los "dieces".
