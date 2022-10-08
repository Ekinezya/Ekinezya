# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/eyuph/Desktop/Python/Proje/tarif.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Tarif(object):
    def setupUi(self, Tarif):

        #Arayüz Tasarımı
#################################################################################################################
        Tarif.setObjectName("Tarif")
        Tarif.resize(634, 441)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/icons8-salad-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Tarif.setWindowIcon(icon)
        Tarif.setStyleSheet("background-color:rgb(48,123,172);")

        self.formLayoutWidget = QtWidgets.QWidget(Tarif)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 40, 601, 371))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_yemek_ismi = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_yemek_ismi.setFont(font)
        self.label_yemek_ismi.setObjectName("label_yemek_ismi")
        self.label_yemek_ismi.setStyleSheet("color:rgb(242,240,240);")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_yemek_ismi)
        self.lineEdit_yemek_ismi = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_yemek_ismi.setReadOnly(True)
        self.lineEdit_yemek_ismi.setObjectName("lineEdit_yemek_ismi")
        self.lineEdit_yemek_ismi.setStyleSheet("background-color:rgb(242,240,240);")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_yemek_ismi)
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet("color:rgb(242,240,240);")
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.textEdit_malzemeler = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.textEdit_malzemeler.setReadOnly(True)
        self.textEdit_malzemeler.setObjectName("textEdit_malzemeler")
        self.textEdit_malzemeler.setStyleSheet("background-color:rgb(242,240,240);")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.textEdit_malzemeler)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet("color:rgb(242,240,240);")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.textEdit_yapilis = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.textEdit_yapilis.setObjectName("textEdit_yapilis")
        self.textEdit_yapilis.setStyleSheet("background-color:rgb(242,240,240);")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.textEdit_yapilis)
#################################################################################################################

        self.retranslateUi(Tarif)
        QtCore.QMetaObject.connectSlotsByName(Tarif)

    def retranslateUi(self, Tarif):
        _translate = QtCore.QCoreApplication.translate
        Tarif.setWindowTitle(_translate("Tarif", "Tarif"))
        self.label_yemek_ismi.setText(_translate("Tarif", "Yemek İsmi:"))
        self.label.setText(_translate("Tarif", "Malzemeler:"))
        self.label_2.setText(_translate("Tarif", "Yapılışı:"))

import icons_rc

class tarif(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Tarif()
        self.ui.setupUi(self)

    #Çarpıya basıldında clear() fonk. çağır.
    def closeEvent(self, event):
        self.clear()

    #Tüm text kutucuklarını temizle
    def clear(self):
        self.ui.textEdit_yapilis.clear()
        self.ui.textEdit_malzemeler.clear()
        self.ui.lineEdit_yemek_ismi.clear()

    #Yemek ismi ve hazırlanışını yazdır
    def tarif_yaz(self, tarif):
        self.ui.lineEdit_yemek_ismi.setText(tarif[0])
        self.ui.textEdit_yapilis.setText(tarif[11])
        malzemeler = tarif[1:10]
        print(malzemeler)
        for i in malzemeler:
            if type(i) == float:
                continue
            self.ui.textEdit_malzemeler.append(i)