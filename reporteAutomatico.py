import subprocess
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, letter

# Datos del sismo
sismo_lon = -67.5988
sismo_lat = 9.9623

# Llamar al script ReporteAutomatico.py y pasar los datos del sismo como argumentos
#subprocess.run(['python', 'mapadeestaciones.py', '--lon', str(sismo_lon), '--lat', str(sismo_lat)])

w, h = letter

c = canvas.Canvas("muestra.pdf", pagesize=letter)
c.drawString(50, h-50, "esto es un texto en pdf")

#c.line(50, h-70, 400, h-70)

c.drawImage("ejemplo.png", 100 , h-400, width=200, height=200)

#c.drawImage("Cintillo2024EPS.png", 0 , h-200)

c.save()