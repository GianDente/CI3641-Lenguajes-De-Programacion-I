# Programa que implementa y compara las versiones recursivas, recursivas de cola e iterativa de una familia de funciones.
# Giancarlo Dente
# 15-10395

import time 

# Version recursiva, traducida de la formula dada:
def Frecursiva(n: int):

	if 0 <= n < 35:
		return n 
	elif n >= 35:
		return Frecursiva(n-7) + Frecursiva(n-14) + Frecursiva(n-21) + Frecursiva(n-28) + Frecursiva(n-35)

# Version recursiva de cola:
def FrecursivaCola(n:int, lista_aux: list, i=0):
    if 0 <= n < 35:
        return lista_aux[n+i]
    elif n >= 35:
        # vamos ampliando la lista con elementos del caso base y con los calculados en la llamada recursiva anterior.
        lista = lista_aux[0+i]+lista_aux[7+i]+lista_aux[14+i]+lista_aux[21+i]+lista_aux[28+i]
        lista_aux.append(lista)
        return FrecursivaCola(n-1, lista_aux, i+1)
       
# Version iterativa, correspondiente a la recursion de cola:
def Fiterativo(n: int):

    lista_aux = []
    for i in range(0,35):
        lista_aux.append(i)
    
    if 0 <= n < 35:
        return n
    elif n >= 35:
    	for j in range(35, n+1):
            i = j-35
            lista = lista_aux[0+i]+lista_aux[7+i]+lista_aux[14+i]+lista_aux[21+i]+lista_aux[28+i]
            lista_aux.append(lista)
    	return lista_aux[len(lista_aux)-1]
        

     
#####################################################################################################################

# Distintos valores de entrada:
valores = int(input("Valor de n: "))
slices = int(input())

lista_valores = []
for i in range(0, valores+slices, slices):
    lista_valores.append(i)

print("\n")   
for n in lista_valores:

  	# Version Recursiva
    inicio = time.time()
    resultado_recursivo = Frecursiva(n)
    fin = time.time()

    print(f"F recursivo de {n}: {resultado_recursivo}")
    print(f"Con tiempo de ejecucion: {fin-inicio}" "\n")

print("\n")
print("--------------------------------")
for n in lista_valores:

    # Version recursiva de cola
    inicio = time.time()
    resultado_cola = FrecursivaCola(n, [i for i in range(0, 35)])
    fin = time.time()

    print(f"F recursivo de cola de {n}: {resultado_cola}")
    print(f"Con tiempo de ejecucion: {fin-inicio}" "\n")

print("\n")
print("--------------------------------")
for n in lista_valores:

	# Version iterativa
    inicio = time.time()
    resultado_iterativo = Fiterativo(n)
    fin = time.time()

    print(f"F iterativo de {n}: {resultado_iterativo}")
    print(f"Con tiempo de ejecucion: {fin-inicio}" "\n")

