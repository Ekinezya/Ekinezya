from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt


class SeceneklerGUI(QtWidgets.QStackedWidget):
    #Arayüz Tasarımı
#######################################################################################################################
    def setup(self):
        self.setObjectName("page_secenekler")
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_dil_secenegi = QtWidgets.QLabel(self)
        self.label_dil_secenegi.setGeometry(QtCore.QRect(70, 70, 200, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_dil_secenegi.setFont(font)
        self.label_dil_secenegi.setObjectName("label_16")
        self.label_dil_secenegi.setStyleSheet("color:rgb(81, 113, 140);")
        self.comboBox_dil = QtWidgets.QComboBox(self)
        self.comboBox_dil.setGeometry(QtCore.QRect(270, 80, 140, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_dil.setFont(font)
        self.comboBox_dil.setObjectName("comboBox")
        self.comboBox_dil.setEditable(True)
        self.comboBox_dil.lineEdit().setReadOnly(True)
        self.comboBox_dil.lineEdit().setAlignment(Qt.AlignCenter)
        self.comboBox_dil.setStyleSheet("background-color: rgb(48,123,172);")
        self.comboBox_dil.addItem("")
        self.comboBox_dil.addItem("")
        self.label_tema_secenegi = QtWidgets.QLabel(self)
        self.label_tema_secenegi.setGeometry(QtCore.QRect(70, 140, 200, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_tema_secenegi.setFont(font)
        self.label_tema_secenegi.setObjectName("label_17")
        self.comboBox_tema = QtWidgets.QComboBox(self)
        self.comboBox_tema.setGeometry(QtCore.QRect(270, 145, 140, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_tema.setFont(font)
        self.comboBox_tema.setObjectName("comboBox_2")
        self.comboBox_tema.setEditable(True)
        self.comboBox_tema.lineEdit().setReadOnly(True)
        self.comboBox_tema.lineEdit().setAlignment(Qt.AlignCenter)
        self.comboBox_tema.setStyleSheet("background-color: rgb(48,123,172);")
        self.comboBox_tema.addItem("")
        self.comboBox_tema.addItem("")
        self.label_18 = QtWidgets.QLabel(self)
        self.label_18.setGeometry(QtCore.QRect(10, 70, 41, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("image: url(:/icons/icons/icons8-google-translate-52.png);")
        self.label_18.setText("")
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self)
        self.label_19.setGeometry(QtCore.QRect(10, 130, 41, 51))
        self.label_19.setStyleSheet("image: url(:/icons/icons/icons8-change-theme-48.png);")
        self.label_19.setText("")
        self.label_19.setObjectName("label_19")

        return self

    #######################################################################################################################

    def retranslate(self):
        _translate = QtCore.QCoreApplication.translate

        self.label_dil_secenegi.setText(_translate("main", "Uygulama Dili:"))
        self.comboBox_dil.setItemText(0, _translate("main", "Türkçe"))
        self.comboBox_dil.setItemText(1, _translate("main", "İngilizce"))
        self.label_tema_secenegi.setText(_translate("main", "Uygulama Teması:"))
        self.comboBox_tema.setItemText(0, _translate("main", "Aydınlık Tema"))
        self.comboBox_tema.setItemText(1, _translate("main", "Karanlık Tema"))





