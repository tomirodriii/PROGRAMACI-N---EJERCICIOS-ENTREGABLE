# Escriba un programa que permita crear una lista de palabras y que, a continuación de tres opciones:

# * Contar: Me pide una cadena, y me dice cuantas veces aparece en la lista
# * Modificar: Me pide una cadena, y otra cadena a modificar, y modifica todas alas apariciones de la primera por la 
# segunda en la lista.
# * Eliminar: Me pide una cadena, y la elimina de la lista.
# * Mostrar: Muestra la lista de cadenas
# * Terminar

import os
os.system("cls")

palabras = []

seguir = True
otra_op = True

while seguir:
    p = input("Ingrese una palabra:").lower()
    if p == "":
        seguir = False
    else:
        palabras.append(p)


while otra_op: 
    opcion = input("Ingrese una opcion (Contar, Modificar, Eliminar, Mostrar o Terminar):").lower()

    if opcion == "terminar":
        otra_op = False
        print("Gracias por jugar!")
        
    elif opcion == "contar":
        print(len(palabras))
        
    elif opcion == "modificar":
        input_mod = input("Ingrese la palabra a modificar:").lower()
        input_mod2 = input("Ingrese la palabra la modificacion:").lower()
        for i,palabra in enumerate(palabras):
            if input_mod == palabras[i]:
                palabras[i] = input_mod2
            else:
                print("Palabra no encontrada")
                
    elif opcion == "eliminar":
        input_elim = input("Ingrese la palabra a eliminar:").lower()
        for i in palabras:
            if i == input_elim:
                palabras.remove(i)
                
    elif opcion == "mostrar":
        print(palabras)
        
    