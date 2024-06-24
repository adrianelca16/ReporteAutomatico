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
    if profundidad == "0":
        profundidad = 5
    longitud = lista[cantidad - 4]
    latitud = lista[cantidad - 6]
    hora = lista[cantidad - 7]
    fecha = lista[cantidad - 8]
    magnitudTexto = lista[cantidad - 9]
    magnitud = magnitudTexto.split("=")[1]


# Usamos expresiones regulares para buscar los valores que necesitamos


<<<<<<< HEAD
if resultado:
    magnitud = resultado.group(1)
    latitud = resultado.group(2)
    longitud = resultado.group(4)
    profundidad_texto = resultado.group(6)
    fecha_hora = resultado.group(7)

    # Dividir la cadena de fecha y hora
    fecha, hora = fecha_hora.split()


    # Extraer solo el valor numérico de la profundidad
    profundidad_numerica = re.search(r"(\d+)\s+km", profundidad_texto)
    if profundidad_numerica:
        profundidad = float(profundidad_numerica.group(1))
    else:
        print("No se pudo extraer la profundidad del formato esperado.")
        profundidad = 0.0
=======
print(profundidad, latitud, longitud, hora,fecha, magnitud)
>>>>>>> a12c3bf4eb217a1ac14e6b1233c66f5efb52ae5b

    # Llamar a otro script con los valores extraídos
subprocess.call([python_path, 'Azimut.py', '--mag', magnitud, '--lat', f"{latitud}", '--lon', f"{longitud}", '--pro', str(profundidad), '--fec', fecha, '--hor', hora])

