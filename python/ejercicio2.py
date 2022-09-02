''' sintaxis de range(inicio <opcional>,fin <obligatorio>,incremento <opcional>)
'''

# Ejercicio 1: iterar un rango de 0 a 10 e imprimir numeros divisibles por 3
# Ejemplo: 0,3,6,9

for i in range(0,11,3):
    print(i)
else:
    print("Terminado ejercicio 1")  #se puede hacer tambien con i % 3 ==0

#Ejercicio 2: crear un rango de numeros de 2 a 6 e imprimelos
# ejemplo de ejecucion: 2,3,4,5,6

for i in range(2,7):
    print(i)
else:
    print("Terminado ejercicio 2")

#Ejercicio 3: Crear un rango de 3 a 10 pero con incremento de 2 en 2
#ejemplo: 3,5,7,9

for i in range(3,11,2):
    print(i)
else:
    print("Terminado ejercicio 3")