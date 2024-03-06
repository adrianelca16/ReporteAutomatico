from Login import *
from PyQt5 import QtWidgets
import sys
from conexion_postgresql import conectar_db, buscarUsuario
from os import startfile
import subprocess

class MiApp(QtWidgets.QMainWindow): 
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_Ingresar.clicked.connect(self.ingresar)

        self.connection = conectar_db()
    def ingresar(self):
        usuario = self.ui.lineEdit_usuario.text()
        password = self.ui.lineEdit_contrasena.text()

        if self.connection : 
            login = buscarUsuario(self.connection,usuario,password)

            if login == "login" :

                script_path = "ReporteBac.py"
        
        # Usa subprocess.Popen para ejecutar otro script de Python
                subprocess.Popen(["python", script_path])
                #self.abrir = self.abrir_menu()
                #self.hide()
                self.close()

    def abrir_menu(self):
        self.abrir = startfile("ReporteBac.py")

if __name__ == "__main__":
     app = QtWidgets.QApplication(sys.argv)
     mi_app = MiApp()
     mi_app.show()
     sys.exit(app.exec_())		
