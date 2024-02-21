import subprocess
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, letter

# Datos del sismo
sismo_lon = -67.5988
sismo_lat = 9.9623

# Llamar al script ReporteAutomatico.py y pasar los datos del sismo como argumentos
#subprocess.run(['python', 'mapadeestaciones.py', '--lon', str(sismo_lon), '--lat', str(sismo_lat)])

w, h = letter

c = canvas.Canvas("muestra.pdf", pagesize=A4)

c.drawImage("Cintillo_2024_Mesa_de_trabajo1.png", 100 , h, width=400, height=25)

c.setFont("Helvetica", 11)

c.drawString(200, h-30, "SERVICIO SISMÓLOGICO VENEZOLANO")

c.line(80, h-50, 530, h-50)

c.setFont("Helvetica-Bold", 18)

c.drawString(165, h-85, "Reporte Sismológico Automático")

c.line(80, h-105, 530, h-105)

c.drawImage("ejemplo.png", 110 , h-485, width=360, height=360)

c.line(80, h-680, 530, h-680)

c.drawImage("ministerio-01.png", 200, h-760, width=70, height=70 )

c.drawImage("cintillo_redes_Mesa_de_trabajo1.png", 130, h-780, width=350, height=10)

c.save()