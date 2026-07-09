def luhn_check(s):
    """
    Verifica si un número de tarjeta es válido según el Algoritmo de Luhn.
    Se ejecuta de forma regresiva (de derecha a izquierda).
    """
    # 1. Ejecutar de forma regresiva: Invertimos el string para iterar de derecha a izquierda.
    s_reversa = s[::-1]
    suma_total = 0
    
    for i, char_digito in enumerate(s_reversa):
        # Convertir el carácter a entero
        digito = int(char_digito)
        
        # 2. Desde el segundo dígito (índice 1, 3, 5... en el string invertido)
        if i % 2 != 0: 
            # Duplicar el valor
            duplicado = digito * 2
            
            # Si es mayor que 9, restar 9 (equivalente a sumar los dígitos)
            if duplicado > 9:
                digito_final = duplicado - 9
            else:
                digito_final = duplicado
            
            suma_total += digito_final
        
        else:
            # Los dígitos no duplicados
            suma_total += digito

    # 3. Si el total es múltiplo de 10, es válido (suma % 10 == 0)
    return suma_total % 10 == 0


def validar_tarjetas():
    """
    Función principal para leer N tarjetas y contar las inválidas.
    """
    # Recibir n (Cantidad de tarjetas)
    try:
        n = int(input())
    except ValueError:
        # Manejo de entrada no numérica para n
        return

    # Definir T (cantidad de tarjetas INVÁLIDAS)
    T = 0 

    # Evaluar cada una de las 'n' tarjetas
    for _ in range(n):
        s = input().strip()
        
        # Control básico: la entrada debe ser numérica.
        if not s.isdigit() or len(s) == 0:
            # Si no es un número válido, lo contamos como inválido y pasamos al siguiente.
            T += 1
            continue

        # Aplicar el Algoritmo de Luhn
        es_valida = luhn_check(s)
        
        # Si NO es válida, incrementar el contador T
        if not es_valida:
            T += 1

    # Salida: El programa debe mostrar al finalizar el proceso únicamente 
    # un número que represente la cantidad de tarjetas inválidas detectadas.
    print(T)

# Ejecutar la función para iniciar el programa
# Nota: La entrada/salida se gestiona directamente en la consola sin mensajes intermedios.
validar_tarjetas()