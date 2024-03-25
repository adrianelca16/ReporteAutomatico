import math
import pandas as pd

# Radio de la Tierra en kilómetros
radio_tierra = 6371.0

lat_punto_fijo = 10.41
lon_punto_fijo = -72.75

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

# Leer el archivo
ciu = pd.read_csv("./assets/ciu.txt", sep='\s+')

# Obtener las columnas de latitud y longitud
latitudes = ciu['Lat']
longitudes = ciu['Lon']

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

# Mostrar las dos distancias más bajas, sus coordenadas correspondientes y direcciones
for indice in indices_distancias_bajas:
    distancia = distancias[indice]
    lat = latitudes[indice]
    lon = longitudes[indice]
    direccion = direcciones[indice]
    if direccion == "N":
        direccion1 = "norte"
    print("Distancia:", round(distancia), "km hacia el", direccion)
    azimut = calcular_azimut(lat_punto_fijo, lon_punto_fijo, lat, lon)  # Calcular el azimut específico para este punto
    print("Azimut:", round(azimut), "grados")
