import subprocess


with open ('bulletin_ultimo_evento.txt', 'r') as archivo:
    lineas = archivo.readlines()
    linea = lineas[5].strip().split()
    magnitud = linea[4].split("=")[1]
    latitud = linea[7]
    longitud = linea[9]
    profundidad = linea[11]
    fecha = linea[5]
    hora = linea[6]

    if float(profundidad) == 0:
        profundidad = "5.0"
subprocess.run(['python', 'Azimut.py', '--mag', str(magnitud), '--lat', str(latitud), '--lon',str(longitud), '--pro',str(profundidad), '--fec', str(fecha), '--hor', str(hora)])  # Ejecuta el