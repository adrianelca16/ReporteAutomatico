import math
import pandas as pd
import argparse
import subprocess
# Radio de la Tierra en kilómetros
radio_tierra = 6371.0

# Función para calcular la distancia haversine entre dos puntos en kilómetros
def calcular_distancia(lat1, lon1, lat2, lon2):
    # Convertir grados a radianes
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    # Diferencia de latitud y longitud
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    # Fórmula de la distancia haversine
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distancia = radio_tierra * c
    return distancia

# Función para calcular el azimut entre dos puntos en grados
def calcular_azimut(lat1, lon1, lat2, lon2):
    delta_lon = lon2 - lon1
    y = math.sin(delta_lon) * math.cos(lat2)
    x = math.cos(lat1) * math.sin(lat2) - math.sin(lat1) * math.cos(lat2) * math.cos(delta_lon)
    azimut = math.atan2(y, x)
    azimut_grados = math.degrees(azimut)
    return azimut_grados

# Función para obtener la dirección cardinal a partir de un azimut en grados
def obtener_direccion(azimut):
    # Dividir el círculo en octantes
    octantes = ['N', 'NE', 'E', 'SE', 'S', 'SO', 'O', 'NO', 'N']

    # Calcular el índice del octante
    octante_index = round(azimut / (360.0 / len(octantes))) % len(octantes)

    # Devolver la dirección cardinal correspondiente al octante
    return octantes[octante_index]

if __name__ == "__main__":
    # Parsear los argumentos de la línea de comandos
    parser = argparse.ArgumentParser(description='Calcula las distancias y direcciones desde un punto fijo a ciudades.')
    parser.add_argument('--lat', type=float, help='Latitud del punto fijo')
    parser.add_argument('--lon', type=float, help='Longitud del punto fijo')
    parser.add_argument('--mag', type=float, help='Longitud del punto fijo')
    parser.add_argument('--pro', type=float, help='Longitud del punto fijo')
    parser.add_argument('--fec', type=str, help='Longitud del punto fijo')
    parser.add_argument('--hor', type=str, help='Longitud del punto fijo')
    args = parser.parse_args()

    lat_punto_fijo = args.lat
    lon_punto_fijo = -abs(args.lon)

    # Leer el archivo
    ciu = pd.read_csv("./assets/ciu.txt", sep='\s+')

    # Obtener las columnas de latitud, longitud y nombres de las ciudades
    latitudes = ciu['Lat']
    longitudes = ciu['Lon']
    ciudades = ciu['Nombre']

    # Lista para almacenar las distancias y direcciones
    distancias = []
    direcciones = []

    # Calcular las distancias y direcciones y almacenarlas en las listas correspondientes
    for lat, lon in zip(latitudes, longitudes):
        distancia = calcular_distancia(lat_punto_fijo, lon_punto_fijo, lat, lon)
        azimut = calcular_azimut(lat_punto_fijo, lon_punto_fijo, lat, lon)
        direccion = obtener_direccion(azimut)
        distancias.append(distancia)
        direcciones.append(direccion)

    # Ordenar las distancias y obtener los índices de las dos distancias más bajas
    indices_distancias_bajas = sorted(range(len(distancias)), key=lambda i: distancias[i])[:2]

    resultados = []
    # Mostrar las dos distancias más bajas, sus coordenadas correspondientes y direcciones
    for indice in indices_distancias_bajas:
        distancia = distancias[indice]
        lat = latitudes[indice]
        lon = longitudes[indice]
        direccion = direcciones[indice]
        nomCiu = ciudades[indice]

        azimut = calcular_azimut(lat_punto_fijo, lon_punto_fijo, lat, lon) 

        resultado = f"Distancia: {round(distancia)} km hacia el {direccion} desde {nomCiu} (Azm. {round(azimut)})"

        resultados.append(resultado)
    
    subprocess.run(['python', 'reporteAutomatico.py', '--mag', str(args.mag), '--lat', str(args.lat), '--lon',str(args.lon), '--pro',str(args.pro),'--fec',str(args.fec) ,'--hor',str(args.hor),'--azm1',str(resultados[0]), '--azm2', str(resultados[1])])
    print(resultados)
