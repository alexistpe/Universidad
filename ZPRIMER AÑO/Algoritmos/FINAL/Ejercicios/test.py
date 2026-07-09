import time
import random

# Tu Quicksort casero (versión 2 con 'm' en el medio)
def QuickCasero(s):
    t = len(s)
    if t <= 1: # Simplificado para el benchmark
        return s
    else:
        s1, s2, m = [], [], []
        val = s[t // 2]
        for x in s:
            if x < val: s1.append(x)
            elif x > val: s2.append(x)
            else: m.append(x)
        return QuickCasero(s1) + m + QuickCasero(s2)

# Algoritmo Burbuja para comparar (El "lento")
def BubbleSort(s):
    n = len(s)
    v = s.copy()
    for i in range(n):
        for j in range(0, n - i - 1):
            if v[j] > v[j + 1]:
                v[j], v[j + 1] = v[j + 1], v[j]
    return v

def medir_tiempo(algoritmo, datos):
    inicio = time.perf_counter()
    algoritmo(datos)
    fin = time.perf_counter()
    return (fin - inicio) * 1000 # Convertido a milisegundos

# --- PRUEBA DE RENDIMIENTO ---
tamanos = [10, 100, 1000, 10000, 20000, 100000, 1000000, 10000000] # Cantidad de números a ordenar

print(f"{'Tamaño':<10} | {'QuickCasero (ms)':<20} | {'BubbleSort (ms)':<20}")
print("-" * 55)

for n in tamanos:
    # Generamos una lista aleatoria para la prueba
    test_data = [random.randint(0, 10000) for _ in range(n)]
    
    t_quick = medir_tiempo(QuickCasero, test_data)
    #t_bubble = medir_tiempo(BubbleSort, test_data)
    
    print(f"{n:<10} | {t_quick:<20.4f}")
