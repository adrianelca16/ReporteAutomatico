import subprocess

# Datos del sismo
sismo_lon = -67.5988
sismo_lat = 9.9623

# Llamar al script ReporteAutomatico.py y pasar los datos del sismo como argumentos
subprocess.run(['python', 'mapadeestaciones.py', '--lon', str(sismo_lon), '--lat', str(sismo_lat)])
