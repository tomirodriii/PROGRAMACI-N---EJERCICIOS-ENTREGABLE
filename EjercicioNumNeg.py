# Crear un programa que añada números a una lista hasta que introducimos un número negativo. 
# A continuación debe crear una nueva lista igual que la anterior pero eliminando los 
# números duplicados. Muestra esta segunda lista para comprobar que hemos eliminados los duplicados.

import os
os.system("cls")

numeros = []
while True:
    num = int(input("Introduce un número ( o negativo para terminar): "))
    if num < 0:
        break
    numeros.append(num)
    
numeros_sin_duplicados = list(set(numeros))
print("Lista sin duplicados:", numeros_sin_duplicados)