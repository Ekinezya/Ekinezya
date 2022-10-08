from decimal import Decimal
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal
from PyQt5 import  QtCore
from profile_python import Ui_MainWindow_profile

class Profile(QMainWindow):

    new_user_signal = pyqtSignal(list)

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow_profile()
        self.ui.setupUi(self)

        self.ui.comboBox_profiles_cinsiyet.addItem("Erkek")
        self.ui.comboBox_profiles_cinsiyet.addItem("Kadın")
        self.ui.pushButton_profile_add.clicked.connect(self.new_profile_add)

    @QtCore.pyqtSlot()
    def new_profile_add(self):
        """yeni profili main nesnesine taşır"""
        name = self.ui.lineEdit_name.text()
        age = self.ui.lineEdit_age.text()
        weight = self.ui.lineEdit_weight.text()
        boy = self.ui.lineEdit_profile_boy.text()
        cinsiyet = self.ui.comboBox_profiles_cinsiyet.currentText()
        profile = [name, age, weight, boy, cinsiyet]

        self.new_user_signal.emit(profile)

    def closeEvent(self, event):
        self.clear()

    def clear(self):
        """pencere kapatılınca pencereyi temizler"""
        self.ui.lineEdit_age.clear()
        self.ui.lineEdit_name.clear()
        self.ui.lineEdit_weight.clear()
        self.ui.lineEdit_profile_boy.clear()
        self.ui.comboBox_profiles_cinsiyet.setCurrentText("Erkek")

    def vkiHesapla(self, boy, kilo):
        """kulanıcının boy ve kilo bilgilerine göre vücut kütle indeksini hesaplar"""
        vki = (float(kilo) / (float(boy) * float(boy)))
        return Decimal(vki).quantize(Decimal('.01'))

    def gunlukKaloriIhtiyaciHesapla(self, kilo, cinsiyet):
        """kulanıcının bilgilerine göre günlük kalori ihtiyacını hesaplar"""

        if cinsiyet == "Erkek":
            kalori = Decimal(1 * float(kilo) * 24)
        else:
            kalori = Decimal(0.9 * float(kilo) * 24)
        return Decimal(kalori).quantize(Decimal('.01'))