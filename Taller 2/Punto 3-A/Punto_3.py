# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Punto_3.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(728, 623)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        Dialog.setFont(font)
        Dialog.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.Lista = QtWidgets.QComboBox(Dialog)
        self.Lista.setGeometry(QtCore.QRect(40, 80, 131, 22))
        self.Lista.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Lista.setObjectName("Lista")
        self.Lista.addItem("")
        self.Lista.addItem("")
        self.Lista.addItem("")
        self.Lista.addItem("")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(80, 40, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setScaledContents(False)
        self.label.setWordWrap(False)
        self.label.setOpenExternalLinks(False)
        self.label.setObjectName("label")
        self.Img_robot = QtWidgets.QLabel(Dialog)
        self.Img_robot.setGeometry(QtCore.QRect(230, 20, 481, 251))
        self.Img_robot.setText("")
        self.Img_robot.setScaledContents(True)
        self.Img_robot.setObjectName("Img_robot")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(30, 440, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 400, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(50, 480, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(30, 520, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(110, 560, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(20, 360, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 300, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setTextFormat(QtCore.Qt.PlainText)
        self.label_4.setScaledContents(False)
        self.label_4.setWordWrap(False)
        self.label_4.setOpenExternalLinks(False)
        self.label_4.setObjectName("label_4")
        self.Logo_u = QtWidgets.QLabel(Dialog)
        self.Logo_u.setGeometry(QtCore.QRect(330, 360, 381, 251))
        self.Logo_u.setText("")
        self.Logo_u.setPixmap(QtGui.QPixmap("/home/pi/Documents/Electiva_Robotica/Taller 2/logo-ecci.png"))
        self.Logo_u.setScaledContents(True)
        self.Logo_u.setObjectName("Logo_u")
        self.Art = QtWidgets.QTextEdit(Dialog)
        self.Art.setGeometry(QtCore.QRect(150, 290, 561, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Art.setFont(font)
        self.Art.setObjectName("Art")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.Lista.currentIndexChanged.connect(self.lISTA_DLESP)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Lista.setItemText(0, _translate("Dialog", "Seleccione"))
        self.Lista.setItemText(1, _translate("Dialog", "Cartesiano"))
        self.Lista.setItemText(2, _translate("Dialog", "Esférico"))
        self.Lista.setItemText(3, _translate("Dialog", "Cilíndrico"))
        self.label.setText(_translate("Dialog", "Robot"))
        self.label_7.setText(_translate("Dialog", "Juan Camio Luna Calderon - 90522"))
        self.label_3.setText(_translate("Dialog", "Wendy Dayan Silva Venegas - 66934"))
        self.label_8.setText(_translate("Dialog", "Juan Bernal Garcia - 87190"))
        self.label_9.setText(_translate("Dialog", "Ing Mecatronica. Electiva de robotica"))
        self.label_10.setText(_translate("Dialog", "2024-1"))
        self.label_6.setText(_translate("Dialog", "Juan Esteban Sanchez Lamprea - 66912"))
        self.label_4.setText(_translate("Dialog", "Articulaciones:"))
    def lISTA_DLESP(self):
        _translate = QtCore.QCoreApplication.translate
        func_index = self.Lista.currentIndex()
        if func_index == 1:
            self.Img_robot.setPixmap(QtGui.QPixmap("E:/Informacion/u/Electiva Robotica/Taller 2/Punto 3/cartesiano.png"))
            self.Art.setText(_translate("Dialog", "3 articulaciones deslizantes"))
        elif func_index == 2:
            self.Img_robot.setPixmap(QtGui.QPixmap("E:/Informacion/u/Electiva Robotica/Taller 2/Punto 3/esferico.png"))
            self.Art.setText(_translate("Dialog", "2 articulaciones rotacionales y 1 lineal"))
        elif func_index == 3:
            self.Img_robot.setPixmap(QtGui.QPixmap("E:/Informacion/u/Electiva Robotica/Taller 2/Punto 3/cilíndrico.png"))
            self.Art.setText(_translate("Dialog", "1 articulación de revolución y 2 prismáticas"))    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
