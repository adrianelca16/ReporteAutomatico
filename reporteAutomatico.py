import subprocess
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, letter
import argparse
from pdf2image import convert_from_path
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

    c.drawString(165, h-85, "Reporte Sismológico Automático")

    c.line(80, h-105, 530, h-105)

    c.drawImage("./imagenes/ejemplo.png", 90 , h-485, width=400, height=360)

    c.setFont("Helvetica", 6)

    c.drawString(170, h-520, "Proyección Mercator | Datum WGS84 | Escala 1:3.500.000 | Fuentes: IGVSB, Funvisis")
    #campos que me faltan por arg
    

    c.setFont("Helvetica-Bold", 11)

    c.drawString(230, h-560, fechaUTC)
    c.drawString(238, h-573, horaUTC)
    c.drawString(230, h-586, fechaHLV)
    c.drawString(238, h-599, horaHLV)
    c.drawString(380, h-560, Latitud)
    c.drawString(390, h-573, Longitud)
    c.drawString(410, h-586, Profundidad)
    c.drawString(400, h-599, Magnitud)
    c.drawString(165, h-658, Localiza1)
    c.drawString(175, h-671, Localiza2)

    c.setFont("Helvetica", 11)

    c.drawString(161, h-560, "Fecha (UTC): ")
    c.drawString(104, h-573, "Tiempo de Origen (UTC): ")
    c.drawString(162, h-586, "Fecha (HLV): ")
    c.drawString(105, h-599, "Tiempo de Origen (HLV): ")
    c.drawString(320, h-560, "Latitud (ºN): ")
    c.drawString(320, h-573, "Longitud (ºO): ")
    c.drawString(320, h-586, "Profundidad (km): ")
    c.drawString(320, h-599, "Magnitud (Mw): ")
    c.drawString(250, h-640, "El sismo se localiza a: ")

    c.line(300, h-550, 300, h-600)
    c.line(80, h-680, 530, h-680)

    c.drawImage("./imagenes/ministerio-01.png", 200, h-760, width=70, height=70 )
    c.drawImage("./imagenes/Logo-Funvisis.png", 300, h-760, width=70 , height= 70)
    c.drawImage("./imagenes/cintillo_redes_Mesa_de_trabajo1.png", 130, h-780, width=350, height=10)

    c.save()

    pdf_path = "./muestra.pdf"

    images = convert_from_path(pdf_path)

    for i, image in enumerate(images):
        image_path = f"muestra.png"
        image.save(image_path, "PNG")
    

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
