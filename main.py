from main_menu_python import Ui_main
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtCore import QTranslator
import sys
import csv
from profilimGUI import ProfilimGUI



data_path= 'profiller.csv', 'besin_degerleri.csv', 'tarifler.csv'

#TODO:Besinlerin grafikleri ?
#TODO:Speech-to-text bug
#TODO:Statusbar mesajları


class main(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_main()
        self.ui.setupUi(self)
        self.ui.set_main_styleSheet(self)
        self.trans = QTranslator(self)#dil
        self.dil_degis(self)#dil

        #Ana stackedwidget sayfa indeksleri
        self.page_profilim_index = 1
        self.page_tarif_index = 2
        self.page_besin_index = 3
        self.page_secenekler_index = 4
        self.page_yardim_index = 5

        #Status Bar süresi
        self.statusBarTime = 3000

        # Toolbar ve stackedwidget sayfaları arasındaki bağlantılar
        self.ui.actionTarifler.triggered.connect(self.go_page_tarif)
        self.ui.actionProfil.triggered.connect(self.go_page_profilim)
        self.ui.actionBesinler.triggered.connect(self.go_page_besin)
        self.ui.actionSecenekler.triggered.connect(self.go_page_secenekler)
        self.ui.actionYardim.triggered.connect(self.go_page_yardim)

        #Açılışta tarif ekranına yönlendir
        self.go_page_profilim()

        # Açılışta kayıtlı profilleri uygulamaya yükle
        self.profil = ProfilimGUI()
        self.profil.setup()
        self.profilleri_yukle()

        #Karanlık tema
        #connect metoduna argümanlı fonksiyon gönderebilmek için lambda kullanıldı
        self.ui.secenekler.comboBox_tema.currentIndexChanged['int'].connect(lambda : self.ui.set_main_styleSheet(self))
        self.ui.secenekler.comboBox_dil.currentIndexChanged.connect(self.dil_degis)#dil

        #Tarif-StatusBar sinyaller
        self.ui.tarif.btnAraTarif.clicked.connect(self.stasusBar_message_ara_malzeme)
        self.ui.tarif.btnMicTarif.clicked.connect(self.statusBar_message_mic_malzeme)
        self.ui.tarif.btnAraYemek.clicked.connect(self.statusBar_message_ara_yemek)
        self.ui.tarif.btnMicYemek.clicked.connect(self.statusBar_message_mic_yemek)

        #Profil-StatusBar sinyaller
        self.ui.profil.pushButton_add.clicked.connect(self.statusBar_message_profil_ekle)
        self.ui.profil.pushButton_update.clicked.connect(self.statusBar_message_profil_guncelle)
        self.ui.profil.pushButton_delete.clicked.connect(self.statusBar_message_profil_sil)

        #Seçenekler-StatusBar sinyalleri
        self.ui.secenekler.comboBox_dil.currentIndexChanged.connect(self.statusBar_dil_secenegi)
        self.ui.secenekler.comboBox_tema.currentIndexChanged.connect(self.statusBar_tema_secenegi)

        #Yardım-StatusBar sinyaller
        self.ui.yardim.pushButton_ileri.clicked.connect(self.statusBar_yardim_ileri)
        self.ui.yardim.pushButton_geri.clicked.connect(self.statusBar_yardim_geri)



    @QtCore.pyqtSlot()
    def stasusBar_message_ara_malzeme(self):
        self.ui.status_main.showMessage('Sistemde var olan daha sağlıklı malzemeler...',self.statusBarTime)

    @QtCore.pyqtSlot()
    def statusBar_message_mic_malzeme(self):
        self.ui.status_main.showMessage('Ekinezya sizi dinliyor...',self.statusBarTime)

    @QtCore.pyqtSlot()
    def statusBar_message_mic_yemek(self):
        self.ui.status_main.showMessage('Ekinezya sizi dinliyor...',self.statusBarTime)

    @QtCore.pyqtSlot()
    def statusBar_message_ara_yemek(self):
        pass
        # self.ui.status_main.showMessage('Sistemde var olan yemek tarifi...',self.statusBarTime)

    @QtCore.pyqtSlot()
    def statusBar_message_profil_ekle(self):
        self.ui.status_main.showMessage('Yeni profil ekle',self.statusBarTime)

    @QtCore.pyqtSlot()
    def statusBar_message_profil_guncelle(self):
        self.ui.status_main.showMessage('Seçili profili güncelle',self.statusBarTime)

    @QtCore.pyqtSlot()
    def statusBar_message_profil_sil(self):
        self.ui.status_main.showMessage('Seçili profili sil',self.statusBarTime)

    @QtCore.pyqtSlot()
    def statusBar_dil_secenegi(self):
        if self.ui.secenekler.comboBox_dil.currentIndex() == 0:
            self.ui.status_main.showMessage('Seçilen dil:Türkçe',self.statusBarTime)
        else:
            self.ui.status_main.showMessage('Seçilen dil:İngilizce',self.statusBarTime)

    @QtCore.pyqtSlot()
    def statusBar_tema_secenegi(self):
        if self.ui.secenekler.comboBox_tema.currentIndex() == 0:
            self.ui.status_main.showMessage('Seçilen tema:Aydınlık',self.statusBarTime)
        else:
            self.ui.status_main.showMessage('Seçilen tema:Karanlık',self.statusBarTime)

    @QtCore.pyqtSlot()
    def statusBar_yardim_ileri(self):
        message = 'Sayfa {}/7'.format(self.ui.yardim.stackedWidget_2.currentIndex())
        self.ui.status_main.showMessage(message)

    @QtCore.pyqtSlot()
    def statusBar_yardim_geri(self):
        message = 'Sayfa {}/7'.format(self.ui.yardim.stackedWidget_2.currentIndex())
        self.ui.status_main.showMessage(message)

    @QtCore.pyqtSlot()
    def go_page_tarif(self):
        #Sayfayı tıklanan indekse göre değiştir
        self.ui.stackedWidget.setCurrentIndex(self.page_tarif_index)
        #Status bar ile kullanıcıyı bilgilendir
        self.ui.status_main.showMessage('Tarif ekranındasınız',self.statusBarTime)

    @QtCore.pyqtSlot()
    def go_page_profilim(self):
        self.ui.stackedWidget.setCurrentIndex(self.page_profilim_index)
        self.ui.status_main.showMessage('Profilim ekranındasınız', self.statusBarTime)
        self.ui.tarif.textEdit.clear()  # tarif sayfasından başka sayfaya geçince textler silinir
        self.ui.tarif.lineEdit_2.clear()

    @QtCore.pyqtSlot()
    def go_page_besin(self):
        self.ui.stackedWidget.setCurrentIndex(self.page_besin_index)
        self.ui.status_main.showMessage('Besinler ekranındasınız', self.statusBarTime)
        self.ui.tarif.textEdit.clear()  # tarif sayfasından başka sayfaya geçince textler silinir
        self.ui.tarif.lineEdit_2.clear()

    @QtCore.pyqtSlot()
    def go_page_secenekler(self):
        self.ui.stackedWidget.setCurrentIndex(self.page_secenekler_index)
        self.ui.status_main.showMessage('Seçenekler ekranındasınız', self.statusBarTime)
        self.ui.tarif.textEdit.clear()  # tarif sayfasından başka sayfaya geçince textler silinir
        self.ui.tarif.lineEdit_2.clear()

    @QtCore.pyqtSlot()
    def go_page_yardim(self):
        self.ui.status_main.showMessage('Yardım ekranındasınız', self.statusBarTime)
        self.ui.stackedWidget.setCurrentIndex(self.page_yardim_index)
        self.ui.tarif.textEdit.clear()  # tarif sayfasından başka sayfaya geçince textler silinir
        self.ui.tarif.lineEdit_2.clear()


    @QtCore.pyqtSlot(int)
    def dil_degis(self, currentIndex):
        #dil = self.secenekler.comboBox_2.currentIndex()
        if currentIndex == 0:
            local = "tr_TR"
            self.trans.load(local)
            QApplication.instance().installTranslator(self.trans)

        elif currentIndex == 1:
            local = "en_US"
            self.trans.load(local)
            QApplication.instance().installTranslator(self.trans)

    @QtCore.pyqtSlot(int)
    def changeEvent(self, event):
        # dil değiştirirken kullanılıyor
        if event.type() == QtCore.QEvent.LanguageChange:
            self.ui.retranslateUi(self)
        super(main, self).changeEvent(event)


    def profilleri_yukle(self):
        """csv dosyasındaki profilleri uygulamaya yükler"""
        #dosyayı okuma modunda aç
        with open('.\\csv_files\\profiller.csv', 'r') as read_obj:
            #csv reader nesnesine dosyayı ata
            csv_reader = csv.reader(read_obj)
            # Satırları gez
            for profile in csv_reader:
                if profile != []:
                    # profili yaz
                    name = profile[0]
                    self.profil.profiles.append(profile)
                    self.ui.profil.comboBox_profiller.addItem(name)

        self.profil.comboBox_index_change()


#Arayüz uygulamasını çalıştır
app = QApplication(sys.argv)
app.setStyle("Fusion")
pencere = main()
pencere.show()
app.exec_()

"""dosyayı okuma modunda aç"""
with open('.\\csv_files\\profiller.csv', "w", newline='') as profiller:
    writer = csv.writer(profiller)
    #profiller dosyasında gez
    for i in pencere.profil.profiles:
        if i:
            writer.writerow(i)