# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/eyuph/Desktop/Python/Proje/profile.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow_profile(object):

    def setupUi(self, MainWindow_profile):
        MainWindow_profile.setObjectName("MainWindow_profile")
        MainWindow_profile.resize(359, 308)
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow_profile.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/icon_profile.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow_profile.setWindowIcon(icon)
        MainWindow_profile.setIconSize(QtCore.QSize(60, 60))
        self.centralwidget = QtWidgets.QWidget(MainWindow_profile)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(40, 40, 291, 181))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_profile_name = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_profile_name.setMinimumSize(QtCore.QSize(50, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_profile_name.setFont(font)
        self.label_profile_name.setObjectName("label_profile_name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_profile_name)
        self.label_profile_age = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_profile_age.setMinimumSize(QtCore.QSize(50, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_profile_age.setFont(font)
        self.label_profile_age.setObjectName("label_profile_age")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_profile_age)
        self.lineEdit_age = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_age.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_age.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_age.setObjectName("lineEdit_age")

        #Validator(Text kutucuğu sadece int veri alabilir)
        self.lineEdit_age.setValidator(QtGui.QIntValidator())  # düzenlendi
        self.lineEdit_age.setMaxLength(3)  # düzenlendi

        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_age)
        self.label_profile_weight = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_profile_weight.setMinimumSize(QtCore.QSize(50, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_profile_weight.setFont(font)
        self.label_profile_weight.setObjectName("label_profile_weight")

        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_profile_weight)
        self.lineEdit_weight = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_weight.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_weight.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEdit_weight.setObjectName("lineEdit_weight")

        reg_ex = QtCore.QRegExp("[0-9][0-9][0-9]?[.][0-9][0-9]")
        input_validator = QtGui.QRegExpValidator(reg_ex, self.lineEdit_weight)  # değiştirildi
        self.lineEdit_weight.setValidator(input_validator)

        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_weight)
        self.lineEdit_name = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_name.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_name.setInputMethodHints(QtCore.Qt.ImhLatinOnly)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.lineEdit_name.text().encode(encoding='utf-8')

        #Validator,regex kullanılarak girilebilecek ismin formatı düzenlendi
        reg_ex = QtCore.QRegExp("(([a-z-A-Z_]+)?[İ,ı,ö,Ö,ü,Ü,ç,Ç,Ğ,ğ,ş,Ş, ])*")
        input_validator = QtGui.QRegExpValidator(reg_ex, self.lineEdit_name)  # değiştirildi
        self.lineEdit_name.setMaxLength(17)
        self.lineEdit_name.setValidator(input_validator)

        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_name)
        self.label_profile_boy = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_profile_boy.setObjectName("label_profile_boy")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_profile_boy)
        self.lineEdit_profile_boy = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_profile_boy.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEdit_profile_boy.setObjectName("lineEdit_profile_boy")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_profile_boy)

        reg_ex = QtCore.QRegExp("[0-2][.][0-9][0-9]")
        input_validator = QtGui.QRegExpValidator(reg_ex, self.lineEdit_profile_boy)  # değiştirildi
        self.lineEdit_profile_boy.setMaxLength(4)
        self.lineEdit_profile_boy.setValidator(input_validator)

        self.label_profile_cinsiyet = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_profile_cinsiyet.setObjectName("label_profile_cinsiyet")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_profile_cinsiyet)
        self.comboBox_profiles_cinsiyet = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox_profiles_cinsiyet.setObjectName("comboBox_profiles_cinsiyet")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.comboBox_profiles_cinsiyet)

        self.pushButton_profile_add = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_profile_add.setGeometry(QtCore.QRect(120, 240, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_profile_add.setFont(font)
        self.pushButton_profile_add.setObjectName("pushButton_profile_add")
        MainWindow_profile.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow_profile)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_profile)

    def retranslateUi(self, MainWindow_profile):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_profile.setWindowTitle(_translate("MainWindow_profile", "Kullanıcı ekle"))
        self.label_profile_name.setText(_translate("MainWindow_profile", " İsim:"))
        self.label_profile_age.setText(_translate("MainWindow_profile", " Yaş:"))
        self.label_profile_weight.setText(_translate("MainWindow_profile", " Kilo:"))
        self.label_profile_boy.setText(_translate("MainWindow_profile", " Boy:"))
        self.label_profile_cinsiyet.setText(_translate("MainWindow_profile", " Cinsiyet:"))
        self.pushButton_profile_add.setText(_translate("MainWindow_profile", "Ekle"))

import icons_rc
