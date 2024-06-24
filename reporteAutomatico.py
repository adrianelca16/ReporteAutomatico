import subprocess
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, letter
import argparse
from pdf2image import convert_from_path
from PIL import Image
from reportlab.lib.colors import white, black, yellow, orange, red
from reportlab.graphics.shapes import Drawing, Polygon

def generar_reporte(args):
    w, h = letter

    fechaUTC = args.fec
    fechaHLV = args.fec
    horaUTC = args.hor
    horaHLV = args.hor

    #campos con args
    Latitud = args.lat
    Longitud = args.lon
    Profundidad = args.pro
    Magnitud = args.mag

    Localiza1 = args.azm1
    Localiza2 = args.azm2

    lon= float(Longitud)
    lonDeci = "{:.2f}".format(-lon)

    lat=float(Latitud)
    latDeci="{:.2f}".format(lat)

    subprocess.run(['python','mapadeestaciones.py','--lat', latDeci, '--lon', lonDeci])

    c = canvas.Canvas(args.output_file, pagesize=A4)

    c.drawImage("./imagenes/Cintillo_2024_Mesa_de_trabajo1.png", 100 , h, width=400, height=25)

    c.setFont("Helvetica", 11)

    c.drawString(200, h-30, "SERVICIO SISMÓLOGICO VENEZOLANO")

    c.line(80, h-50, 530, h-50)

    c.setFont("Helvetica-Bold", 18)

    c.drawString(205, h-85, "Reporte Automático")

    c.line(80, h-105, 530, h-105)

    c.drawImage("./imagenes/ejemplo.png", 90 , h-485, width=400, height=360)

    c.drawImage("./imagenes/mapa_pequeno.png", 131, h-465, width=80 , height=70 )

    c.setLineWidth(2)
    c.line(131, h-395, 212, h-395)

    c.line(212,h-394, 212, h-465)

    c.setFillColor(white)  # Establece el color de relleno en blanco
    c.rect(402, 327, 80, 65, fill=1)  

    c.setFillColor(black)


    c.setFont("Helvetica", 8)
    c.drawString(425, 380, "Leyenda:") 
    c.setFont("Helvetica", 7) # Agrega el título de la leyenda
    c.drawString(420, 370, "Epicentro")  # Agrega la primera descripción
    c.drawString(420, 360, "Ciudades")
    c.drawString(420, 350, "Estaciones")
    c.drawString(420, 340, "Sismicidad")
    c.drawString(420, 330, "Fallas G.")

    #triangulo amarillo
    # c.setLineWidth(1)
    # c.line(407, 350 ,410, 355)
    # c.line(407, 350 ,414, 350)
    # c.line(410, 355 ,414, 350)

    triangle_coords = [407, 350, 410, 355, 414, 350]
    triangle = Polygon(triangle_coords)
    triangle.fillColor = yellow
    triangle.strokeColor = black
    drawing = Drawing()
    drawing.add(triangle)

    drawing.wrap(0,0)  # El 0, 0 indica el ancho y alto del objeto
    drawing.drawOn(c, 0, 0)

    #Estrella
    c.setLineWidth(1)
    c.line(410,376,409,373)
    c.line(410,376,412,373)
    c.line(412,373,414,373)
    c.line(414,373,412.5,371)
    c.line(412.5,371,414,369)
    c.line(409,373,407,373)
    c.line(407,373,408.5,371)
    c.line(408.5,371,407.5,369)
    c.line(407.5,369,410.5,370.5)
    c.line(410.5,370.5,413.5,369)



    #circulo negro
    c.setLineWidth(2)
    c.circle(410, 362, 1)

    c.setStrokeColor(orange) # Naranja
    c.circle(410, 342, 2)

    c.setStrokeColor(red)  # Rojo
    c.line(407, 333, 414, 333)

    c.setStrokeColor(black)

    c.setLineWidth(5)
    c.line(127,665, 127, 322)
    c.line(485,665, 485, 322)
    c.line(127,663,485,663)
    c.line(127,325,485,325)
    c.setFont("Helvetica", 6)

    c.setLineWidth(2)
    c.drawString(170, h-505, "Proyección Mercator | Datum WGS84 | Escala 1:3.500.000 | Fuentes: IGVSB, Funvisis")
    #campos que me faltan por arg
    

    c.setFont("Helvetica-Bold", 11)

    c.drawString(230, h-530, fechaUTC)
    c.drawString(238, h-543, horaUTC.replace('.', ','))
    c.drawString(230, h-556, fechaHLV)
    c.drawString(238, h-569, horaHLV.replace('.', ','))
    c.drawString(380, h-530, Latitud.replace('.', ','))
    c.drawString(390, h-543, Longitud.replace('.', ','))
    c.drawString(410, h-556, Profundidad.replace('.', ','))
    c.drawString(400, h-569, Magnitud.replace('.', ','))
    

    c.setFont("Helvetica", 11)

    c.drawString(161, h-530, "Fecha (UTC): ")
    c.drawString(104, h-543, "Tiempo de Origen (UTC): ")
    c.drawString(162, h-556, "Fecha (HLV): ")
    c.drawString(105, h-569, "Tiempo de Origen (HLV): ")
    c.drawString(320, h-530, "Latitud (ºN): ")
    c.drawString(320, h-543, "Longitud (ºO): ")
    c.drawString(320, h-556, "Profundidad (km): ")
    c.drawString(320, h-569, "Magnitud (Mw): ")
    c.drawString(250, h-587, "El sismo se localiza a: ")

    c.drawString(165, h-601, Localiza1)
    c.drawString(175, h-614, Localiza2)

    c.setFont("Helvetica",10)
    c.drawString(87, h-643, "Atención: Los datos reflejados en este reporte preliminar son generados por una aplicación de")
    c.drawString(87, h-656, "cálculo automático y sus valores pueden ser inexactos hasta ser revisados por un analista de")
    c.drawString(87, h-669, "forma de onda.")

    c.line(300, h-520, 300, h-570)
    c.line(80, h-680, 530, h-680)

    c.drawImage("./imagenes/ministerio-01.png", 200, h-760, width=70, height=70 )
    c.drawImage("./imagenes/Logo-Funvisis.png", 300, h-760, width=70 , height= 70)
    c.drawImage("./imagenes/cintillo_redes_Mesa_de_trabajo1.png", 130, h-780, width=350, height=10)

    c.save()

    pdf_path = "./muestra.pdf"

    images = convert_from_path(pdf_path)

    for i, image in enumerate(images):
    # Redimensionar la imagen
    # Guardar la imagen redimensionada
        image_path = f"muestra.png"
        image.save(image_path, "PNG")

        saved_image = Image.open(image_path)
    # Redimensionar la imagen
        resized_image = saved_image.resize((400, 500))
    # Guardar la imagen redimensionada
        resized_image.save(image_path)
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Genera un reporte sismológico automático en formato PDF.')
    parser.add_argument('--lat', type=str, help='Latitud del epicentro del sismo')
    parser.add_argument('--lon', type=str, help='Longitud del epicentro del sismo')
    parser.add_argument('--pro', type=str, help='Profundidad del sismo')
    parser.add_argument('--mag', type=str, help='Magnitud del sismo')
    parser.add_argument('--azm1', type=str, help='Magnitud del sismo')
    parser.add_argument('--azm2', type=str, help='Magnitud del sismo')
    parser.add_argument('--fec', type=str, help='Magnitud del sismo')
    parser.add_argument('--hor', type=str, help='Magnitud del sismo')
    parser.add_argument('--output_file', type=str, default='muestra.pdf', help='Nombre del archivo de salida PDF')
    args = parser.parse_args()

    #

    generar_reporte(args)
