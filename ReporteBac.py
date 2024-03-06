from Reporte import *
from PyQt5 import QtWidgets
import sys

class MiApp(QtWidgets.QMainWindow,):
    def __init__(self):
        super().__init__()
        # Crear la ventana principal
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #ventana de imprimir
        self.ui.pushButton_ultimoSismo.clicked.connect(self.irImprimir)
        self.ui.pushButton_regresarImprimir.clicked.connect(self.volver)

        #ventana de busqueda
        self.ui.pushButton_busquedaManual.clicked.connect(lambda: self.ui.stackedWidget_izq.setCurrentIndex(2))
        self.ui.pushButton_RegresarID.clicked.connect(self.volver)
        
        #ventana de ultimos 10
        self.ui.pushButton_ultimos10.clicked.connect(lambda: self.ui.stackedWidget_izq.setCurrentIndex(3))
        self.ui.pushButton_regresar10.clicked.connect(self.volver)

        #ventana de fecha
        self.ui.pushButton_busquedaFecha.clicked.connect(lambda: self.ui.stackedWidget_izq.setCurrentIndex(4))
        self.ui.pushButton_regresarFecha.clicked.connect(self.volver)



    def irImprimir(self):
        self.ui.stackedWidget_izq.setCurrentIndex(1)
        self.ui.stackedWidget_der.setCurrentIndex(1)

        
    def volver(self):
        self.ui.stackedWidget_izq.setCurrentIndex(0)
        self.ui.stackedWidget_der.setCurrentIndex(0)


if __name__ == "__main__":
     app = QtWidgets.QApplication(sys.argv)
     mi_app = MiApp()
     mi_app.show()
     sys.exit(app.exec_())		
