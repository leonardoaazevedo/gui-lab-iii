import control

from connection import Connection
import time
import numpy as np

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8


    def _translate(context, text, disambig):

        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)


class Ui_Guindaste(object):

    def setupUi(self, Guindaste):
        # create connection
        control = Connection()
        # Janela principal da GUI
        Guindaste.setObjectName(_fromUtf8("Guindaste"))
        Guindaste.resize(820, 800)

        # Titulo central "Controle do Guindaste"
        self.label_5 = QtWidgets.QLabel(Guindaste)
        self.label_5.setGeometry(QtCore.QRect(245, 20, 400, 41))
        self.label_5.setStyleSheet(_fromUtf8("font: 18pt \"Helvetica\";"))
        self.label_5.setObjectName(_fromUtf8("label_5"))

        # Imagem guindaste
        self.pixmap = QtGui.QPixmap('crane.png')
        self.label_13 = QtWidgets.QLabel(Guindaste)
        self.label_13 = QtWidgets.QLabel(Guindaste)
        self.label_13.setPixmap(self.pixmap)
        self.label_13.setGeometry(QtCore.QRect(650, 130, 160, 290))
        self.label_13.setScaledContents(True)

        # Telas centrais
        self.graphicsView = QtWidgets.QGraphicsView(Guindaste)
        self.graphicsView.setGeometry(QtCore.QRect(207, 125, 420, 300))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))

        # camera
        self.view = QtWidgets.QLabel(Guindaste)
        self.view.setGeometry(QtCore.QRect(207, 125, 220, 220))
        self.pixmap = QtGui.QPixmap()
        self.view.setPixmap(self.pixmap)

        # Label da camera
        self.label_14 = QtWidgets.QLabel(Guindaste)
        self.label_14.setGeometry(QtCore.QRect(207, 90, 220, 41))
        self.label_14.setObjectName(_fromUtf8("label_14"))



        # LCDs colors
        self.off_color = QtGui.QPalette()
        self.off_color.setColor(QtGui.QPalette.Light, QtGui.QColor(255, 145, 145))
        self.on_color = QtGui.QPalette()
        self.on_color.setColor(QtGui.QPalette.Light, QtGui.QColor(145, 225, 145))

        # Quadro status"
        self.groupBox_status = QtWidgets.QGroupBox(Guindaste)
        self.groupBox_status.setGeometry((QtCore.QRect(630, 430, 180, 235)))  ##   /cima/direita/baixo
        self.groupBox_status.setObjectName(_fromUtf8("groupBox_status"))

        # Label estado de conexão
        self.label_10 = QtWidgets.QLabel(self.groupBox_status)
        self.label_10.setGeometry(QtCore.QRect(30, 30, 131, 31))
        self.label_10.setObjectName(_fromUtf8("label_10"))

        # Estado do guindaste
        self.lcdNumber_5 = QtWidgets.QLCDNumber(self.groupBox_status)
        self.lcdNumber_5.setGeometry(QtCore.QRect(30, 55, 60, 30))
        self.lcdNumber_5.setObjectName(_fromUtf8("lcdNumber_5"))
        self.lcdNumber_5.setPalette(self.off_color)

        # lABEL ESTADO DO GUINDASTE
        self.label_12 = QtWidgets.QLabel(self.groupBox_status)
        self.label_12.setGeometry(QtCore.QRect(30, 100, 131, 31))
        self.label_12.setObjectName(_fromUtf8("label_12"))

        # estado do imã
        self.lcdNumber_6 = QtWidgets.QLCDNumber(self.groupBox_status)
        self.lcdNumber_6.setGeometry(QtCore.QRect(30, 125, 60, 30))
        self.lcdNumber_6.setObjectName(_fromUtf8("lcdNumber_6"))
        self.lcdNumber_6.setPalette(self.off_color)

        # Label estado do imã
        self.label_8 = QtWidgets.QLabel(self.groupBox_status)
        self.label_8.setGeometry(QtCore.QRect(30, 160, 131, 31))
        self.label_8.setObjectName(_fromUtf8("label_8"))

        # LCDs estado do imã
        self.lcdNumber_4 = QtWidgets.QLCDNumber(self.groupBox_status)
        self.lcdNumber_4.setGeometry(QtCore.QRect(30, 190, 60, 30))
        self.lcdNumber_4.setObjectName(_fromUtf8("lcdNumber_4"))
        self.lcdNumber_4.setPalette(self.off_color)

        # Quadro inferior esquerdo "Controle do Guindaste ON/OFF"
        self.groupBox_4 = QtWidgets.QGroupBox(Guindaste)
        self.groupBox_4.setGeometry(QtCore.QRect(15, 120, 181, 151)) ##   /cima/direita/baixo
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))

        # Botão de conectar
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_7.setGeometry(QtCore.QRect(50, 35, 80, 30))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))

        # Botão de conectar
        # self.pushButton_8 = QtWidgets.QPushButton(self.groupBox_20)
        # self.pushButton_8.setGeometry(QtCore.QRect(50, 35, 80, 30))
        # self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))

        # Ligar e desligar guindaste
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 90, 80, 30))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))

        # Quadro inferior esquerdo "Controle de acoplamento imã"
        self.groupBox_3 = QtWidgets.QGroupBox(Guindaste)
        self.groupBox_3.setGeometry(QtCore.QRect(15, 300, 181, 96))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))

        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_6.setGeometry(QtCore.QRect(50, 40, 80, 30))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))

        # Quadro inferior central "Girar a torre"
        self.groupBox = QtWidgets.QGroupBox(Guindaste)
        self.groupBox.setGeometry(QtCore.QRect(207, 430, 145, 235))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))

        # Botão Girar sentido horário
        self.pushButton_gira_torre_horario = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_gira_torre_horario.setGeometry(QtCore.QRect(30, 30, 80, 40))
        self.pushButton_gira_torre_horario.setObjectName(_fromUtf8("pushButton_gira_torre_horario"))
        self.pushButton_gira_torre_horario.setText(_translate("Guindaste", "Girar torre \n horário", None))

        # Botão Girar sentido anti-horário
        self.pushButton_gira_torre_anti_horario = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_gira_torre_anti_horario.setGeometry(QtCore.QRect(30, 80, 80, 40))
        self.pushButton_gira_torre_anti_horario.setObjectName(_fromUtf8("pushButton_gira_torre_anti_horario"))
        self.pushButton_gira_torre_anti_horario.setText(_translate("Guindaste", "Girar torre \n anti-horário", None))
        self.pushButton_gira_torre_anti_horario.setText(_translate("Guindaste", "Girar torre \n anti-horário", None))

        # Label Angulo da torre
        self.label_angulo_da_torre = QtWidgets.QLabel(self.groupBox)
        self.label_angulo_da_torre.setGeometry(QtCore.QRect(30, 140, 131, 31))
        self.label_angulo_da_torre.setObjectName(_fromUtf8("label_angulo_da_torre"))

        # display Angulo da torre
        self.lcdNumber_angulo_da_torre = QtWidgets.QLCDNumber(self.groupBox)
        self.lcdNumber_angulo_da_torre.setGeometry(QtCore.QRect(30, 180, 60, 31))
        self.lcdNumber_angulo_da_torre.setObjectName(_fromUtf8("lcdNumber_angulo_da_torre"))

        # Quado inferior esquerdo Frente/Ré Caminhão
        self.groupBox_20 = QtWidgets.QGroupBox(Guindaste)
        self.groupBox_20.setGeometry(QtCore.QRect(30, 430, 145, 235))
        self.groupBox_20.setObjectName(_fromUtf8("groupBox20"))

        # Botão mover para frente
        self.pushButton_frente_caminhao= QtWidgets.QPushButton(self.groupBox_20)
        self.pushButton_frente_caminhao.setGeometry(QtCore.QRect(30, 50, 80, 30))
        # self.pushButton_5.setGeometry(QtCore.QRect(190, 85, 80, 45))
        self.pushButton_frente_caminhao.setObjectName(_fromUtf8("pushButton_frente_caminhao"))
        self.pushButton_frente_caminhao.setText(_translate("Guindaste", "Mover para\n frente", None))

        #Botão Mover para trás
        self.pushButton_tras_caminhao = QtWidgets.QPushButton(self.groupBox_20)
        self.pushButton_tras_caminhao.setGeometry(QtCore.QRect(30, 100, 80, 30))
        self.pushButton_tras_caminhao.setObjectName(_fromUtf8("pushButton_tras_caminhao"))
        self.pushButton_tras_caminhao.setText(_translate("Guindaste", "Mover para\n trás", None))

        # Label Distância do caminhão
        self.label_distancia_do_caminhao= QtWidgets.QLabel(self.groupBox_20)
        self.label_distancia_do_caminhao.setGeometry(QtCore.QRect(30, 140, 131, 31))
        self.label_distancia_do_caminhao.setObjectName(_fromUtf8("label_distancia_do_caminhao"))

        # display distância do caminhão
        self.lcdNumber_distancia_caminhao = QtWidgets.QLCDNumber(self.groupBox_20)
        self.lcdNumber_distancia_caminhao.setGeometry(QtCore.QRect(30, 170, 60, 31))
        self.lcdNumber_distancia_caminhao.setObjectName(_fromUtf8("lcdNumber_distancia_caminhao"))

        # Quadro inferior central "Controle Direcional Guindaste com Botões Braço/Lança"
        self.groupBox1 = QtWidgets.QGroupBox(Guindaste)
        self.groupBox1.setGeometry(QtCore.QRect(362, 430, 265, 235))
        self.groupBox1.setObjectName(_fromUtf8("groupBox"))

        # Botão Subir lança
        self.pushButton_subir_lanca = QtWidgets.QPushButton(self.groupBox1)
        self.pushButton_subir_lanca.setGeometry(QtCore.QRect(30, 50, 80, 35))
        self.pushButton_subir_lanca.setObjectName(_fromUtf8("pushButton_subir_lanca"))
        self.pushButton_subir_lanca.setText(_translate("Guindaste", "Subir \n Lança", None))

        # Botão descer lança
        self.pushButton_descer_lanca = QtWidgets.QPushButton(self.groupBox1)
        self.pushButton_descer_lanca.setGeometry(QtCore.QRect(30, 100, 80, 35))
        self.pushButton_descer_lanca.setObjectName(_fromUtf8("pushButton_descer_lanca"))
        self.pushButton_descer_lanca.setText(_translate("Guindaste", "Descer \n Lança", None))

        # Label ALTURA da lança
        self.label_altura_lanca = QtWidgets.QLabel(self.groupBox1)
        self.label_altura_lanca.setGeometry(QtCore.QRect(30, 150, 131, 31))
        self.label_altura_lanca.setObjectName(_fromUtf8("label_altura_lanca"))

        # display altura da lança
        self.lcdNumber_altura_lanca = QtWidgets.QLCDNumber(self.groupBox1)
        self.lcdNumber_altura_lanca.setGeometry(QtCore.QRect(30, 180, 60, 31))
        self.lcdNumber_altura_lanca.setObjectName(_fromUtf8("lcdNumber_altura_lanca"))

        # Botão Expande lança
        self.pushButton_expande_lanca = QtWidgets.QPushButton(self.groupBox1)
        self.pushButton_expande_lanca.setGeometry(QtCore.QRect(150, 50, 80, 35))
        self.pushButton_expande_lanca.setObjectName(_fromUtf8("pushButton_expande_lanca"))
        self.pushButton_expande_lanca.setText(_translate("Guindaste", "Expande \n Lança", None))

        # Botão Comprime lança
        self.pushButton_comprime_lanca = QtWidgets.QPushButton(self.groupBox1)
        self.pushButton_comprime_lanca.setGeometry(QtCore.QRect(150, 100, 80, 35))
        self.pushButton_comprime_lanca.setObjectName(_fromUtf8("pushButton_comprime_lanca"))
        self.pushButton_comprime_lanca.setText(_translate("Guindaste", "Comprime \n Lança", None))

        # Label distância da lança
        self.label_distancia_lanca = QtWidgets.QLabel(self.groupBox1)
        self.label_distancia_lanca.setGeometry(QtCore.QRect(150, 150, 131, 31))
        self.label_distancia_lanca.setObjectName(_fromUtf8("label_distancia_lanca"))

        # display distância da lança

        self.lcdNumber_distancia_lanca = QtWidgets.QLCDNumber(self.groupBox1)
        self.lcdNumber_distancia_lanca.setGeometry(QtCore.QRect(150, 180, 60, 31))
        self.lcdNumber_distancia_lanca.setObjectName(_fromUtf8("lcdNumber_distancia_lanca"))

        # janelas de confirmação
        self.confirmWindow = QtWidgets.QMessageBox()
        self.confirmWindow.setIcon(QtWidgets.QMessageBox.Question)
        self.confirmWindow.setWindowTitle('Controle do Imã')
        self.confirmWindow.setText('Desligar imã?')
        self.confirmWindow.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        self.buttonY = self.confirmWindow.button(QtWidgets.QMessageBox.Yes)
        self.buttonY.setText('Sim')
        self.buttonN = self.confirmWindow.button(QtWidgets.QMessageBox.No)
        self.buttonN.setText('Não')
        self.confirmWindow.setDefaultButton(self.buttonN)

        self.confirmWindow_2 = QtWidgets.QMessageBox()
        self.confirmWindow_2.setIcon(QtWidgets.QMessageBox.Question)
        self.confirmWindow_2.setWindowTitle('Controle do Guindaste')
        self.confirmWindow_2.setText("AVISO: Imã ligado.\nDesligue-o antes de concluir esta ação.")
        self.confirmWindow_2.setStandardButtons(QtWidgets.QMessageBox.Ok)

        # raises
        self.view.raise_()
        self.lcdNumber_4.raise_()
        self.lcdNumber_4.display('OFF')
        self.label_10.raise_()
        self.lcdNumber_5.raise_()
        self.lcdNumber_5.display('OFF')
        self.label_12.raise_()
        self.lcdNumber_6.display('Off')
        self.lcdNumber_6.raise_()
        self.label_8.raise_()

        self.groupBox_4.raise_()
        self.groupBox_3.raise_()
        self.groupBox.raise_()
        self.groupBox1.raise_()
        self.groupBox_20.raise_()
        self.label_distancia_lanca.raise_()
        self.lcdNumber_altura_lanca.raise_()
        self.lcdNumber_altura_lanca.display(0)
        self.label_distancia_do_caminhao.raise_()
        self.lcdNumber_distancia_caminhao.raise_()
        self.lcdNumber_distancia_caminhao.display(0)
        self.lcdNumber_distancia_lanca.raise_()
        self.lcdNumber_distancia_lanca.display(0)
        self.label_angulo_da_torre.raise_()
        self.label_13.raise_()
        self.groupBox_status.raise_()

        Guindaste.setFont(QtGui.QFont("Helvetica"))
        self.retranslateUi(Guindaste)

        # Start conection Connection
        def connect():
            print('Start Connection')
            _, status = control.init_connection(ip='127.0.0.1', port=8080)
            if status:
                self.lcdNumber_4.display('UP')
                self.lcdNumber_4.setPalette(self.on_color)
            else:
                self.lcdNumber_4.display('Off')
                self.lcdNumber_4.setPalette(self.off_color)

            self.pushButton_7.clicked.connect(connect)

        def crane():
            if control.connectionStatus:
                status = control.getCraneStatus()
                if status:
                    if control.getMagnetStatus():
                        self.confirmWindow_2.exec_()
                        print("Não é possível desligar o guindaste com o imã ainda ligado.")
                    else:
                        print('Desligado')
                        control.commandCraneOnOff()
                        self.view.clear()

                        self.lcdNumber_5.display('OFF')
                        self.lcdNumber_5.setPalette(self.off_color)
                        self.lcdNumber_4.display(0)
                else:
                    print('Ligado')
                    control.commandCraneOnOff()
                    self.lcdNumber_5.display('UP')
                    self.lcdNumber_5.setPalette(self.on_color)

                    angle = getAngle360(control.getCurrentAngleClaw())
                    self.lcdNumber_6.display(round(angle))

                    dist = control.getStatusDist()
                    self.lcdNumber.display(dist)
                    im1 = control.getCamImage(save=True, number=1)
                    im2 = control.getCamImage(save=True, number=2)
                    if im1 is not None:
                        self.pixmap = QtGui.QPixmap(im1)
                        self.pixmap = self.pixmap.scaled(220, 220)
                        self.view.setPixmap(self.pixmap)
                    if im2 is not None:
                        self.pixmap2 = QtGui.QPixmap(im2)
                        self.pixmap2 = self.pixmap2.scaled(220, 220)
                        self.view2.setPixmap(self.pixmap2)
            else:
                print('Sem conexão.')

        self.pushButton_2.clicked.connect(crane)

        self.retranslateUi(Guindaste)
        QtCore.QMetaObject.connectSlotsByName(Guindaste)

    def retranslateUi(self, Guindaste):
        Guindaste.setWindowTitle(_translate("Guindaste", "Laboratório de Projeto III - Grupo A", None))

        self.label_5.setText(_translate("Guindaste", "GUINDASTE TELEOPERADO", None))
        self.label_14.setText(_translate("Guindaste", "Câmera:", None))
        self.label_10.setText(_translate("Guindaste", "Conexão:", None))
        self.label_12.setText(_translate("Guindaste", "Estado do Guindaste:", None))
        self.label_8.setText(_translate("Guindaste", "Estado de Acoplamento:", None))
        self.groupBox_4.setTitle(_translate("Guindaste", "Sistema do Guindaste", None))
        self.pushButton_7.setText(_translate("Guindaste", "Conectar", None))
        # self.pushButton_8.setText(_translate("Guindaste", "Frente", None))
        self.pushButton_2.setText(_translate("Guindaste", "On/Off", None))
        self.groupBox_3.setTitle(_translate("Guindaste", "Controle do Acoplamento", None))
        self.pushButton_6.setText(_translate("Guindaste", "On/Off", None))
        self.label_altura_lanca.setText(_translate("Guindaste", "Altura da lança:", None))
        self.label_distancia_do_caminhao.setText(_translate("Guindaste", "Distância do Caminhão:", None))
        self.label_distancia_lanca.setText(_translate("Guindaste", "Distância da lança:", None))
        self.label_angulo_da_torre.setText(_translate("Guindaste", "Ângulo da torre:", None))
        self.groupBox.setTitle(_translate("Guindaste", "Sistema da torre", None))
        self.groupBox_20.setTitle(_translate("Guindaste", "Sistema do caminhão", None))
        self.groupBox1.setTitle(_translate("Guindaste", "Sistema da lança", None))
        self.groupBox_status.setTitle(_translate("Guindaste", "Status", None))

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Guindaste = QtWidgets.QMainWindow()
    ui = Ui_Guindaste()
    ui.setupUi(Guindaste)
    Guindaste.show()
    sys.exit(app.exec_())

