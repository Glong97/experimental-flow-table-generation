# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'hearthwiremotor.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_HearthWireMotor(object):
    def setupUi(self, HearthWireMotor):
        if not HearthWireMotor.objectName():
            HearthWireMotor.setObjectName(u"HearthWireMotor")
        HearthWireMotor.resize(893, 868)
        self.label = QLabel(HearthWireMotor)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(360, 20, 104, 16))
        self.groupBox = QGroupBox(HearthWireMotor)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 103, 875, 111))
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(560, 10, 81, 16))
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(730, 10, 51, 16))
        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 40, 121, 16))
        self.directionComboBox_1 = QComboBox(self.groupBox)
        self.directionComboBox_1.addItem("")
        self.directionComboBox_1.addItem("")
        self.directionComboBox_1.setObjectName(u"directionComboBox_1")
        self.directionComboBox_1.setGeometry(QRect(142, 40, 101, 22))
        self.subdivisionComboBox_1 = QComboBox(self.groupBox)
        self.subdivisionComboBox_1.addItem("")
        self.subdivisionComboBox_1.addItem("")
        self.subdivisionComboBox_1.addItem("")
        self.subdivisionComboBox_1.addItem("")
        self.subdivisionComboBox_1.setObjectName(u"subdivisionComboBox_1")
        self.subdivisionComboBox_1.setGeometry(QRect(282, 40, 131, 22))
        self.hexOmitLineEdit_2 = QLineEdit(self.groupBox)
        self.hexOmitLineEdit_2.setObjectName(u"hexOmitLineEdit_2")
        self.hexOmitLineEdit_2.setGeometry(QRect(520, 40, 141, 21))
        self.hexOmitLineEdit_2.setReadOnly(True)
        self.hexLineEdit_2 = QLineEdit(self.groupBox)
        self.hexLineEdit_2.setObjectName(u"hexLineEdit_2")
        self.hexLineEdit_2.setGeometry(QRect(680, 40, 151, 21))
        self.hexLineEdit_2.setReadOnly(True)
        self.velocityLineEdit_1 = QLineEdit(self.groupBox)
        self.velocityLineEdit_1.setObjectName(u"velocityLineEdit_1")
        self.velocityLineEdit_1.setGeometry(QRect(80, 80, 81, 21))
        self.label_32 = QLabel(self.groupBox)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(10, 80, 51, 16))
        self.hexOmitLineEdit_3 = QLineEdit(self.groupBox)
        self.hexOmitLineEdit_3.setObjectName(u"hexOmitLineEdit_3")
        self.hexOmitLineEdit_3.setGeometry(QRect(520, 80, 141, 21))
        self.hexOmitLineEdit_3.setReadOnly(True)
        self.hexLineEdit_3 = QLineEdit(self.groupBox)
        self.hexLineEdit_3.setObjectName(u"hexLineEdit_3")
        self.hexLineEdit_3.setGeometry(QRect(680, 80, 151, 21))
        self.hexLineEdit_3.setReadOnly(True)
        self.label_33 = QLabel(self.groupBox)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(170, 80, 51, 16))
        self.typeComboBox_1 = QComboBox(self.groupBox)
        self.typeComboBox_1.addItem("")
        self.typeComboBox_1.addItem("")
        self.typeComboBox_1.setObjectName(u"typeComboBox_1")
        self.typeComboBox_1.setGeometry(QRect(230, 80, 81, 22))
        self.label_34 = QLabel(self.groupBox)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setGeometry(QRect(330, 80, 31, 16))
        self.unitComboBox_1 = QComboBox(self.groupBox)
        self.unitComboBox_1.addItem("")
        self.unitComboBox_1.addItem("")
        self.unitComboBox_1.addItem("")
        self.unitComboBox_1.setObjectName(u"unitComboBox_1")
        self.unitComboBox_1.setGeometry(QRect(370, 80, 81, 22))
        self.groupBox_2 = QGroupBox(HearthWireMotor)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 210, 875, 110))
        self.hexOmitLineEdit_4 = QLineEdit(self.groupBox_2)
        self.hexOmitLineEdit_4.setObjectName(u"hexOmitLineEdit_4")
        self.hexOmitLineEdit_4.setGeometry(QRect(520, 40, 141, 21))
        self.hexOmitLineEdit_4.setReadOnly(True)
        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(720, 10, 51, 16))
        self.hexLineEdit_4 = QLineEdit(self.groupBox_2)
        self.hexLineEdit_4.setObjectName(u"hexLineEdit_4")
        self.hexLineEdit_4.setGeometry(QRect(680, 40, 151, 21))
        self.hexLineEdit_4.setReadOnly(True)
        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(550, 10, 81, 16))
        self.label_9 = QLabel(self.groupBox_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 40, 131, 16))
        self.directionComboBox_2 = QComboBox(self.groupBox_2)
        self.directionComboBox_2.addItem("")
        self.directionComboBox_2.addItem("")
        self.directionComboBox_2.setObjectName(u"directionComboBox_2")
        self.directionComboBox_2.setGeometry(QRect(150, 40, 101, 22))
        self.subdivisionComboBox_2 = QComboBox(self.groupBox_2)
        self.subdivisionComboBox_2.addItem("")
        self.subdivisionComboBox_2.addItem("")
        self.subdivisionComboBox_2.addItem("")
        self.subdivisionComboBox_2.addItem("")
        self.subdivisionComboBox_2.setObjectName(u"subdivisionComboBox_2")
        self.subdivisionComboBox_2.setGeometry(QRect(290, 40, 131, 22))
        self.hexOmitLineEdit_5 = QLineEdit(self.groupBox_2)
        self.hexOmitLineEdit_5.setObjectName(u"hexOmitLineEdit_5")
        self.hexOmitLineEdit_5.setGeometry(QRect(520, 80, 141, 21))
        self.hexOmitLineEdit_5.setReadOnly(True)
        self.hexLineEdit_5 = QLineEdit(self.groupBox_2)
        self.hexLineEdit_5.setObjectName(u"hexLineEdit_5")
        self.hexLineEdit_5.setGeometry(QRect(680, 80, 151, 21))
        self.hexLineEdit_5.setReadOnly(True)
        self.unitComboBox_2 = QComboBox(self.groupBox_2)
        self.unitComboBox_2.addItem("")
        self.unitComboBox_2.addItem("")
        self.unitComboBox_2.addItem("")
        self.unitComboBox_2.setObjectName(u"unitComboBox_2")
        self.unitComboBox_2.setGeometry(QRect(370, 80, 81, 22))
        self.label_40 = QLabel(self.groupBox_2)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setGeometry(QRect(330, 80, 31, 16))
        self.velocityLineEdit_2 = QLineEdit(self.groupBox_2)
        self.velocityLineEdit_2.setObjectName(u"velocityLineEdit_2")
        self.velocityLineEdit_2.setGeometry(QRect(80, 80, 81, 21))
        self.label_41 = QLabel(self.groupBox_2)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setGeometry(QRect(170, 80, 51, 16))
        self.label_42 = QLabel(self.groupBox_2)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setGeometry(QRect(10, 80, 51, 16))
        self.typeComboBox_2 = QComboBox(self.groupBox_2)
        self.typeComboBox_2.addItem("")
        self.typeComboBox_2.addItem("")
        self.typeComboBox_2.setObjectName(u"typeComboBox_2")
        self.typeComboBox_2.setGeometry(QRect(230, 80, 81, 22))
        self.groupBox_3 = QGroupBox(HearthWireMotor)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(10, 336, 875, 111))
        self.hexOmitLineEdit_6 = QLineEdit(self.groupBox_3)
        self.hexOmitLineEdit_6.setObjectName(u"hexOmitLineEdit_6")
        self.hexOmitLineEdit_6.setGeometry(QRect(520, 40, 141, 21))
        self.hexOmitLineEdit_6.setReadOnly(True)
        self.label_11 = QLabel(self.groupBox_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(720, 10, 51, 16))
        self.hexLineEdit_6 = QLineEdit(self.groupBox_3)
        self.hexLineEdit_6.setObjectName(u"hexLineEdit_6")
        self.hexLineEdit_6.setGeometry(QRect(680, 40, 151, 21))
        self.hexLineEdit_6.setReadOnly(True)
        self.label_12 = QLabel(self.groupBox_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(550, 10, 81, 16))
        self.label_13 = QLabel(self.groupBox_3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(10, 40, 131, 20))
        self.directionComboBox_3 = QComboBox(self.groupBox_3)
        self.directionComboBox_3.addItem("")
        self.directionComboBox_3.addItem("")
        self.directionComboBox_3.setObjectName(u"directionComboBox_3")
        self.directionComboBox_3.setGeometry(QRect(150, 40, 101, 22))
        self.subdivisionComboBox_3 = QComboBox(self.groupBox_3)
        self.subdivisionComboBox_3.addItem("")
        self.subdivisionComboBox_3.addItem("")
        self.subdivisionComboBox_3.addItem("")
        self.subdivisionComboBox_3.addItem("")
        self.subdivisionComboBox_3.setObjectName(u"subdivisionComboBox_3")
        self.subdivisionComboBox_3.setGeometry(QRect(290, 40, 131, 22))
        self.hexOmitLineEdit_7 = QLineEdit(self.groupBox_3)
        self.hexOmitLineEdit_7.setObjectName(u"hexOmitLineEdit_7")
        self.hexOmitLineEdit_7.setGeometry(QRect(520, 80, 141, 21))
        self.hexOmitLineEdit_7.setReadOnly(True)
        self.hexLineEdit_7 = QLineEdit(self.groupBox_3)
        self.hexLineEdit_7.setObjectName(u"hexLineEdit_7")
        self.hexLineEdit_7.setGeometry(QRect(680, 80, 151, 21))
        self.hexLineEdit_7.setReadOnly(True)
        self.unitComboBox_3 = QComboBox(self.groupBox_3)
        self.unitComboBox_3.addItem("")
        self.unitComboBox_3.addItem("")
        self.unitComboBox_3.addItem("")
        self.unitComboBox_3.setObjectName(u"unitComboBox_3")
        self.unitComboBox_3.setGeometry(QRect(370, 80, 81, 22))
        self.label_43 = QLabel(self.groupBox_3)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setGeometry(QRect(330, 80, 31, 16))
        self.velocityLineEdit_3 = QLineEdit(self.groupBox_3)
        self.velocityLineEdit_3.setObjectName(u"velocityLineEdit_3")
        self.velocityLineEdit_3.setGeometry(QRect(80, 80, 81, 21))
        self.label_44 = QLabel(self.groupBox_3)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setGeometry(QRect(170, 80, 51, 16))
        self.label_45 = QLabel(self.groupBox_3)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setGeometry(QRect(10, 80, 51, 16))
        self.typeComboBox_3 = QComboBox(self.groupBox_3)
        self.typeComboBox_3.addItem("")
        self.typeComboBox_3.addItem("")
        self.typeComboBox_3.setObjectName(u"typeComboBox_3")
        self.typeComboBox_3.setGeometry(QRect(230, 80, 81, 22))
        self.groupBox_4 = QGroupBox(HearthWireMotor)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(10, 454, 875, 110))
        self.hexOmitLineEdit_8 = QLineEdit(self.groupBox_4)
        self.hexOmitLineEdit_8.setObjectName(u"hexOmitLineEdit_8")
        self.hexOmitLineEdit_8.setGeometry(QRect(520, 40, 141, 21))
        self.hexOmitLineEdit_8.setReadOnly(True)
        self.label_15 = QLabel(self.groupBox_4)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(720, 10, 51, 16))
        self.hexLineEdit_8 = QLineEdit(self.groupBox_4)
        self.hexLineEdit_8.setObjectName(u"hexLineEdit_8")
        self.hexLineEdit_8.setGeometry(QRect(680, 40, 151, 21))
        self.hexLineEdit_8.setReadOnly(True)
        self.label_16 = QLabel(self.groupBox_4)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(550, 10, 81, 16))
        self.label_17 = QLabel(self.groupBox_4)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(10, 40, 131, 20))
        self.directionComboBox_4 = QComboBox(self.groupBox_4)
        self.directionComboBox_4.addItem("")
        self.directionComboBox_4.addItem("")
        self.directionComboBox_4.setObjectName(u"directionComboBox_4")
        self.directionComboBox_4.setGeometry(QRect(150, 40, 101, 22))
        self.subdivisionComboBox_4 = QComboBox(self.groupBox_4)
        self.subdivisionComboBox_4.addItem("")
        self.subdivisionComboBox_4.addItem("")
        self.subdivisionComboBox_4.addItem("")
        self.subdivisionComboBox_4.addItem("")
        self.subdivisionComboBox_4.setObjectName(u"subdivisionComboBox_4")
        self.subdivisionComboBox_4.setGeometry(QRect(290, 40, 131, 22))
        self.hexOmitLineEdit_9 = QLineEdit(self.groupBox_4)
        self.hexOmitLineEdit_9.setObjectName(u"hexOmitLineEdit_9")
        self.hexOmitLineEdit_9.setGeometry(QRect(520, 80, 141, 21))
        self.hexOmitLineEdit_9.setReadOnly(True)
        self.hexLineEdit_9 = QLineEdit(self.groupBox_4)
        self.hexLineEdit_9.setObjectName(u"hexLineEdit_9")
        self.hexLineEdit_9.setGeometry(QRect(680, 80, 151, 21))
        self.hexLineEdit_9.setReadOnly(True)
        self.unitComboBox_4 = QComboBox(self.groupBox_4)
        self.unitComboBox_4.addItem("")
        self.unitComboBox_4.addItem("")
        self.unitComboBox_4.addItem("")
        self.unitComboBox_4.setObjectName(u"unitComboBox_4")
        self.unitComboBox_4.setGeometry(QRect(370, 80, 81, 22))
        self.label_46 = QLabel(self.groupBox_4)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setGeometry(QRect(330, 80, 31, 16))
        self.velocityLineEdit_4 = QLineEdit(self.groupBox_4)
        self.velocityLineEdit_4.setObjectName(u"velocityLineEdit_4")
        self.velocityLineEdit_4.setGeometry(QRect(80, 80, 81, 21))
        self.label_47 = QLabel(self.groupBox_4)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setGeometry(QRect(170, 80, 51, 16))
        self.label_48 = QLabel(self.groupBox_4)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setGeometry(QRect(10, 80, 51, 16))
        self.typeComboBox_4 = QComboBox(self.groupBox_4)
        self.typeComboBox_4.addItem("")
        self.typeComboBox_4.addItem("")
        self.typeComboBox_4.setObjectName(u"typeComboBox_4")
        self.typeComboBox_4.setGeometry(QRect(230, 80, 81, 22))
        self.groupBox_5 = QGroupBox(HearthWireMotor)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(10, 570, 875, 111))
        self.hexOmitLineEdit_10 = QLineEdit(self.groupBox_5)
        self.hexOmitLineEdit_10.setObjectName(u"hexOmitLineEdit_10")
        self.hexOmitLineEdit_10.setGeometry(QRect(520, 40, 141, 21))
        self.hexOmitLineEdit_10.setReadOnly(True)
        self.label_19 = QLabel(self.groupBox_5)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(720, 10, 51, 16))
        self.hexLineEdit_10 = QLineEdit(self.groupBox_5)
        self.hexLineEdit_10.setObjectName(u"hexLineEdit_10")
        self.hexLineEdit_10.setGeometry(QRect(680, 40, 151, 21))
        self.hexLineEdit_10.setReadOnly(True)
        self.label_20 = QLabel(self.groupBox_5)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(550, 10, 81, 16))
        self.label_21 = QLabel(self.groupBox_5)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(10, 40, 131, 20))
        self.directionComboBox_5 = QComboBox(self.groupBox_5)
        self.directionComboBox_5.addItem("")
        self.directionComboBox_5.addItem("")
        self.directionComboBox_5.setObjectName(u"directionComboBox_5")
        self.directionComboBox_5.setGeometry(QRect(150, 40, 101, 22))
        self.subdivisionComboBox_5 = QComboBox(self.groupBox_5)
        self.subdivisionComboBox_5.addItem("")
        self.subdivisionComboBox_5.addItem("")
        self.subdivisionComboBox_5.addItem("")
        self.subdivisionComboBox_5.addItem("")
        self.subdivisionComboBox_5.setObjectName(u"subdivisionComboBox_5")
        self.subdivisionComboBox_5.setGeometry(QRect(290, 40, 131, 22))
        self.hexOmitLineEdit_11 = QLineEdit(self.groupBox_5)
        self.hexOmitLineEdit_11.setObjectName(u"hexOmitLineEdit_11")
        self.hexOmitLineEdit_11.setGeometry(QRect(520, 80, 141, 21))
        self.hexOmitLineEdit_11.setReadOnly(True)
        self.hexLineEdit_11 = QLineEdit(self.groupBox_5)
        self.hexLineEdit_11.setObjectName(u"hexLineEdit_11")
        self.hexLineEdit_11.setGeometry(QRect(680, 80, 151, 21))
        self.hexLineEdit_11.setReadOnly(True)
        self.unitComboBox_5 = QComboBox(self.groupBox_5)
        self.unitComboBox_5.addItem("")
        self.unitComboBox_5.addItem("")
        self.unitComboBox_5.addItem("")
        self.unitComboBox_5.setObjectName(u"unitComboBox_5")
        self.unitComboBox_5.setGeometry(QRect(370, 80, 81, 22))
        self.label_49 = QLabel(self.groupBox_5)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setGeometry(QRect(330, 80, 31, 16))
        self.velocityLineEdit_5 = QLineEdit(self.groupBox_5)
        self.velocityLineEdit_5.setObjectName(u"velocityLineEdit_5")
        self.velocityLineEdit_5.setGeometry(QRect(80, 80, 81, 21))
        self.label_50 = QLabel(self.groupBox_5)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setGeometry(QRect(170, 80, 51, 16))
        self.label_51 = QLabel(self.groupBox_5)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setGeometry(QRect(10, 80, 51, 16))
        self.typeComboBox_5 = QComboBox(self.groupBox_5)
        self.typeComboBox_5.addItem("")
        self.typeComboBox_5.addItem("")
        self.typeComboBox_5.setObjectName(u"typeComboBox_5")
        self.typeComboBox_5.setGeometry(QRect(230, 80, 81, 22))
        self.groupBox_6 = QGroupBox(HearthWireMotor)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setGeometry(QRect(10, 687, 875, 81))
        self.label_24 = QLabel(self.groupBox_6)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(720, 10, 51, 16))
        self.hexLineEdit_12 = QLineEdit(self.groupBox_6)
        self.hexLineEdit_12.setObjectName(u"hexLineEdit_12")
        self.hexLineEdit_12.setGeometry(QRect(680, 40, 151, 21))
        self.hexLineEdit_12.setReadOnly(True)
        self.label_25 = QLabel(self.groupBox_6)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(550, 10, 81, 16))
        self.hexOmitLineEdit_12 = QLineEdit(self.groupBox_6)
        self.hexOmitLineEdit_12.setObjectName(u"hexOmitLineEdit_12")
        self.hexOmitLineEdit_12.setGeometry(QRect(520, 40, 141, 21))
        self.hexOmitLineEdit_12.setReadOnly(True)
        self.label_23 = QLabel(self.groupBox_6)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(10, 40, 131, 16))
        self.enableCheckBox_2 = QCheckBox(self.groupBox_6)
        self.enableCheckBox_2.setObjectName(u"enableCheckBox_2")
        self.enableCheckBox_2.setGeometry(QRect(210, 40, 61, 20))
        self.enableCheckBox_4 = QCheckBox(self.groupBox_6)
        self.enableCheckBox_4.setObjectName(u"enableCheckBox_4")
        self.enableCheckBox_4.setGeometry(QRect(370, 40, 61, 20))
        self.enableCheckBox_5 = QCheckBox(self.groupBox_6)
        self.enableCheckBox_5.setObjectName(u"enableCheckBox_5")
        self.enableCheckBox_5.setGeometry(QRect(450, 40, 61, 20))
        self.enableCheckBox_1 = QCheckBox(self.groupBox_6)
        self.enableCheckBox_1.setObjectName(u"enableCheckBox_1")
        self.enableCheckBox_1.setGeometry(QRect(140, 40, 61, 20))
        self.groupBox_7 = QGroupBox(self.groupBox_6)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setGeometry(QRect(20, 730, 851, 81))
        self.label_26 = QLabel(self.groupBox_7)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(720, 10, 51, 16))
        self.label_27 = QLabel(self.groupBox_7)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(550, 10, 81, 16))
        self.label_28 = QLabel(self.groupBox_7)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(10, 40, 131, 16))
        self.enableCheckBox_3 = QCheckBox(self.groupBox_6)
        self.enableCheckBox_3.setObjectName(u"enableCheckBox_3")
        self.enableCheckBox_3.setGeometry(QRect(290, 40, 61, 20))
        self.commitPushButton = QPushButton(HearthWireMotor)
        self.commitPushButton.setObjectName(u"commitPushButton")
        self.commitPushButton.setGeometry(QRect(630, 820, 75, 24))
        self.cancelPushButton = QPushButton(HearthWireMotor)
        self.cancelPushButton.setObjectName(u"cancelPushButton")
        self.cancelPushButton.setGeometry(QRect(740, 820, 75, 24))
        self.layoutWidget = QWidget(HearthWireMotor)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 780, 259, 26))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_29 = QLabel(self.layoutWidget)
        self.label_29.setObjectName(u"label_29")

        self.horizontalLayout.addWidget(self.label_29)

        self.actionIDLineEdit = QLineEdit(self.layoutWidget)
        self.actionIDLineEdit.setObjectName(u"actionIDLineEdit")
        self.actionIDLineEdit.setReadOnly(True)

        self.horizontalLayout.addWidget(self.actionIDLineEdit)

        self.generateIDPushButton = QPushButton(self.layoutWidget)
        self.generateIDPushButton.setObjectName(u"generateIDPushButton")

        self.horizontalLayout.addWidget(self.generateIDPushButton)

        self.confCheckBox_5 = QCheckBox(HearthWireMotor)
        self.confCheckBox_5.setObjectName(u"confCheckBox_5")
        self.confCheckBox_5.setGeometry(QRect(440, 70, 61, 20))
        self.hexLineEdit_1 = QLineEdit(HearthWireMotor)
        self.hexLineEdit_1.setObjectName(u"hexLineEdit_1")
        self.hexLineEdit_1.setGeometry(QRect(690, 70, 151, 21))
        self.hexLineEdit_1.setReadOnly(True)
        self.label_2 = QLabel(HearthWireMotor)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 70, 81, 21))
        self.confCheckBox_1 = QCheckBox(HearthWireMotor)
        self.confCheckBox_1.setObjectName(u"confCheckBox_1")
        self.confCheckBox_1.setGeometry(QRect(129, 70, 61, 20))
        self.hexOmitLineEdit_1 = QLineEdit(HearthWireMotor)
        self.hexOmitLineEdit_1.setObjectName(u"hexOmitLineEdit_1")
        self.hexOmitLineEdit_1.setGeometry(QRect(530, 70, 141, 21))
        self.hexOmitLineEdit_1.setReadOnly(True)
        self.confCheckBox_2 = QCheckBox(HearthWireMotor)
        self.confCheckBox_2.setObjectName(u"confCheckBox_2")
        self.confCheckBox_2.setGeometry(QRect(200, 70, 61, 20))
        self.confCheckBox_3 = QCheckBox(HearthWireMotor)
        self.confCheckBox_3.setObjectName(u"confCheckBox_3")
        self.confCheckBox_3.setGeometry(QRect(280, 70, 61, 20))
        self.confCheckBox_4 = QCheckBox(HearthWireMotor)
        self.confCheckBox_4.setObjectName(u"confCheckBox_4")
        self.confCheckBox_4.setGeometry(QRect(360, 70, 61, 20))
        self.label_30 = QLabel(HearthWireMotor)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(560, 40, 81, 16))
        self.label_31 = QLabel(HearthWireMotor)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(730, 40, 51, 16))

        self.retranslateUi(HearthWireMotor)

        self.unitComboBox_3.setCurrentIndex(2)
        self.unitComboBox_4.setCurrentIndex(2)
        self.unitComboBox_5.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(HearthWireMotor)
    # setupUi

    def retranslateUi(self, HearthWireMotor):
        HearthWireMotor.setWindowTitle(QCoreApplication.translate("HearthWireMotor", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("HearthWireMotor", u"1\u7089\u4e1d\u7535\u673a\u53c2\u6570\u8bbe\u7f6e", None))
        self.groupBox.setTitle(QCoreApplication.translate("HearthWireMotor", u"\u8f6c\u673a1\u53c2\u6570\u52a8\u4f5c", None))
        self.label_4.setText(QCoreApplication.translate("HearthWireMotor", u"\u5341\u516d\u8fdb\u5236\u7f29\u5199", None))
        self.label_5.setText(QCoreApplication.translate("HearthWireMotor", u"\u5341\u516d\u8fdb\u5236", None))
        self.label_6.setText(QCoreApplication.translate("HearthWireMotor", u"\u8f6c\u673a1\u7ec6\u5206\u548c\u65b9\u5411\u8bbe\u7f6e", None))
        self.directionComboBox_1.setItemText(0, QCoreApplication.translate("HearthWireMotor", u"\u53ea\u6b63\u8f6c\u9006", None))
        self.directionComboBox_1.setItemText(1, QCoreApplication.translate("HearthWireMotor", u"\u53cd\u8f6c", None))

        self.subdivisionComboBox_1.setItemText(0, QCoreApplication.translate("HearthWireMotor", u"2\u76f84\u62cd", None))
        self.subdivisionComboBox_1.setItemText(1, QCoreApplication.translate("HearthWireMotor", u"2\u7ec6\u5206", None))
        self.subdivisionComboBox_1.setItemText(2, QCoreApplication.translate("HearthWireMotor", u"4\u7ec6\u5206", None))
        self.subdivisionComboBox_1.setItemText(3, QCoreApplication.translate("HearthWireMotor", u"8\u7ec6\u5206", None))

        self.hexLineEdit_2.setText("")
        self.velocityLineEdit_1.setText(QCoreApplication.translate("HearthWireMotor", u"3", None))
        self.label_32.setText(QCoreApplication.translate("HearthWireMotor", u"\u8fd0\u884c\u901f\u5ea6", None))
        self.hexOmitLineEdit_3.setText("")
        self.hexLineEdit_3.setText("")
        self.label_33.setText(QCoreApplication.translate("HearthWireMotor", u"\u8fd0\u52a8\u7c7b\u522b", None))
        self.typeComboBox_1.setItemText(0, QCoreApplication.translate("HearthWireMotor", u"\u76f4\u7ebf\u8fd0\u52a8", None))
        self.typeComboBox_1.setItemText(1, QCoreApplication.translate("HearthWireMotor", u"\u5706\u5468\u8fd0\u52a8", None))

        self.label_34.setText(QCoreApplication.translate("HearthWireMotor", u"\u5355\u4f4d", None))
        self.unitComboBox_1.setItemText(0, QCoreApplication.translate("HearthWireMotor", u"mm/s", None))
        self.unitComboBox_1.setItemText(1, QCoreApplication.translate("HearthWireMotor", u"mm/min", None))
        self.unitComboBox_1.setItemText(2, QCoreApplication.translate("HearthWireMotor", u"mm/H", None))

        self.groupBox_2.setTitle(QCoreApplication.translate("HearthWireMotor", u"\u6837\u63d0\u673a2\u53c2\u6570\u52a8\u4f5c", None))
        self.label_7.setText(QCoreApplication.translate("HearthWireMotor", u"\u5341\u516d\u8fdb\u5236", None))
        self.hexLineEdit_4.setText("")
        self.label_8.setText(QCoreApplication.translate("HearthWireMotor", u"\u5341\u516d\u8fdb\u5236\u7f29\u5199", None))
        self.label_9.setText(QCoreApplication.translate("HearthWireMotor", u"\u6837\u63d0\u673a2\u7ec6\u5206\u548c\u65b9\u5411\u8bbe\u7f6e", None))
        self.directionComboBox_2.setItemText(0, QCoreApplication.translate("HearthWireMotor", u"\u6b63\u8f6c\u4e0b", None))
        self.directionComboBox_2.setItemText(1, QCoreApplication.translate("HearthWireMotor", u"\u53cd\u8f6c\u4e0a", None))

        self.subdivisionComboBox_2.setItemText(0, QCoreApplication.translate("HearthWireMotor", u"2\u76f84\u62cd", None))
        self.subdivisionComboBox_2.setItemText(1, QCoreApplication.translate("HearthWireMotor", u"2\u7ec6\u5206", None))
        self.subdivisionComboBox_2.setItemText(2, QCoreApplication.translate("HearthWireMotor", u"4\u7ec6\u5206", None))
        self.subdivisionComboBox_2.setItemText(3, QCoreApplication.translate("HearthWireMotor", u"8\u7ec6\u5206", None))

        self.hexOmitLineEdit_5.setText("")
        self.hexLineEdit_5.setText("")
        self.unitComboBox_2.setItemText(0, QCoreApplication.translate("HearthWireMotor", u"mm/s", None))
        self.unitComboBox_2.setItemText(1, QCoreApplication.translate("HearthWireMotor", u"mm/min", None))
        self.unitComboBox_2.setItemText(2, QCoreApplication.translate("HearthWireMotor", u"mm/H", None))

        self.label_40.setText(QCoreApplication.translate("HearthWireMotor", u"\u5355\u4f4d", None))
        self.velocityLineEdit_2.setText(QCoreApplication.translate("HearthWireMotor", u"3", None))
        self.label_41.setText(QCoreApplication.translate("HearthWireMotor", u"\u8fd0\u52a8\u7c7b\u522b", None))
        self.label_42.setText(QCoreApplication.translate("HearthWireMotor", u"\u8fd0\u884c\u901f\u5ea6", None))
        self.typeComboBox_2.setItemText(0, QCoreApplication.translate("HearthWireMotor", u"\u76f4\u7ebf\u8fd0\u52a8", None))
        self.typeComboBox_2.setItemText(1, QCoreApplication.translate("HearthWireMotor", u"\u5706\u5468\u8fd0\u52a8", None))

        self.groupBox_3.setTitle(QCoreApplication.translate("HearthWireMotor", u"\u7089\u4e0a\u673a3\u53c2\u6570\u52a8\u4f5c", None))
        self.label_11.setText(QCoreApplication.translate("HearthWireMotor", u"\u5341\u516d\u8fdb\u5236", None))
        self.hexLineEdit_6.setText("")
        self.label_12.setText(QCoreApplication.translate("HearthWireMotor", u"\u5341\u516d\u8fdb\u5236\u7f29\u5199", None))
        self.label_13.setText(QCoreApplication.translate("HearthWireMotor", u"\u7089\u4e0a\u673a3\u7ec6\u5206\u548c\u65b9\u5411\u8bbe\u7f6e", None))
        self.directionComboBox_3.setItemText(0, QCoreApplication.translate("HearthWireMotor", u"\u6b63\u8f6c\u4e0a", None))
        self.directionComboBox_3.setItemText(1, QCoreApplication.translate("HearthWireMotor", u"\u53cd\u8f6c\u4e0b", None))

        self.subdivisionComboBox_3.setItemText(0, QCoreApplication.translate("HearthWireMotor", u"2\u76f84\u62cd", None))
        self.subdivisionComboBox_3.setItemText(1, QCoreApplication.translate("HearthWireMotor", u"2\u7ec6\u5206", None))
        self.subdivisionComboBox_3.setItemText(2, QCoreApplication.translate("HearthWireMotor", u"4\u7ec6\u5206", None))
        self.subdivisionComboBox_3.setItemText(3, QCoreApplication.translate("HearthWireMotor", u"8\u7ec6\u5206", None))

        self.hexOmitLineEdit_7.setText("")
        self.hexLineEdit_7.setText("")
        self.unitComboBox_3.setItemText(0, QCoreApplication.translate("HearthWireMotor", u"mm/s", None))
        self.unitComboBox_3.setItemText(1, QCoreApplication.translate("HearthWireMotor", u"mm/min", None))
        self.unitComboBox_3.setItemText(2, QCoreApplication.translate("HearthWireMotor", u"mm/H", None))

        self.label_43.setText(QCoreApplication.translate("HearthWireMotor", u"\u5355\u4f4d", None))
        self.velocityLineEdit_3.setText(QCoreApplication.translate("HearthWireMotor", u"50", None))
        self.label_44.setText(QCoreApplication.translate("HearthWireMotor", u"\u8fd0\u52a8\u7c7b\u522b", None))
        self.label_45.setText(QCoreApplication.translate("HearthWireMotor", u"\u8fd0\u884c\u901f\u5ea6", None))
        self.typeComboBox_3.setItemText(0, QCoreApplication.translate("HearthWireMotor", u"\u76f4\u7ebf\u8fd0\u52a8", None))
        self.typeComboBox_3.setItemText(1, QCoreApplication.translate("HearthWireMotor", u"\u5706\u5468\u8fd0\u52a8", None))

        self.groupBox_4.setTitle(QCoreApplication.translate("HearthWireMotor", u"\u7089\u4e2d\u673a4\u53c2\u6570\u52a8\u4f5c", None))
        self.label_15.setText(QCoreApplication.translate("HearthWireMotor", u"\u5341\u516d\u8fdb\u5236", None))
        self.hexLineEdit_8.setText("")
        self.label_16.setText(QCoreApplication.translate("HearthWireMotor", u"\u5341\u516d\u8fdb\u5236\u7f29\u5199", None))
        self.label_17.setText(QCoreApplication.translate("HearthWireMotor", u"\u7089\u4e2d\u673a4\u7ec6\u5206\u548c\u65b9\u5411\u8bbe\u7f6e", None))
        self.directionComboBox_4.setItemText(0, QCoreApplication.translate("HearthWireMotor", u"\u6b63\u8f6c\u4e0a", None))
        self.directionComboBox_4.setItemText(1, QCoreApplication.translate("HearthWireMotor", u"\u53cd\u8f6c\u4e0b", None))

        self.subdivisionComboBox_4.setItemText(0, QCoreApplication.translate("HearthWireMotor", u"2\u76f84\u62cd", None))
        self.subdivisionComboBox_4.setItemText(1, QCoreApplication.translate("HearthWireMotor", u"2\u7ec6\u5206", None))
        self.subdivisionComboBox_4.setItemText(2, QCoreApplication.translate("HearthWireMotor", u"4\u7ec6\u5206", None))
        self.subdivisionComboBox_4.setItemText(3, QCoreApplication.translate("HearthWireMotor", u"8\u7ec6\u5206", None))

        self.hexOmitLineEdit_9.setText("")
        self.hexLineEdit_9.setText("")
        self.unitComboBox_4.setItemText(0, QCoreApplication.translate("HearthWireMotor", u"mm/s", None))
        self.unitComboBox_4.setItemText(1, QCoreApplication.translate("HearthWireMotor", u"mm/min", None))
        self.unitComboBox_4.setItemText(2, QCoreApplication.translate("HearthWireMotor", u"mm/H", None))

        self.label_46.setText(QCoreApplication.translate("HearthWireMotor", u"\u5355\u4f4d", None))
        self.velocityLineEdit_4.setText(QCoreApplication.translate("HearthWireMotor", u"50", None))
        self.label_47.setText(QCoreApplication.translate("HearthWireMotor", u"\u8fd0\u52a8\u7c7b\u522b", None))
        self.label_48.setText(QCoreApplication.translate("HearthWireMotor", u"\u8fd0\u884c\u901f\u5ea6", None))
        self.typeComboBox_4.setItemText(0, QCoreApplication.translate("HearthWireMotor", u"\u76f4\u7ebf\u8fd0\u52a8", None))
        self.typeComboBox_4.setItemText(1, QCoreApplication.translate("HearthWireMotor", u"\u5706\u5468\u8fd0\u52a8", None))

        self.groupBox_5.setTitle(QCoreApplication.translate("HearthWireMotor", u"\u7089\u4e0b\u673a5\u53c2\u6570\u52a8\u4f5c", None))
        self.label_19.setText(QCoreApplication.translate("HearthWireMotor", u"\u5341\u516d\u8fdb\u5236", None))
        self.hexLineEdit_10.setText("")
        self.label_20.setText(QCoreApplication.translate("HearthWireMotor", u"\u5341\u516d\u8fdb\u5236\u7f29\u5199", None))
        self.label_21.setText(QCoreApplication.translate("HearthWireMotor", u"\u7089\u4e0b\u673a5\u7ec6\u5206\u548c\u65b9\u5411\u8bbe\u7f6e", None))
        self.directionComboBox_5.setItemText(0, QCoreApplication.translate("HearthWireMotor", u"\u6b63\u8f6c\u4e0a", None))
        self.directionComboBox_5.setItemText(1, QCoreApplication.translate("HearthWireMotor", u"\u53cd\u8f6c\u4e0b", None))

        self.subdivisionComboBox_5.setItemText(0, QCoreApplication.translate("HearthWireMotor", u"2\u76f84\u62cd", None))
        self.subdivisionComboBox_5.setItemText(1, QCoreApplication.translate("HearthWireMotor", u"2\u7ec6\u5206", None))
        self.subdivisionComboBox_5.setItemText(2, QCoreApplication.translate("HearthWireMotor", u"4\u7ec6\u5206", None))
        self.subdivisionComboBox_5.setItemText(3, QCoreApplication.translate("HearthWireMotor", u"8\u7ec6\u5206", None))

        self.hexOmitLineEdit_11.setText("")
        self.hexLineEdit_11.setText("")
        self.unitComboBox_5.setItemText(0, QCoreApplication.translate("HearthWireMotor", u"mm/s", None))
        self.unitComboBox_5.setItemText(1, QCoreApplication.translate("HearthWireMotor", u"mm/min", None))
        self.unitComboBox_5.setItemText(2, QCoreApplication.translate("HearthWireMotor", u"mm/H", None))

        self.label_49.setText(QCoreApplication.translate("HearthWireMotor", u"\u5355\u4f4d", None))
        self.velocityLineEdit_5.setText(QCoreApplication.translate("HearthWireMotor", u"50", None))
        self.label_50.setText(QCoreApplication.translate("HearthWireMotor", u"\u8fd0\u52a8\u7c7b\u522b", None))
        self.label_51.setText(QCoreApplication.translate("HearthWireMotor", u"\u8fd0\u884c\u901f\u5ea6", None))
        self.typeComboBox_5.setItemText(0, QCoreApplication.translate("HearthWireMotor", u"\u76f4\u7ebf\u8fd0\u52a8", None))
        self.typeComboBox_5.setItemText(1, QCoreApplication.translate("HearthWireMotor", u"\u5706\u5468\u8fd0\u52a8", None))

        self.groupBox_6.setTitle(QCoreApplication.translate("HearthWireMotor", u"\u7535\u673a\u5931\u6b65\u68c0\u6d4b\u4f7f\u80fd", None))
        self.label_24.setText(QCoreApplication.translate("HearthWireMotor", u"\u5341\u516d\u8fdb\u5236", None))
        self.hexLineEdit_12.setText("")
        self.label_25.setText(QCoreApplication.translate("HearthWireMotor", u"\u5341\u516d\u8fdb\u5236\u7f29\u5199", None))
        self.label_23.setText(QCoreApplication.translate("HearthWireMotor", u"\u7535\u673a\u5931\u6b65\u68c0\u6d4b\u4f7f\u80fd\u8bbe\u7f6e", None))
        self.enableCheckBox_2.setText(QCoreApplication.translate("HearthWireMotor", u"\u6837\u63d0\u673a2", None))
        self.enableCheckBox_4.setText(QCoreApplication.translate("HearthWireMotor", u"\u7089\u4e2d\u673a4", None))
        self.enableCheckBox_5.setText(QCoreApplication.translate("HearthWireMotor", u"\u7089\u4e0b\u673a5", None))
        self.enableCheckBox_1.setText(QCoreApplication.translate("HearthWireMotor", u"\u8f6c\u673a1", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("HearthWireMotor", u"\u7535\u673a\u5931\u6b65\u68c0\u6d4b\u4f7f\u80fd", None))
        self.label_26.setText(QCoreApplication.translate("HearthWireMotor", u"\u5341\u516d\u8fdb\u5236", None))
        self.label_27.setText(QCoreApplication.translate("HearthWireMotor", u"\u5341\u516d\u8fdb\u5236\u7f29\u5199", None))
        self.label_28.setText(QCoreApplication.translate("HearthWireMotor", u"\u7535\u673a\u5931\u6b65\u68c0\u6d4b\u4f7f\u80fd\u8bbe\u7f6e", None))
        self.enableCheckBox_3.setText(QCoreApplication.translate("HearthWireMotor", u"\u7089\u4e0a\u673a3", None))
        self.commitPushButton.setText(QCoreApplication.translate("HearthWireMotor", u"\u786e\u5b9a", None))
        self.cancelPushButton.setText(QCoreApplication.translate("HearthWireMotor", u"\u53d6\u6d88", None))
        self.label_29.setText(QCoreApplication.translate("HearthWireMotor", u"\u52a8\u4f5cID", None))
        self.generateIDPushButton.setText(QCoreApplication.translate("HearthWireMotor", u"\u751f\u6210\u52a8\u4f5cID", None))
        self.confCheckBox_5.setText(QCoreApplication.translate("HearthWireMotor", u"\u7089\u4e0b\u673a5", None))
        self.hexLineEdit_1.setText("")
        self.label_2.setText(QCoreApplication.translate("HearthWireMotor", u"\u7535\u673a\u53c2\u6570\u7247\u9009", None))
        self.confCheckBox_1.setText(QCoreApplication.translate("HearthWireMotor", u"\u8f6c\u673a1", None))
        self.confCheckBox_2.setText(QCoreApplication.translate("HearthWireMotor", u"\u6837\u63d0\u673a2", None))
        self.confCheckBox_3.setText(QCoreApplication.translate("HearthWireMotor", u"\u7089\u4e0a\u673a3", None))
        self.confCheckBox_4.setText(QCoreApplication.translate("HearthWireMotor", u"\u7089\u4e2d\u673a4", None))
        self.label_30.setText(QCoreApplication.translate("HearthWireMotor", u"\u5341\u516d\u8fdb\u5236\u7f29\u5199", None))
        self.label_31.setText(QCoreApplication.translate("HearthWireMotor", u"\u5341\u516d\u8fdb\u5236", None))
    # retranslateUi

