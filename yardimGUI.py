from PyQt5 import QtCore, QtGui, QtWidgets

class YardimGUI(QtWidgets.QStackedWidget):
    #Arayüz Tasarımı
#######################################################################################################################
    def setup(self):
        self.setObjectName("page_yardim")
        self.label_6 = QtWidgets.QLabel(self)
        self.label_6.setGeometry(QtCore.QRect(80, 200, 421, 271))
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.stackedWidget_2 = QtWidgets.QStackedWidget(self)
        self.stackedWidget_2.setGeometry(QtCore.QRect(10, 30, 601, 481))
        self.stackedWidget_2.setStyleSheet("background-color: rgb(242,240,240);")
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.page)
        self.textBrowser_5.setGeometry(QtCore.QRect(10, 10, 541, 51))
        self.textBrowser_5.setStyleSheet("background-color: rgb(48,123,172);")
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.label = QtWidgets.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(10, 60, 401, 331))
        #self.iconLabelYemek.setStyleSheet("image: url(:/icons/icons/icons8-salad-32.png);")
        self.label.setStyleSheet("image: url(:/icons/icons/page1.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(self.page)
        self.label_5.setGeometry(QtCore.QRect(390, 230, 191, 201))
        self.label_5.setStyleSheet("image: url(:/icons/icons/page1_2.png);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.stackedWidget_2.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.page_2)
        self.textBrowser_4.setGeometry(QtCore.QRect(0, 0, 551, 61))
        self.textBrowser_4.setStyleSheet("background-color: rgb(48,123,172);")
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.label_7 = QtWidgets.QLabel(self.page_2)
        self.label_7.setGeometry(QtCore.QRect(-30, 60, 521, 361))
        self.label_7.setStyleSheet("image: url(:/icons/icons/page2.png);")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.stackedWidget_2.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.page_3)
        self.textBrowser_3.setGeometry(QtCore.QRect(20, 10, 531, 61))
        self.textBrowser_3.setStyleSheet("background-color: rgb(48, 123, 172);")
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.label_8 = QtWidgets.QLabel(self.page_3)
        self.label_8.setGeometry(QtCore.QRect(-20, 80, 541, 371))
        self.label_8.setStyleSheet("image: url(:/icons/icons/page3.png);")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.stackedWidget_2.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.textBrowser = QtWidgets.QTextBrowser(self.page_4)
        self.textBrowser.setGeometry(QtCore.QRect(20, 10, 541, 71))
        self.textBrowser.setStyleSheet("background-color: rgb(48, 123, 172);")
        self.textBrowser.setObjectName("textBrowser")
        self.label_10 = QtWidgets.QLabel(self.page_4)
        self.label_10.setGeometry(QtCore.QRect(0, 80, 471, 331))
        self.label_10.setStyleSheet("image: url(:/icons/icons/page4.png);")
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.page_4)
        self.label_11.setGeometry(QtCore.QRect(220, 290, 381, 181))
        self.label_11.setStyleSheet("image: url(:/icons/icons/page4_2.png);")
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.stackedWidget_2.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.page_5)
        self.textBrowser_2.setGeometry(QtCore.QRect(0, 0, 561, 51))
        self.textBrowser_2.setStyleSheet("background-color: rgb(48, 123, 172);")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.label_9 = QtWidgets.QLabel(self.page_5)
        self.label_9.setGeometry(QtCore.QRect(-20, 60, 461, 331))
        self.label_9.setStyleSheet("image: url(:/icons/icons/page5.png);")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.label_20 = QtWidgets.QLabel(self.page_5)
        self.label_20.setGeometry(QtCore.QRect(230, 260, 341, 201))
        self.label_20.setStyleSheet("image: url(:/icons/icons/page5_2.png);")

        self.label_20.setText("")
        self.label_20.setObjectName("label_20")
        self.stackedWidget_2.addWidget(self.page_5)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.textBrowser_6 = QtWidgets.QTextBrowser(self.page_6)
        self.textBrowser_6.setGeometry(QtCore.QRect(0, 0, 541, 61))
        self.textBrowser_6.setStyleSheet("background-color: rgb(48, 123, 172);")
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.label_12 = QtWidgets.QLabel(self.page_6)
        self.label_12.setGeometry(QtCore.QRect(0, 60, 511, 401))
        self.label_12.setStyleSheet("image: url(:/icons/icons/page6.png);")
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.stackedWidget_2.addWidget(self.page_6)
        self.page_7 = QtWidgets.QWidget()
        self.page_7.setObjectName("page_7")
        self.textBrowser_7 = QtWidgets.QTextBrowser(self.page_7)
        self.textBrowser_7.setGeometry(QtCore.QRect(10, 10, 531, 51))
        self.textBrowser_7.setStyleSheet("background-color: rgb(48, 123, 172);")
        self.textBrowser_7.setObjectName("textBrowser_7")
        self.label_13 = QtWidgets.QLabel(self.page_7)
        self.label_13.setGeometry(QtCore.QRect(-20, 70, 471, 311))
        self.label_13.setStyleSheet("image: url(:/icons/icons/page7.png);")
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.label_21 = QtWidgets.QLabel(self.page_7)
        self.label_21.setGeometry(QtCore.QRect(120, 220, 461, 241))
        self.label_21.setStyleSheet("image: url(:/icons/icons/page7_2.png);")

        self.label_21.setText("")
        self.label_21.setObjectName("label_21")
        self.stackedWidget_2.addWidget(self.page_7)
        self.page_8 = QtWidgets.QWidget()
        self.page_8.setObjectName("page_8")
        self.textBrowser_8 = QtWidgets.QTextBrowser(self.page_8)
        self.textBrowser_8.setGeometry(QtCore.QRect(0, 0, 531, 51))
        self.textBrowser_8.setStyleSheet("background-color: rgb(48, 123, 172);")
        self.textBrowser_8.setObjectName("textBrowser_8")
        self.label_14 = QtWidgets.QLabel(self.page_8)
        self.label_14.setGeometry(QtCore.QRect(-20, 60, 381, 251))

        self.label_14.setStyleSheet("image: url(:/icons/icons/page8.png);")

        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.page_8)
        self.label_15.setGeometry(QtCore.QRect(130, 210, 491, 251))
        self.label_15.setStyleSheet("image: url(:/icons/icons/page8_2.png);")
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")
        self.stackedWidget_2.addWidget(self.page_8)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(320, 500, 281, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.pushButton_geri = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_geri.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/geri.ico"), QtGui.QIcon.Normal,QtGui.QIcon.Off)

        self.pushButton_geri.setIcon(icon3)
        self.pushButton_geri.setObjectName("geri")
        self.horizontalLayout.addWidget(self.pushButton_geri)

        self.pushButton_ileri = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_ileri.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons/ileri.ico"), QtGui.QIcon.Normal,QtGui.QIcon.Off)
        self.pushButton_ileri.setIcon(icon4)
        self.pushButton_ileri.setObjectName("ileri")
        self.horizontalLayout.addWidget(self.pushButton_ileri)
#######################################################################################################################

        #Sinyaller
        self.pushButton_ileri.clicked.connect(self.go_forward_page)
        self.pushButton_geri.clicked.connect(self.go_backward_page)

        return self

    @QtCore.pyqtSlot()
    def go_forward_page(self):
        """StackedWidget sayfasını bir ilerlet"""
        self.stackedWidget_2.setCurrentIndex(self.stackedWidget_2.currentIndex() + 1)

    @QtCore.pyqtSlot()
    def go_backward_page(self):
        """StackedWidget sayfasını bir geri götür"""
        self.stackedWidget_2.setCurrentIndex(self.stackedWidget_2.currentIndex() - 1)

    def retranslate(self):
        _translate = QtCore.QCoreApplication.translate
        self.pushButton_geri.setToolTip('Önceki sayfa için tıklayın')
        self.pushButton_ileri.setToolTip('Sonraki sayfa için tıklayın')

        self.textBrowser_5.setHtml(_translate("main",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">Profilim ekranındaki ekle butonuna basınız ve bilgilerinizi giriniz.</span></p></body></html>"))
        self.textBrowser_4.setHtml(_translate("main",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600; color:#ffffff;\">Girdiğiniz bilgilerinizle birlikte vücut kitle indeksiniz ve günlük kalori ihtiyacınızı hesaplayacaktır.</span></p></body></html>"))
        self.textBrowser_3.setHtml(_translate("main",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600; color:#ffffff;\">Dilerseniz seçili profili güncelle butonundan girdiğiniz bilgileri yenileriyle değiştirebilirsiniz </span></p></body></html>"))
        self.textBrowser.setHtml(_translate("main",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600; color:#ffffff;\">Tariflerim sayfasındaki malzemeler bölümünde klavyeden ya da sesli komut ile girdiğiniz malzemelerin alternatiflerini grafik halinde görebilirsiniz.</span></p></body></html>"))
        self.textBrowser_2.setHtml(_translate("main",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600; color:#ffffff;\">Tariflerim sayfasındaki yemek bölümünde klavyeden ya da sesli komut ile girdiğiniz tarif ismi ile tarifin malzemelerini ve yapılışını görebilirsiniz</span></p></body></html>"))
        self.textBrowser_6.setHtml(_translate("main",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600; color:#ffffff;\">Besinler ekranında istediğiniz besine tıklayarak besin değerleri oranını görebilirsiniz </span></p>\n"
                                              "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt; font-weight:600; color:#550000;\"><br /></p></body></html>"))
        self.textBrowser_7.setHtml(_translate("main",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600; color:#ffffff;\">Seçenekler ekranından uygulama dilini ayarlayarak uygulamayı Türkçe ya da İngilizce olarak kullanabilirsiniz</span></p>\n"
                                              "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt; font-weight:600; color:#ffffff;\"><br /></p></body></html>"))
        self.textBrowser_8.setHtml(_translate("main",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600; color:#ffffff;\">Seçenekler ekranından uygulamanın temasını aydınlık ya da karanlık olarak ayarlayabilirsiniz</span></p>\n"
                                              "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt; font-weight:600; color:#ffffff;\"><br /></p></body></html>"))
        return self