# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/eyuph/Desktop/Python/Proje/guncelle.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import icons_rc
class Ui_Guncelle(object):
    def setupUi(self, Guncelle):
        Guncelle.setObjectName("Guncelle")
        Guncelle.resize(400, 300)
        Guncelle.setMinimumSize(QtCore.QSize(400, 300))
        Guncelle.setMaximumSize(QtCore.QSize(400, 300))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/icon_profile.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Guncelle.setWindowIcon(icon)
        self.formLayoutWidget_2 = QtWidgets.QWidget(Guncelle)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(30, 30, 301, 181))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_guncelle_name = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_guncelle_name.setMinimumSize(QtCore.QSize(50, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_guncelle_name.setFont(font)
        self.label_guncelle_name.setObjectName("label_guncelle_name")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_guncelle_name)
        self.label_guncelle_age = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_guncelle_age.setMinimumSize(QtCore.QSize(50, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_guncelle_age.setFont(font)
        self.label_guncelle_age.setObjectName("label_guncelle_age")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_guncelle_age)
        self.lineEdit_guncelle_age = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_guncelle_age.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_guncelle_age.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.lineEdit_guncelle_age.setObjectName("lineEdit_guncelle_age")

        self.lineEdit_guncelle_age.setValidator(QtGui.QIntValidator())  # düzenlendi
        self.lineEdit_guncelle_age.setMaxLength(3)  # düzenlendi

        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_guncelle_age)
        self.label_guncelle_weight = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_guncelle_weight.setMinimumSize(QtCore.QSize(50, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_guncelle_weight.setFont(font)
        self.label_guncelle_weight.setObjectName("label_guncelle_weight")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_guncelle_weight)
        self.lineEdit_guncelle_weight = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_guncelle_weight.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_guncelle_weight.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhPreferNumbers)
        self.lineEdit_guncelle_weight.setObjectName("lineEdit_guncelle_weight")

        reg_ex = QtCore.QRegExp("[0-9][0-9][0-9]?[.][0-9][0-9]")
        input_validator = QtGui.QRegExpValidator(reg_ex, self.lineEdit_guncelle_weight)  # değiştirildi
        self.lineEdit_guncelle_weight.setValidator(input_validator)

        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_guncelle_weight)
        self.lineEdit_guncelle_name = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_guncelle_name.setEnabled(False)
        self.lineEdit_guncelle_name.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_guncelle_name.setInputMethodHints(QtCore.Qt.ImhLatinOnly)
        self.lineEdit_guncelle_name.setReadOnly(True)
        self.lineEdit_guncelle_name.setObjectName("lineEdit_guncelle_name")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_guncelle_name)
        self.label_guncelle_boy = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_guncelle_boy.setFont(font)
        self.label_guncelle_boy.setObjectName("label_guncelle_boy")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_guncelle_boy)
        self.lineEdit_guncelle_boy = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_guncelle_boy.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhPreferNumbers)
        self.lineEdit_guncelle_boy.setObjectName("lineEdit_guncelle_boy")

        reg_ex = QtCore.QRegExp("[0-2][.][0-9][0-9]")
        input_validator = QtGui.QRegExpValidator(reg_ex, self.lineEdit_guncelle_boy)  # değiştirildi
        self.lineEdit_guncelle_boy.setMaxLength(4)
        self.lineEdit_guncelle_boy.setValidator(input_validator)

        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_guncelle_boy)
        self.label_guncelle_cinsiyet = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_guncelle_cinsiyet.setFont(font)
        self.label_guncelle_cinsiyet.setObjectName("label_guncelle_cinsiyet")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_guncelle_cinsiyet)
        self.comboBox_guncelle_cinsiyet = QtWidgets.QComboBox(self.formLayoutWidget_2)
        self.comboBox_guncelle_cinsiyet.setEnabled(False)
        self.comboBox_guncelle_cinsiyet.setEditable(True)
        self.comboBox_guncelle_cinsiyet.setObjectName("comboBox_guncelle_cinsiyet")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.comboBox_guncelle_cinsiyet)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Guncelle)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 219, 381, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_guncelle = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_guncelle.setMinimumSize(QtCore.QSize(150, 40))
        self.pushButton_guncelle.setMaximumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_guncelle.setFont(font)
        self.pushButton_guncelle.setObjectName("pushButton_guncelle")
        self.horizontalLayout.addWidget(self.pushButton_guncelle)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)

        self.retranslateUi(Guncelle)
        QtCore.QMetaObject.connectSlotsByName(Guncelle)

    def retranslateUi(self, Guncelle):
        _translate = QtCore.QCoreApplication.translate
        Guncelle.setWindowTitle(_translate("Guncelle", "Güncelle"))
        self.label_guncelle_name.setText(_translate("Guncelle", " İsim:"))
        self.label_guncelle_age.setText(_translate("Guncelle", " Yaş:"))
        self.label_guncelle_weight.setText(_translate("Guncelle", " Kilo:"))
        self.label_guncelle_boy.setText(_translate("Guncelle", " Boy:"))
        self.label_guncelle_cinsiyet.setText(_translate("Guncelle", " Cinsiyet:"))
        self.pushButton_guncelle.setText(_translate("Guncelle", "Güncelle"))


