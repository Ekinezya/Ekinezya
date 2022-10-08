from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow

class HomeGUI(QtWidgets.QStackedWidget):
    def setup(self):
        self.page_home = QtWidgets.QWidget()
        self.page_home.setObjectName("page_home")
        self.label_2 = QtWidgets.QLabel(self.page_home)
        self.label_2.setGeometry(QtCore.QRect(190, 0, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(81, 113, 140);")
        self.label_2.setObjectName("label_2")
    def retranslate(self,main):
        _translate = QtCore.QCoreApplication.translate
        self.label_2.setText(_translate("main", "Ana Ekran"))