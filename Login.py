from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(694, 600)
        MainWindow.setFixedSize(694, 600)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        MainWindow.setAnimated(True)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: rgb(255, 253, 252);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_Emcabezado = QtWidgets.QFrame(self.frame)
        self.frame_Emcabezado.setMinimumSize(QtCore.QSize(0, 150))
        self.frame_Emcabezado.setMaximumSize(QtCore.QSize(16777215, 150))
        self.frame_Emcabezado.setStyleSheet("image: url(:/cintillos/cintillo.png);")
        self.frame_Emcabezado.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Emcabezado.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Emcabezado.setObjectName("frame_Emcabezado")
        self.verticalLayout.addWidget(self.frame_Emcabezado)
        self.frame_Login = QtWidgets.QFrame(self.frame)
        self.frame_Login.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Login.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Login.setObjectName("frame_Login")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_Login)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_titulo = QtWidgets.QLabel(self.frame_Login)
        self.label_titulo.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_titulo.setFont(font)
        self.label_titulo.setStyleSheet("color: rgb(207, 69, 0);\n"
"font: 75 20pt \"MS Shell Dlg 2\";")
        self.label_titulo.setAlignment(QtCore.Qt.AlignCenter)
        self.label_titulo.setObjectName("label_titulo")
        self.verticalLayout_2.addWidget(self.label_titulo)
        self.label_Subtitulo = QtWidgets.QLabel(self.frame_Login)
        self.label_Subtitulo.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_Subtitulo.setStyleSheet("color: rgb(207, 69, 0);\n"
"font: 75 20pt \"MS Shell Dlg 2\";")
        self.label_Subtitulo.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Subtitulo.setObjectName("label_Subtitulo")
        self.verticalLayout_2.addWidget(self.label_Subtitulo)
        self.frame_Datos_usuario = QtWidgets.QFrame(self.frame_Login)
        self.frame_Datos_usuario.setMaximumSize(QtCore.QSize(16777215, 400))
        self.frame_Datos_usuario.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.frame_Datos_usuario.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_Datos_usuario.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Datos_usuario.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Datos_usuario.setObjectName("frame_Datos_usuario")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_Datos_usuario)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 91, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(217, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 1, 0, 1, 1)
        self.lineEdit_usuario = QtWidgets.QLineEdit(self.frame_Datos_usuario)
        self.lineEdit_usuario.setMinimumSize(QtCore.QSize(150, 30))
        self.lineEdit_usuario.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_usuario.setFont(font)
        self.lineEdit_usuario.setStyleSheet("QLineEdit {\n"
"    color: rgb(68, 68, 68);\n"
"    background-color: rgb(255, 208, 190);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: #000000;\n"
"    border-radius: 10px;\n"
"}")
        self.lineEdit_usuario.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_usuario.setObjectName("lineEdit_usuario")
        self.gridLayout_2.addWidget(self.lineEdit_usuario, 1, 1, 1, 3)
        spacerItem2 = QtWidgets.QSpacerItem(216, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 1, 4, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(217, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 2, 0, 1, 1)
        self.lineEdit_contrasena = QtWidgets.QLineEdit(self.frame_Datos_usuario)
        self.lineEdit_contrasena.setMinimumSize(QtCore.QSize(150, 30))
        self.lineEdit_contrasena.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_contrasena.setFont(font)
        self.lineEdit_contrasena.setStyleSheet("QLineEdit {\n"
"    color: rgb(68, 68, 68);\n"
"    background-color: rgb(255, 208, 190);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: #000000;\n"
"    border-radius: 10px;\n"
"}")
        self.lineEdit_contrasena.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_contrasena.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_contrasena.setObjectName("lineEdit_contrasena")
        self.gridLayout_2.addWidget(self.lineEdit_contrasena, 2, 1, 1, 3)
        spacerItem4 = QtWidgets.QSpacerItem(216, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 2, 4, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(245, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem5, 3, 0, 1, 2)
        self.pushButton_Ingresar = QtWidgets.QPushButton(self.frame_Datos_usuario)
        self.pushButton_Ingresar.setEnabled(True)
        self.pushButton_Ingresar.setMinimumSize(QtCore.QSize(120, 35))
        self.pushButton_Ingresar.setMaximumSize(QtCore.QSize(150, 35))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.pushButton_Ingresar.setFont(font)
        self.pushButton_Ingresar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_Ingresar.setStyleSheet("QPushButton {\n"
"    background-color: rgb(204, 0, 0);\n"
"    color: #ffffff;\n"
"    border-radius: 15px;\n"
"    border: none;\n"
"    font: 75 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(171, 0, 0);\n"
"transition: ease 13s;\n"
"cursor: pointer;\n"
"}")
        self.pushButton_Ingresar.setObjectName("pushButton_Ingresar")
        self.gridLayout_2.addWidget(self.pushButton_Ingresar, 3, 2, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(244, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem6, 3, 3, 1, 2)
        spacerItem7 = QtWidgets.QSpacerItem(20, 90, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem7, 4, 2, 1, 1)
        self.verticalLayout_2.addWidget(self.frame_Datos_usuario)
        self.verticalLayout.addWidget(self.frame_Login)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Reporte Automatico"))
        self.label_titulo.setText(_translate("MainWindow", "SISTEMA DE PUBLICACION"))
        self.label_Subtitulo.setText(_translate("MainWindow", "CALCULO AUTOMATICO DE SISMOS"))
        self.lineEdit_usuario.setPlaceholderText(_translate("MainWindow", "Usuario"))
        self.lineEdit_contrasena.setPlaceholderText(_translate("MainWindow", "Contraseña"))
        self.pushButton_Ingresar.setText(_translate("MainWindow", "Ingresar"))
import imagenes_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
