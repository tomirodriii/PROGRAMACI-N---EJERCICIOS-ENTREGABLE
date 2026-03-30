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
    p = input("Ingrese una palabra: ").lower()
    if p == "":
        seguir = False
    else:
        palabras.append(p)


while otra_op:
    opcion = input("\nIngrese una opcion (Contar, Modificar, Eliminar, Mostrar o Terminar): ").lower()

    if opcion == "terminar":
        otra_op = False
        print("Gracias por usar el programa!")

    elif opcion == "contar":
         print(len(palabras))

    elif opcion == "modificar":
        input_mod = input("Ingrese la palabra a modificar: ").lower()
        input_mod2 = input("Ingrese la nueva palabra: ").lower()

        encontrada = False

        for i in range(len(palabras)):
            if palabras[i] == input_mod:
                palabras[i] = input_mod2
                encontrada = True

        if not encontrada:
            print("Palabra no encontrada")
        else:
            print("Lista actualizada:", palabras)

    elif opcion == "eliminar":
        input_elim = input("Ingrese la palabra a eliminar: ").lower()
        
        if input_elim in palabras:
            while input_elim in palabras:
                palabras.remove(input_elim)
            print("Lista actualizada:", palabras)
        else:
            print("Palabra no encontrada")

    elif opcion == "mostrar":
        print("Lista:", palabras)

