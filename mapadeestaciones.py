import argparse
import pygmt
import pandas as pd

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
    fig.plot(x=ciuc.Lon, y=ciuc.Lat, style="c0.12c", color="black", pen="black")
    fig.text(textfiles=None, x=ciuc.Lon - 0.15, y=ciuc.Lat - 0.1,
            position=None, text=ciuc.Nombre, angle=0,
            font='4p,Helvetica-Bold,black', justify='LM')

    #Ciudades pequeñas
    fig.plot(x=ciu.Lon, y=ciu.Lat, style="c0.05c", color="black", pen="black")
    fig.text(textfiles=None, x=ciu.Lon - 0.15, y=ciu.Lat - 0.1,
            position=None, text=ciu.Nombre, angle=0,
            font='3p,Helvetica-Bold,black', justify='LM')

    # Sismo
    fig.plot(x=sismo_lon, y=sismo_lat, style="a0.8c", color='white', pen="black")

    #Norte
    norte_lon = sismo_lon - x_range + 0.2
    norte_lat = sismo_lat + y_range - 0.8
    fig.plot(x=norte_lon, y=norte_lat, style="c0.3c", pen="1.2p,black")

    fig.plot(x=[norte_lon, norte_lon], y=[norte_lat - 0.3, norte_lat + 0.3], pen="1p,black")
    fig.plot(x=[norte_lon-0.18, norte_lon+0.18], y=[norte_lat, norte_lat], pen="1p,black")

    fig.text(x=norte_lon, y=norte_lat + 0.4,text='N', font='14p,Helvetica-Bold,black', justify='CM')

    fig.legend(position="jBR", box='+glavender+p0.5p+r',spec='./assets/estaciones_legend.txt')

    # Trazar el rectángulo

    # Tamaño del rectángulo (ancho y alto)
    width = 2.5
    height = 2.5

    # Calcular las coordenadas de las esquinas del rectángulo
    lon_start = sismo_lon - width / 2
    lon_end = sismo_lon + width / 2
    lat_start = sismo_lat - height / 2
    lat_end = sismo_lat + height / 2

    # Definir las coordenadas del rectángulo como una lista de listas
    rectangle = [[lon_start, lat_start, lon_end, lat_end]]

    #mapa pequeño
    with fig.inset(
        position="jBL",
        region=[-74, -59, 1, 13],  # Región ajustada a Venezuela
        projection="M3c",  # Proyección Mercator
    ):
        fig.grdimage(grid='./assets/etopo1_bedrock.grd', cmap='./assets/verde.cpt', frame=True)
        fig.coast(
            region=[-74, -59, 1, 13],  # Región ajustada a Venezuela
            shorelines=True,
            resolution="f",
            area_thresh=10000,
            borders="1/0.8p",
        )
        fig.plot(data=rectangle, style="r+s", pen="1p,red")

    fig.savefig('./imagenes/ejemplo.png')
if __name__ == "__main__":
     main()