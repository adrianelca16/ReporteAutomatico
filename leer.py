import re
import subprocess
import sys

python_path = sys.executable

with open('bulletin_ultimo_evento.txt', 'r') as archivo:
    texto = archivo.readlines()[:7]

    texto1=texto[5].strip()

    lista = texto1.split()

    cantidad = len(lista)

    profundidad = lista[cantidad - 2]
    longitud = lista[cantidad - 4]
    latitud = lista[cantidad - 6]
    hora = lista[cantidad - 7]
    fecha = lista[cantidad - 8]
    magnitudTexto = lista[cantidad - 9]
    magnitud = magnitudTexto.split("=")[1]


# Usamos expresiones regulares para buscar los valores que necesitamos


print(profundidad, latitud, longitud, hora,fecha, magnitud)

    # Llamar a otro script con los valores extraídos
subprocess.call([python_path, 'Azimut.py', '--mag', magnitud, '--lat', f"{latitud}", '--lon', f"{longitud}", '--pro', str(profundidad), '--fec', fecha, '--hor', hora])

