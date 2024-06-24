import re
import subprocess
import sys


python_path = sys.executable

with open('bulletin_ultimo_evento.txt', 'r') as archivo:
    texto = archivo.read()

# Usamos expresiones regulares para buscar los valores que necesitamos
patron = r"MLv=(\d+\.\d+).*?(\d+\.\d+)\s([NS])\s+(\d+\.\d+)\s([WE]).*?(\d+\s+km).*?(\d+/\d+/\d+\s+\d+:\d+:\d+\.\d+)"

resultado = re.search(patron, texto, re.DOTALL)

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

    # Llamar a otro script con los valores extraídos
    subprocess.call([python_path, 'Azimut.py', '--mag', magnitud, '--lat', f"{latitud}", '--lon', f"{longitud}", '--pro', str(profundidad), '--fec', fecha, '--hor', hora])
else:
    print("No se encontraron los valores necesarios en el archivo.")
