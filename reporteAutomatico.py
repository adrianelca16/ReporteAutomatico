import subprocess
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, letter

# Datos del sismo
sismo_lon = -67.5988
sismo_lat = 9.9623

# Llamar al script ReporteAutomatico.py y pasar los datos del sismo como argumentos
subprocess.run(['python', 'mapadeestaciones.py', '--lon', str(sismo_lon), '--lat', str(sismo_lat)])

w, h = letter

c = canvas.Canvas("muestra.pdf", pagesize=A4)

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

fechaUTC = "15/02/2024"
fechaHLV = "14/02/2024"
horaUTC = "00:14:8,4"
horaHLV = "20:14:8,4"
Latitud = "10,41"
Longitud = "72,75"
Profundidad = "5,0"
Magnitud = "2,5"

Localiza1 = "45"
Localiza2 = "49"

c.setFont("Helvetica-Bold", 11)

# Dibujar la variable en negrita junto con el texto normal
c.drawString(230, h-560, fechaUTC)
c.drawString(238, h-573, horaUTC)
c.drawString(230, h-586, fechaHLV)
c.drawString(238, h-599, horaHLV)
c.drawString(380, h-560, Latitud)
c.drawString(390, h-573, Longitud)
c.drawString(410, h-586, Profundidad)
c.drawString(400, h-599, Magnitud)
c.drawString(205, h-658, Localiza1)
c.drawString(200, h-671, Localiza2)


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
c.drawString(220, h-658, "km al noroeste de machiques (Azm. 330º)")
c.drawString(220, h-671, "km al oeste de Villa del Rosario (Azm. 284º)")


c.line(300, h-550, 300, h-600)

c.line(80, h-680, 530, h-680)

c.drawImage("./imagenes/ministerio-01.png", 200, h-760, width=70, height=70 )

c.drawImage("./imagenes/Logo-Funvisis.png", 300, h-760, width=70 , height= 70)

c.drawImage("./imagenes/cintillo_redes_Mesa_de_trabajo1.png", 130, h-780, width=350, height=10)

c.save()