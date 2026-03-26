# Crear un programa de ordenador para gestionar los resultados de la quiniela de fútbol.
# Para ello vamos a utilizar dos tablas:
# 
# * Equipos: Que es una tabla de cadenas donde guardamos en cada columna el nombre de 
# los equipos de cada partido. En la quiniela se indican 15 partidos.
# * Resultados: Es una tabla de enteros donde se indica el resultado. 
# También tiene dos # columnas, en la primera se guarda el número de goles del equipo 
# que está guardado en la primera columna de la tabla anterior, y en la segunda los goles 
# del otro equipo.
# 
# El programa ira pidiendo los nombres de los equipos de cada partido y el resultado 
# del partido, a continuación se imprimirá la quiniela de esa jornada.
# 
# ¿Qué modificación habría que hacer en las tablas para guardar todos los resultados 
# de todas las jornadas de la temporada?

import os
os.system("cls")

equipos = []
resultados = []
for i in range(15):
    equipo1 = input(f"Introduce el nombre del equipo 1 {i+1}: ")
    equipo2 = input(f"Introduce el nombre del equipo 2 {i+1}: ")
    equipos.append((equipo1, equipo2))
    
    goles1 = int(input(f"Introduce los goles de {equipo1}: "))
    goles2 = int(input(f"Introduce los goles de {equipo2}: "))
    resultados.append((goles1, goles2))
    
    