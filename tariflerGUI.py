from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal
import speech_recognition as sr
import pandas as pd
from tarif_python import tarif
from grafik_python import Grafik

class TariflerGUI(QtWidgets.QStackedWidget):
    #Arayüz Tasarımı
#######################################################################################################################
    def setup(self):
        self.setObjectName("page_tarif")
        self.labelTarif = QtWidgets.QLabel(self)
        self.labelTarif.setGeometry(QtCore.QRect(115, 40, 160, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.labelTarif.setFont(font)
        self.labelTarif.setStyleSheet("color: rgb(54, 80, 115);\n\n")
        self.labelTarif.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTarif.setObjectName("labelTarif")
        self.iconLabelTarif = QtWidgets.QLabel(self)
        self.iconLabelTarif.setGeometry(QtCore.QRect(65, 40, 47, 41))
        self.iconLabelTarif.setStyleSheet("image: url(:/icons/icons/icons8-ingredients-48 (1).png);")
        self.iconLabelTarif.setText("")
        self.iconLabelTarif.setObjectName("iconLabelTarif")
        self.lineEdit_2 = QtWidgets.QLineEdit(self)
        self.lineEdit_2.setGeometry(QtCore.QRect(330, 90, 200, 150))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.lineEdit_2.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.iconLabelYemek = QtWidgets.QLabel(self)
        self.iconLabelYemek.setGeometry(QtCore.QRect(345, 40, 50, 41))
        self.iconLabelYemek.setStyleSheet("image: url(:/icons/icons/icons8-salad-32.png);")
        self.iconLabelYemek.setText("")
        self.iconLabelYemek.setObjectName("iconLabelYemek")
        self.labelYemek = QtWidgets.QLabel(self)
        self.labelYemek.setGeometry(QtCore.QRect(370, 40, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.labelYemek.setFont(font)
        self.labelYemek.setStyleSheet("color: rgb(242, 224, 201);\n""\n""")
        self.labelYemek.setAlignment(QtCore.Qt.AlignCenter)
        self.labelYemek.setObjectName("labelYemek")
        self.textEdit = QtWidgets.QTextEdit(self)
        self.textEdit.setGeometry(QtCore.QRect(70, 90, 200, 150))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.btnMicTarif = QtWidgets.QPushButton(self)
        self.btnMicTarif.setGeometry(QtCore.QRect(70, 245, 95, 25))
        self.btnMicTarif.setStyleSheet("background-color: rgb(48,123,172);")
        self.btnMicTarif.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnMicTarif.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/icons8-microphone-24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnMicTarif.setIcon(icon1)
        self.btnMicTarif.setIconSize(QtCore.QSize(32, 32))
        self.btnMicTarif.setObjectName("btnMicTarif")
        self.btnAraTarif = QtWidgets.QPushButton(self)
        self.btnAraTarif.setGeometry(QtCore.QRect(175, 245, 95, 25))
        self.btnAraTarif.setStyleSheet("background-color: rgb(48,123,172);")
        self.btnAraTarif.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnAraTarif.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/icons8-search-24 (3).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAraTarif.setIcon(icon2)
        self.btnAraTarif.setIconSize(QtCore.QSize(32, 32))
        self.btnAraTarif.setObjectName("btnAraTarif")
        self.btnMicYemek = QtWidgets.QPushButton(self)
        self.btnMicYemek.setGeometry(QtCore.QRect(330, 245, 95, 25))
        self.btnMicYemek.setStyleSheet("background-color: rgb(48,123,172);")
        self.btnMicYemek.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnMicYemek.setText("")
        self.btnMicYemek.setIcon(icon1)
        self.btnMicYemek.setIconSize(QtCore.QSize(32, 32))
        self.btnMicYemek.setObjectName("btnMicYemek")
        self.btnAraYemek = QtWidgets.QPushButton(self)
        self.btnAraYemek.setGeometry(QtCore.QRect(435, 245, 95, 25))
        self.btnAraYemek.setStyleSheet("background-color: rgb(48,123,172);")
        self.btnAraYemek.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnAraYemek.setText("")
        self.btnAraYemek.setIcon(icon2)
        self.btnAraYemek.setIconSize(QtCore.QSize(32, 32))
        self.btnAraYemek.setObjectName("btnAraYemek")
#################################################################################################################

        self.tarif_page = tarif()
        self.grafik_page = Grafik()

        #Buton sinyalleri
        self.btnAraYemek.clicked.connect(self.ara_tarif_getir)
        self.btnMicYemek.clicked.connect(self.mic_tarif_getir)
        self.btnMicTarif.clicked.connect(self.mic_malzeme_oner)
        self.btnAraTarif.clicked.connect(self.ara_malzeme_oner)

        return self

    @QtCore.pyqtSlot()
    def ara_malzeme_oner(self):
        malzemeler = self.textEdit.toPlainText()
        self.alternatifMalzemeOner(malzemeler.strip())  # strip \n hatasını giderir
        self.textEdit.clear()

    @QtCore.pyqtSlot()
    def mic_malzeme_oner(self):
        malzemeler = self.ses()
        if malzemeler:
            self.textEdit.setText(malzemeler)
            self.alternatifMalzemeOner(malzemeler)
        self.textEdit.clear()

    @QtCore.pyqtSlot()
    def ara_tarif_getir(self):
        yemek = self.lineEdit_2.text()
        self.tarifGetir(yemek)
        self.lineEdit_2.clear()

    @QtCore.pyqtSlot()
    def mic_tarif_getir(self):
        yemek = self.ses()
        if yemek:
            self.lineEdit_2.setText(yemek)
            self.tarifGetir(yemek)
        self.lineEdit_2.clear()

    def ses(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:  # mikrofon erişimi
            r.adjust_for_ambient_noise(source)
            audio = r.record(source, duration=5)
            try:
                soylenen = r.recognize_google(audio, language="tr-TR")
                return soylenen
            except:
                print("Malesef anlaşılmadı!!!")

    def tarifGetir(self, yemekIsmi):
        """Kullanıcıdan alınan yemek ismine göre tarifi ekrana bastırır"""
        # projeye eklenmiş tarifler.csv dosyasını DataFrame olarak okur.
        dosya = pd.read_csv('.\\csv_files\\tarifler.csv',
                            names=['Yemek', 'Malzeme1', 'Malzeme2', 'Malzeme3', 'Malzeme4', 'Malzeme5', 'Malzeme6',
                                   'Malzeme7', 'Malzeme8', 'Malzeme9', 'Malzeme10', 'Tarif'])
        # kullanıcıdan tarifini öğrenmek istediği yemeğin ismini alır.
        # yemekIsmi = self.lineEdit_2.text()
        # büyük harf-küçük harf duyarlılığını ortadan kaldırmak için tüm harfleri büyük harf yapar.
        yemekIsmi = yemekIsmi.replace("i", "İ")
        yemekIsmi = yemekIsmi.upper()
        # for döngüsünde değerini güncellediğimiz değişkenleri ilklendirir.
        sorgu = -1
        bulundu = False
        # dosya DataFramenin Yemek başlıklı kayıtlarını gezer ve aranan kaydı bulunca döngüyü sonlandırır.
        for i in dosya.Yemek:
            sorgu += 1
            i = i.strip()
            if i == yemekIsmi:
                bulundu = True
                #print(dosya.iloc[sorgu])  # her şeyi ekrana basar
                liste = []
                liste.extend(dosya.iloc[sorgu])
                break
        # eğer bulundu değişkeni True ile güncellenmemişse ekrana sistemde o tarifin bulunmadığı bilgisini bastırır.
        if not bulundu:
            #print("SİSTEMDE", yemekIsmi, "TARİFİ BULUNMAMAKTADIR.")
            return
        self.tarif_page.tarif_yaz(liste)
        self.tarif_page.show()

    def alternatifMalzemeOner(self, malzemeler):

        malzemeListesi = malzemeler.upper()
        count = 0
        for i in malzemeListesi.split():
            if i == "ŞEKER":

                count += 1
                metin = "Şeker yerine esmer şeker / bal / muz / tarçın / vanilya " \
                        "ya da hurma kullanabilirsiniz."
                image = "background-image: url(:/grafik/icons/grafik/şeker.png);"
            elif i == "UN":

                count += 1
                metin = "Beyaz un yerine yulaf unu / kepekli un / tam buğday unu " \
                        "ya da çavdar unu kullanabilirsiniz."
                image = "background-image: url(:/grafik/icons/grafik/un.png);"
            elif i == "SIVI":

                count += 1
                metin = "Sıvıyağ yerine zeytinyağı ya da tereyağı kullanabilirsiniz."
                image = "background-image: url(:/grafik/icons/grafik/yag.png);"
            elif i == "TAVUK":

                count += 1
                metin = "Tavuk yerine hindi / kaz ya da ördek kullanabilirsiniz."
                image = "background-image: url(:/grafik/icons/grafik/tavuk.png);"
            elif i == "SÜT":

                count += 1
                metin = "Süt yerine light süt / laktozsuz süt / keçi sütü " \
                        "ya da badem sütü kullanabilirsiniz."
                image = "background-image: url(:/grafik/icons/grafik/sut.png);"
            elif i == "DANA":

                count += 1
                metin = "Dana eti yerine koyun eti ya da keçi eti kullanabilirsiniz."
                image = "background-image: url(:/grafik/icons/grafik/et.png);"

            if count == 1:
                self.grafik_page.ui.label_grafik_1.setStyleSheet(image)
                self.grafik_page.ui.textEdit_grafik_yazi1.setText(metin)
            elif count == 2:
                self.grafik_page.ui.label_grafik_2.setStyleSheet(image)
                self.grafik_page.ui.textEdit_grafik_yazi2.setText(metin)
            elif count == 3:
                self.grafik_page.ui.label_grafik_3.setStyleSheet(image)
                self.grafik_page.ui.textEdit_grafik_yazi3.setText(metin)
            elif count == 4:
                self.grafik_page.ui.label_grafik_4.setStyleSheet(image)
                self.grafik_page.ui.textEdit_grafik_yazi4.setText(metin)

        if count != 0:
            if count == 1:
                self.grafik_page.setFixedSize(550, 380)
            elif count == 2:
                self.grafik_page.setFixedSize(950, 450)
            else:
                self.grafik_page.setFixedSize(1000, 900)
            self.grafik_page.show()



    def retranslate(self):

        _translate = QtCore.QCoreApplication.translate

        self.labelTarif.setText(_translate("TariflerGUI", "Malzemeler"))
        self.lineEdit_2.setPlaceholderText(_translate("TariflerGUI", "Yemek ismini giriniz."))
        self.labelYemek.setText(_translate("TariflerGUI", "Yemek"))
        self.textEdit.setPlaceholderText(_translate("TariflerGUI", "Malzemeleri giriniz."))

        return self


