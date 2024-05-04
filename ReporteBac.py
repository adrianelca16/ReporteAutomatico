from Reporte import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget,QFileDialog, QTableWidgetItem
from PyQt5.QtGui import QPixmap
import sys
import subprocess
import shutil

class MiApp(QtWidgets.QMainWindow,):
    def __init__(self):
        super().__init__()
        # Crear la ventana principal
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #ventana de imprimir
        self.ui.pushButton_ultimoSismo.clicked.connect(self.irImprimir)
        self.ui.pushButton_regresarImprimir.clicked.connect(self.volver)
        self.ui.pushButton_imprimirReporte.clicked.connect(self.descargar_pdf)

        #ventana de busqueda
        self.ui.pushButton_busquedaManual.clicked.connect(lambda: self.ui.stackedWidget_izq.setCurrentIndex(2))
        self.ui.pushButton_RegresarID.clicked.connect(self.volver)
        self.ui.pushButton_continuarID.clicked.connect(self.buscarID)
        #ventana de ultimos 10
        self.ui.pushButton_ultimos10.clicked.connect(self.ultimosSismos)
        self.ui.pushButton_regresar10.clicked.connect(self.volver)

        #ventana de fecha
        self.ui.pushButton_busquedaFecha.clicked.connect(lambda: self.ui.stackedWidget_izq.setCurrentIndex(4))
        self.ui.pushButton_regresarFecha.clicked.connect(self.volver)

    


    def irImprimir(self):
        python_path = sys.executable
        comandoLista = "scevtls -d postgresql:// --begin 01-01-2024 00:00:00 > lista_de_eventos.txt"
        #subprocess.call(comandoLista, shell=True)
        #with open("lista_de_eventos.txt","r") as archivo:
            #ultimo_sismo = archivo.readlines()[-1]
        #comandoXml = "scxmldump -d postgresql:// -E " + ultimo_sismo + " -PAMF -o ultimo_evento.xml"
        #subprocess.call(comandoXml,shell=True)
        comandoBoletin = "scbulletin -i /home/ndcuser/adrian/ReporteAutomatico/ultimo_evento.xml > /home/ndcuser/adrian/ReporteAutomatico/bulletin_ultimo_evento.txt"
        #subprocess.call(comandoBoletin,shell=True)
        subprocess.call([python_path, 'leer.py'])
        self.ui.stackedWidget_izq.setCurrentIndex(1)
        image_widget = create_image_widget("./muestra.png",400,500)
        self.ui.stackedWidget_der.insertWidget(1, image_widget)
        self.ui.stackedWidget_der.setCurrentIndex(1)

    def ultimosSismos(self):
        with open("lista_de_eventosAdrianPrueba.txt", "r") as archivo:
            lineas = archivo.readlines()[-10:][::-1] 
            for indice,linea in enumerate(lineas):
                # comandoXml = "scxmldump -d postgresql:// -E " + linea.strip() + " -PAMF -o ultimos_10_sismos.xml"
                # subprocess.call(comandoXml,shell=True)
                # comandoBoletin = "scbulletin -i /home/ndcuser/adrian/ReporteAutomatico/ultimos_10_sismos.xml > /home/ndcuser/adrian/ReporteAutomatico/bulletin_ultimo_evento.txt"
                # subprocess.call(comandoBoletin,shell=True)
                with open ('bulletin_ultimo_evento.txt', 'r') as archivo:
                    lineasArchivo = archivo.readlines()
                    lineaArchivo = lineasArchivo[5].strip().split()
                    fecha = lineaArchivo[5]
                    hora = lineaArchivo[6]
                    idSismo = linea.strip()
                    if indice >= self.ui.tableWidget_ultimos10.rowCount():
                        return
                    
                    item_id = QTableWidgetItem(idSismo)
                    item_fecha = QTableWidgetItem(fecha)
                    item_hora = QTableWidgetItem(hora)
                    
                    self.ui.tableWidget_ultimos10.setItem(indice, 2, item_id)
                    self.ui.tableWidget_ultimos10.setItem(indice, 0, item_fecha)
                    self.ui.tableWidget_ultimos10.setItem(indice, 1, item_hora)
        self.ui.stackedWidget_izq.setCurrentIndex(3)

    def buscarID(self):
        python_path = sys.executable
        comandoLista = "scevtls -d postgresql:// --begin 01-01-2024 00:00:00 > lista_de_eventos.txt"
        #subprocess.call(comandoLista, shell=True)
        texto_busqueda = self.ui.lineEdit_ID.text()
        
        if not texto_busqueda:
            return
        
        encontrado = False  # Variable para indicar si se encontró el texto
        
        with open("lista_de_eventos.txt", "r") as archivo:
            lineas = archivo.readlines()
            
            for linea in lineas:
                if texto_busqueda in linea:
                    encontrado = True
                    break  # Salir del bucle si se encuentra una coincidencia
        
        if encontrado:
            print("El texto está presente en el archivo.")
            # Aquí puedes agregar el código para realizar alguna acción si se encuentra el texto
        else:
            print("El texto no está presente en el archivo.")
            # Aquí puedes agregar el código para realizar alguna acción si no se encuentra el texto
    def volver(self):
        self.ui.stackedWidget_izq.setCurrentIndex(0)
        self.ui.stackedWidget_der.setCurrentIndex(0)

    def descargar_pdf(self):
        ruta_pdf_origen = "./muestra.pdf"

        # Abrir el cuadro de diálogo para seleccionar la carpeta de destino
        ruta_destino = QFileDialog.getExistingDirectory(self, "Seleccionar Carpeta")

        if ruta_destino:
            ruta_destino = ruta_destino + "/muestra.pdf"

            # Copiar el archivo PDF a la nueva ubicación
            shutil.copyfile(ruta_pdf_origen, ruta_destino)

   
def create_image_widget(image_path,width, height):
    image_widget = QWidget()
    layout = QVBoxLayout()
    label = QLabel()
    pixmap = QPixmap(image_path)  # Reemplaza "image_path" con la ruta de tu imagen
    pixmap = pixmap.scaled(width, height)  # Escalar la imagen al tamaño deseado
    label.setPixmap(pixmap)
    label.setFixedSize(width, height)  # Establecer las dimensiones del label
    layout.addWidget(label)
    image_widget.setLayout(layout)
    return image_widget

if __name__ == "__main__":
     app = QtWidgets.QApplication(sys.argv)
     mi_app = MiApp()
     mi_app.show()
     sys.exit(app.exec_())		
