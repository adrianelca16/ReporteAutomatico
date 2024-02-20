import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mi Aplicación PyQt")
        self.setGeometry(100, 100, 800, 700)  # Establecer la posición y el tamaño de la ventana

        # Crear un widget de etiqueta (texto)
        self.label = QLabel("¡Hola, mundo!", self)
        self.label.setGeometry(50, 50, 300, 50)  # Establecer la posición y el tamaño de la etiqueta

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
