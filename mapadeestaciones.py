import argparse
import pygmt
import pandas as pd
import numpy as np

def main():
    parser = argparse.ArgumentParser(description='Genera un reporte automático con datos de sismo.')
    parser.add_argument('--lon', type=float, help='Longitud del sismo')
    parser.add_argument('--lat', type=float, help='Latitud del sismo')
    args = parser.parse_args()

    estaciones = pd.read_csv("./assets/ESTACIONES.txt", sep='\s+')  # Estaciones nacionales
    nofun = pd.read_csv("./assets/ESTACIONES_NOFUNV.txt", sep='\s+')  # Estaciones internacionales
    ciuc = pd.read_csv("./assets/ciuc.txt", sep=' ', skipinitialspace=True) #ciudades
    ciu = pd.read_csv("./assets/ciu.txt", sep=' ', skipinitialspace=True) #ciudades

    #Datos del sismo pero esto es variable
    sismo_lon = args.lon
    sismo_lat = args.lat

    # Definir la región del mapa
    x_range = 2  # Rango en el eje x
    y_range = 2  # Rango en el eje y
    region = [sismo_lon - x_range, sismo_lon + x_range, sismo_lat - y_range, sismo_lat + y_range]

    fig = pygmt.Figure()

    # Agregar la base del mapa
    fig.grdimage(grid='./assets/etopo1_bedrock.grd', cmap='./assets/verde.cpt', region=region, projection='M8c', frame=True)

    # Agregar límites costeros, fronteras y fallas
    fig.coast(shorelines=True, resolution='f', borders=['1/0.8p', '2/0.1p'])
    fig.plot(data='./assets/fallas2015.txt', pen='0.2,red')

    # Estaciones nacionales
    fig.plot(x=estaciones.Lon, y=estaciones.Lat, style="t0.2c", color='yellow', pen="black")

    # Estaciones internacionales
    fig.plot(x=nofun.Lon, y=nofun.Lat, style="t0.2c", color='green', pen="black")

    #ciudades Grandes
    for index, row in ciuc.iterrows():
        fig.plot(x=row['Lon'], y=row['Lat'], style="c0.12c", color="black", pen="black")
        fig.text(x=row['Lon'] - 0.15, y=row['Lat'] - 0.1, text=row['Nombre'], font='4p,Helvetica-Bold,black', justify='LM')

    #Ciudades pequeñas
    for index, row in ciu.iterrows():
        fig.plot(x=row['Lon'], y=row['Lat'], style="c0.05c", color="black", pen="black")
        fig.text(x=row['Lon'] - 0.15, y=row['Lat'] - 0.1, text=row['Nombre'], font='3p,Helvetica-Bold,black', justify='LM')

    # Sismo
    fig.plot(x=sismo_lon, y=sismo_lat, style="a0.8c", color='white', pen="black")

    #Norte
    norte_lon = sismo_lon - x_range + 0.2
    norte_lat = sismo_lat + y_range - 0.8
    fig.plot(x=norte_lon, y=norte_lat, style="c0.3c", pen="1.2p,black")
    fig.plot(x=[norte_lon, norte_lon], y=[norte_lat - 0.3, norte_lat + 0.3], pen="1p,black")
    fig.plot(x=[norte_lon-0.18, norte_lon+0.18], y=[norte_lat, norte_lat], pen="1p,black")
    fig.text(x=norte_lon, y=norte_lat + 0.4,text='N', font='14p,Helvetica-Bold,black', justify='CM')

    # Guardar la figura principal
    fig.savefig('./imagenes/ejemplo.png')

    # Definir las dimensiones del rectángulo para el mapa pequeño
    width = 2
    height = 2

    lon_start = sismo_lon - width / 2
    lon_end = sismo_lon + width / 2
    lat_start = sismo_lat - height / 2
    lat_end = sismo_lat + height / 2
    # Crear una figura para el mapa pequeño

    rectangle_x = [lon_start, lon_end, lon_end, lon_start, lon_start]
    rectangle_y = [lat_start, lat_start, lat_end, lat_end, lat_start]


    inset = pygmt.Figure()
    inset.grdimage(grid='./assets/etopo1_bedrock.grd', cmap='./assets/verde.cpt', region=[-74, -59, 1, 13], frame=False)
    inset.coast(region=[-74, -59, 1, 13], shorelines=True, resolution="f", area_thresh=10000, borders="1/0.8p")

    # Trazar el rectángulo en el mapa pequeño
    inset.plot(x=rectangle_x, y=rectangle_y, pen="4p,red")
    # Guardar el mapa pequeño como una imagen separada
    inset.savefig('./imagenes/mapa_pequeno.png')



if __name__ == "__main__":
    main()
