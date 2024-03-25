with open ('bulletin_ultimo_evento.txt', 'r') as archivo:
    lineas = archivo.readlines()
    linea = lineas[5].strip().split()
    magnitud = linea[4]
    latitud = linea[7]
    longitud = linea[9]
    profundidad = linea[11]
print ('magnitud: ', magnitud)
print ('latitud: ', latitud)
print ('longitud: ', longitud)
print ('profundidad: ', profundidad)