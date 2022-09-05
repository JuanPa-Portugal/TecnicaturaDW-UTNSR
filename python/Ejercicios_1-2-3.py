'''
     ---- Martin Verstraeten // Grupo Codestyle - UTN SRb 2022 ----
Ejercicio 1:
- Iterar un rango de 3 a 10 e imprimir numeros divisibles entre 3
(Ejemplp de ejecucion: 0,3,6,9
'''
print('-- Ejercicio 1 --')
print('--- Iterar un rango de 3 a 10 e imprimir numeros divisibles entre 3. (0,3,6,9) ---')

for i in range(11):
    if i % 3 == 0:
        print(i)

'''
Ejercicio 2:
- Crear un rango de numeros de 2 a 6 e imprimirlos.
(Ejemplp de ejecucion: 2,3,4,5,6
'''
print('')
print('-- Ejercicio 2 --')
print('--- Crear un rango de numeros de 2 a 6 e imprimirlos. (2,3,4,5,6) ---')

for i in range(2,7):
    print(i)

'''
Ejercicio 1:
- Crear un rango de 3 a 10 pero con incremento de 2 en 2.
(Ejemplo de ejecucion: 3,5,7,9
'''
print('')
print('-- Ejercicio 3 --')
print('--- Crear un rango de 3 a 10 pero con incremento de 2 en 2. (3,5,7,9) ---')

for i in range(3,11,2):
    print(i)