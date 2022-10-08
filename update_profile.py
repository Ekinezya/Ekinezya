from decimal import Decimal
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal
from guncelle_python import Ui_Guncelle

class updateProfile(QMainWindow):
    new_user_signal = pyqtSignal(list)

    def __init__(self):
        super().__init__()
        self.ui = Ui_Guncelle()
        self.ui.setupUi(self)
        self.ui.pushButton_guncelle.clicked.connect(self.update_profile)

    def update_profile(self):
        name = self.ui.lineEdit_guncelle_name.text()
        age = self.ui.lineEdit_guncelle_age.text()
        weight = self.ui.lineEdit_guncelle_weight.text()
        boy = self.ui.lineEdit_guncelle_boy.text()
        cinsiyet = self.ui.comboBox_guncelle_cinsiyet.currentText()
        profile = [name, age, weight, boy, cinsiyet]

        self.new_user_signal.emit(profile)
    def clear(self):
        self.ui.lineEdit_guncelle_name.clear()
        self.ui.lineEdit_guncelle_age.clear()
        self.ui.lineEdit_guncelle_weight.clear()
        self.ui.lineEdit_guncelle_boy.clear()
        self.ui.comboBox_guncelle_cinsiyet.clear()