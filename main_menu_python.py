# -*- coding: utf-8 -*-

from PyQt5 import QtCore,QtGui,QtWidgets
from tariflerGUI import TariflerGUI
from profilimGUI import ProfilimGUI
from besinlerGUI import BesinlerGUI
from seceneklerGUI import SeceneklerGUI
from yardimGUI import YardimGUI


class Ui_main(object):
    #Arayüz Tasarımı
#################################################################################################################################
    def setupUi(self, main):
        main.setObjectName("main")
        main.resize(800, 600)
        main.setMinimumSize(QtCore.QSize(800, 600))
        main.setMaximumSize(QtCore.QSize(16777215, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/book.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        main.setWindowIcon(icon)

        self.centralwidget = QtWidgets.QWidget(main)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 611, 551))
        self.stackedWidget.setObjectName("stackedWidget")

        self.page_home = QtWidgets.QWidget()
        self.page_home.setObjectName("page_home")
        self.label_2 = QtWidgets.QLabel(self.page_home)
        self.label_2.setGeometry(QtCore.QRect(190, 0, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.stackedWidget.addWidget(self.page_home)

        #Profil sayfasıyla ilgili arayüz kodlarını çağır
        self.page_profilim = QtWidgets.QWidget()
        self.profil = ProfilimGUI()
        self.page_profilim = self.profil.setup()

        self.stackedWidget.addWidget(self.page_profilim)

        self.page_tarif = QtWidgets.QWidget()
        self.tarif = TariflerGUI()
        self.page_tarif = self.tarif.setup()

        self.stackedWidget.addWidget(self.page_tarif)

        self.page_besin = QtWidgets.QWidget()
        self.besin = BesinlerGUI()
        self.page_besin = self.besin.setup()

        self.stackedWidget.addWidget(self.page_besin)

        self.page_secenekler = QtWidgets.QWidget()
        self.secenekler = SeceneklerGUI()
        self.page_secenekler = self.secenekler.setup()

        self.stackedWidget.addWidget(self.page_secenekler)

        self.page_yardim = QtWidgets.QWidget()
        self.yardim = YardimGUI()
        self.page_yardim = self.yardim.setup()

        self.stackedWidget.addWidget(self.page_yardim)

        main.setCentralWidget(self.centralwidget)

        self.status_main = QtWidgets.QStatusBar(main)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.status_main.setFont(font)
        self.status_main.setObjectName("status_main")
        main.setStatusBar(self.status_main)

        self.toolBar = QtWidgets.QToolBar(main)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.toolBar.setFont(font)
        self.toolBar.setMovable(True)
        self.toolBar.setIconSize(QtCore.QSize(48, 48))
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolBar.setObjectName("toolBar")
        self.toolBar.setMinimumWidth(180)
        main.addToolBar(QtCore.Qt.LeftToolBarArea, self.toolBar)

        self.action_profil = QtWidgets.QAction(main)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)

        self.action_profil.setFont(font)
        self.action_profil.setObjectName("action_profil")

        self.actionProfil = QtWidgets.QAction(main)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons/icons8-account-26.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionProfil.setIcon(icon4)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(50)
        self.actionProfil.setFont(font)
        self.actionProfil.setObjectName("actionProfil")

        self.actionTarifler = QtWidgets.QAction(main)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/icons8-bake-48 (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionTarifler.setIcon(icon3)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(50)
        self.actionTarifler.setFont(font)
        self.actionTarifler.setObjectName("actionTarifler")


        self.actionSecenekler = QtWidgets.QAction(main)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/icons/icons8-settings-32 (4).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSecenekler.setIcon(icon5)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.actionSecenekler.setFont(font)
        self.actionSecenekler.setObjectName("actionSecenekler")
        self.actionBesinler = QtWidgets.QAction(main)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/icons/icons8-pear-24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBesinler.setIcon(icon6)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.actionBesinler.setFont(font)
        self.actionBesinler.setObjectName("actionBesinler")
        self.actionYardim = QtWidgets.QAction(main)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/icons/icons8-user-manual-32 (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionYardim.setIcon(icon7)
        font = QtGui.QFont()
        font.setPointSize(14)

        self.actionYardim.setFont(font)
        self.actionYardim.setObjectName("actionYardim")
        self.toolBar.addAction(self.actionProfil)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionTarifler)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionBesinler)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionSecenekler)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionYardim)

        self.retranslateUi(main)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(main)


#################################################################################################################################

    def retranslateUi(self, main):
        _translate = QtCore.QCoreApplication.translate

        main.setWindowTitle(_translate("main", "Ekinezya"))
        self.label_2.setText(_translate("main", "Ana Ekran"))

        self.page_tarif = self.tarif.retranslate()
        self.page_profilim = self.profil.retranslate()
        self.page_besin = self.besin.retranslate()
        self.page_secenekler = self.secenekler.retranslate()
        self.page_yardim = self.yardim.retranslate()

        self.toolBar.setWindowTitle(_translate("main", "toolBar"))
        self.action_profil.setText(_translate("main", "profil"))
        self.actionTarifler.setText(_translate("main", "Tarifler"))
        self.actionTarifler.setToolTip(_translate("main", "<html><head/><body><p><span style=\" font-size:16pt;\">Tarifler</span></p></body></html>"))
        self.actionProfil.setText(_translate("main", "Profilim"))
        self.actionSecenekler.setText(_translate("main", "Seçenekler"))
        self.actionBesinler.setText(_translate("main", "Besinler"))
        self.actionYardim.setText(_translate("main", "Yardım"))

    @QtCore.pyqtSlot()
    def set_main_styleSheet(self,main):
        #Aydınlık modu etkinleştir
        if self.secenekler.comboBox_tema.currentIndex() == 0:
            self.toolBar.setStyleSheet("#toolBar{\n""background-color: rgb(48,123,172);\n""}")
            main.setStyleSheet("#centralwidget{\n""background-color: rgb(242,240,240);\n""}")
            self.stackedWidget.setStyleSheet("")
            self.label_2.setStyleSheet("color: rgb(81, 113, 140);")
            self.tarif.btnAraTarif.setStyleSheet("background-color: rgb(48,123,172);")
            self.tarif.btnMicTarif.setStyleSheet("background-color: rgb(48,123,172);")
            self.tarif.btnAraYemek.setStyleSheet("background-color: rgb(48,123,172);")
            self.tarif.btnMicYemek.setStyleSheet("background-color: rgb(48,123,172);")
            self.tarif.labelTarif.setStyleSheet("color: rgb(54, 80, 115);")
            self.tarif.labelYemek.setStyleSheet("color: rgb(54, 80, 115);")
            self.besin.label_besin_degerleri.setStyleSheet("border-color: rgb(85, 0, 255);\n"
                                                        "background-color: rgb(48,123,172);\n""\n"
                                                        "color:rgb(242,240,240);""")

            self.profil.pushButton_add.setStyleSheet("background-color: rgb(242,240,255);")
            self.profil.pushButton_delete.setStyleSheet("background-color: rgb(242,240,255);")
            self.profil.pushButton_update.setStyleSheet("background-color: rgb(242,240,255);")

            self.secenekler.label_dil_secenegi.setStyleSheet("color:rgb(0, 0, 0);")
            self.secenekler.label_tema_secenegi.setStyleSheet("color:rgb(0, 0, 0);")
            self.profil.label_name.setStyleSheet("color: rgb(0, 0, 0);")
            self.profil.label_boy.setStyleSheet("color: rgb(0, 0, 0);")
            self.profil.label_age.setStyleSheet("color: rgb(0, 0, 0);")
            self.profil.label_weight.setStyleSheet("color: rgb(0, 0, 0);")
            self.profil.label_cinsiyet.setStyleSheet("color: rgb(0, 0, 0);")
            self.profil.label_kitle_indeks.setStyleSheet("color: rgb(0, 0, 0);")
            self.profil.label_kalori_ihtiyac.setStyleSheet("color: rgb(0, 0, 0);")
            self.profil.label_name_.setStyleSheet("color: rgb(0, 0, 0);")
            self.profil.label_boy_.setStyleSheet("color: rgb(0, 0, 0);")
            self.profil.label_age_.setStyleSheet("color: rgb(0, 0, 0);")
            self.profil.label_weight_.setStyleSheet("color: rgb(0, 0, 0);")
            self.profil.label_cinsiyet_.setStyleSheet("color: rgb(0, 0, 0);")
            self.profil.label_kitle_indeks_.setStyleSheet("color: rgb(0, 0, 0);")
            self.profil.label_kalori_ihtiyac_.setStyleSheet("color: rgb(0, 0, 0);")
            self.profil.label_profil_secin.setStyleSheet("background-color: rgb(48,123,172);"
                                                         "color:rgb(242,240,240);")
            self.profil.comboBox_profiller.setStyleSheet("background-color: rgb(48,123,172);"
                                                       "color:rgb(242,240,240);")

            self.secenekler.comboBox_dil.setStyleSheet("background-color: rgb(48,123,172);"
                                                       "color:rgb(242,240,240);")
            self.secenekler.comboBox_tema.setStyleSheet("background-color: rgb(48,123,172);"
                                                       "color:rgb(242,240,240);")
        #Karanlık modu etkinleştir
        else:
            self.toolBar.setStyleSheet("#toolBar{\n""background-color: rgb(56, 58, 62);\n""}")
            main.setStyleSheet("#centralwidget{\n""background-color: rgb(30, 31, 38);\n""}")
            self.stackedWidget.setStyleSheet("")
            self.label_2.setStyleSheet("color: rgb(81, 113, 140);")
            self.tarif.btnAraTarif.setStyleSheet("background-color: rgb(56, 58, 62);")
            self.tarif.btnMicTarif.setStyleSheet("background-color: rgb(56, 58, 62);")
            self.tarif.btnAraYemek.setStyleSheet("background-color: rgb(56, 58, 62);")
            self.tarif.btnMicYemek.setStyleSheet("background-color: rgb(56, 58, 62);")
            self.tarif.labelTarif.setStyleSheet("color: rgb(242, 224, 201);")
            self.tarif.labelYemek.setStyleSheet("color: rgb(242, 224, 201);")
            self.besin.label_besin_degerleri.setStyleSheet("border-color: rgb(85, 0, 255);\n"
                                                           "background-color: rgb(66, 82, 90);\n""\n"
                                                           "color: rgb(242, 224, 201);""")
            self.profil.pushButton_add.setStyleSheet("background-color: rgb(56, 58, 62);")
            self.profil.pushButton_delete.setStyleSheet("background-color: rgb(56, 58, 62);")
            self.profil.pushButton_update.setStyleSheet("background-color: rgb(56, 58, 62);")

            self.secenekler.label_dil_secenegi.setStyleSheet("color: rgb(242, 224, 201);")
            self.secenekler.label_tema_secenegi.setStyleSheet("color: rgb(242, 224, 201);")
            self.profil.label_name.setStyleSheet("color: rgb(242, 224, 201);")
            self.profil.label_boy.setStyleSheet("color: rgb(242, 224, 201);")
            self.profil.label_age.setStyleSheet("color: rgb(242, 224, 201);")
            self.profil.label_weight.setStyleSheet("color: rgb(242, 224, 201);")
            self.profil.label_cinsiyet.setStyleSheet("color: rgb(242, 224, 201);")
            self.profil.label_kitle_indeks.setStyleSheet("color: rgb(242, 224, 201);")
            self.profil.label_kalori_ihtiyac.setStyleSheet("color: rgb(242, 224, 201);")
            self.profil.label_name_.setStyleSheet("color: rgb(242, 224, 201);")
            self.profil.label_boy_.setStyleSheet("color: rgb(242, 224, 201);")
            self.profil.label_age_.setStyleSheet("color: rgb(242, 224, 201);")
            self.profil.label_weight_.setStyleSheet("color: rgb(242, 224, 201);")
            self.profil.label_cinsiyet_.setStyleSheet("color: rgb(242, 224, 201);")
            self.profil.label_kitle_indeks_.setStyleSheet("color: rgb(242, 224, 201);")
            self.profil.label_kalori_ihtiyac_.setStyleSheet("color: rgb(242, 224, 201);")
            self.profil.label_profil_secin.setStyleSheet("background-color: rgb(56, 58, 62);"
                                                         "color:rgb(242,240,240);")
            self.profil.comboBox_profiller.setStyleSheet("background-color: rgb(56, 58, 62);"
                                                         "color:rgb(242,240,240);")
            self.secenekler.comboBox_dil.setStyleSheet("background-color: rgb(56, 58, 62);"
                                                       "color:rgb(242,240,240);")
            self.secenekler.comboBox_tema.setStyleSheet("background-color: rgb(56, 58, 62);"
                                                        "color:rgb(242,240,240);")
import icons_rc
import besinler_rc