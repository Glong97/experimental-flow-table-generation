# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'furnacewireheating.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_FurnaceWireHeating(object):
    def setupUi(self, FurnaceWireHeating):
        if not FurnaceWireHeating.objectName():
            FurnaceWireHeating.setObjectName(u"FurnaceWireHeating")
        FurnaceWireHeating.resize(779, 364)
        self.label = QLabel(FurnaceWireHeating)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(310, 20, 131, 16))
        self.label_2 = QLabel(FurnaceWireHeating)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 70, 101, 16))
        self.checkBox_1 = QCheckBox(FurnaceWireHeating)
        self.checkBox_1.setObjectName(u"checkBox_1")
        self.checkBox_1.setGeometry(QRect(170, 70, 51, 20))
        self.checkBox_2 = QCheckBox(FurnaceWireHeating)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setGeometry(QRect(240, 70, 51, 20))
        self.checkBox_3 = QCheckBox(FurnaceWireHeating)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setGeometry(QRect(310, 70, 51, 20))
        self.checkBox_4 = QCheckBox(FurnaceWireHeating)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setGeometry(QRect(380, 70, 51, 20))
        self.label_3 = QLabel(FurnaceWireHeating)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(50, 110, 101, 16))
        self.valLineEdit_1 = QLineEdit(FurnaceWireHeating)
        self.valLineEdit_1.setObjectName(u"valLineEdit_1")
        self.valLineEdit_1.setGeometry(QRect(210, 110, 141, 21))
        self.valLineEdit_2 = QLineEdit(FurnaceWireHeating)
        self.valLineEdit_2.setObjectName(u"valLineEdit_2")
        self.valLineEdit_2.setGeometry(QRect(210, 150, 141, 21))
        self.label_4 = QLabel(FurnaceWireHeating)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(50, 150, 101, 16))
        self.valLineEdit_3 = QLineEdit(FurnaceWireHeating)
        self.valLineEdit_3.setObjectName(u"valLineEdit_3")
        self.valLineEdit_3.setGeometry(QRect(210, 190, 141, 21))
        self.label_5 = QLabel(FurnaceWireHeating)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(50, 190, 101, 16))
        self.valLineEdit_4 = QLineEdit(FurnaceWireHeating)
        self.valLineEdit_4.setObjectName(u"valLineEdit_4")
        self.valLineEdit_4.setGeometry(QRect(210, 230, 141, 21))
        self.label_6 = QLabel(FurnaceWireHeating)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(50, 230, 101, 16))
        self.label_7 = QLabel(FurnaceWireHeating)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(660, 40, 54, 16))
        self.label_8 = QLabel(FurnaceWireHeating)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(490, 40, 71, 16))
        self.hexOmitLineEdit_1 = QLineEdit(FurnaceWireHeating)
        self.hexOmitLineEdit_1.setObjectName(u"hexOmitLineEdit_1")
        self.hexOmitLineEdit_1.setGeometry(QRect(460, 70, 131, 21))
        self.hexOmitLineEdit_1.setReadOnly(True)
        self.hexLineEdit_1 = QLineEdit(FurnaceWireHeating)
        self.hexLineEdit_1.setObjectName(u"hexLineEdit_1")
        self.hexLineEdit_1.setGeometry(QRect(610, 70, 151, 21))
        self.hexLineEdit_1.setReadOnly(True)
        self.hexOmitLineEdit_2 = QLineEdit(FurnaceWireHeating)
        self.hexOmitLineEdit_2.setObjectName(u"hexOmitLineEdit_2")
        self.hexOmitLineEdit_2.setGeometry(QRect(460, 110, 131, 21))
        self.hexOmitLineEdit_2.setReadOnly(True)
        self.hexLineEdit_2 = QLineEdit(FurnaceWireHeating)
        self.hexLineEdit_2.setObjectName(u"hexLineEdit_2")
        self.hexLineEdit_2.setGeometry(QRect(610, 110, 151, 21))
        self.hexLineEdit_2.setReadOnly(True)
        self.hexOmitLineEdit_3 = QLineEdit(FurnaceWireHeating)
        self.hexOmitLineEdit_3.setObjectName(u"hexOmitLineEdit_3")
        self.hexOmitLineEdit_3.setGeometry(QRect(460, 150, 131, 21))
        self.hexOmitLineEdit_3.setReadOnly(True)
        self.hexLineEdit_3 = QLineEdit(FurnaceWireHeating)
        self.hexLineEdit_3.setObjectName(u"hexLineEdit_3")
        self.hexLineEdit_3.setGeometry(QRect(610, 150, 151, 21))
        self.hexLineEdit_3.setReadOnly(True)
        self.hexOmitLineEdit_4 = QLineEdit(FurnaceWireHeating)
        self.hexOmitLineEdit_4.setObjectName(u"hexOmitLineEdit_4")
        self.hexOmitLineEdit_4.setGeometry(QRect(460, 190, 131, 21))
        self.hexOmitLineEdit_4.setReadOnly(True)
        self.hexLineEdit_4 = QLineEdit(FurnaceWireHeating)
        self.hexLineEdit_4.setObjectName(u"hexLineEdit_4")
        self.hexLineEdit_4.setGeometry(QRect(610, 190, 151, 21))
        self.hexLineEdit_4.setReadOnly(True)
        self.hexOmitLineEdit_5 = QLineEdit(FurnaceWireHeating)
        self.hexOmitLineEdit_5.setObjectName(u"hexOmitLineEdit_5")
        self.hexOmitLineEdit_5.setGeometry(QRect(460, 230, 131, 21))
        self.hexOmitLineEdit_5.setReadOnly(True)
        self.hexLineEdit_5 = QLineEdit(FurnaceWireHeating)
        self.hexLineEdit_5.setObjectName(u"hexLineEdit_5")
        self.hexLineEdit_5.setGeometry(QRect(610, 230, 151, 21))
        self.hexLineEdit_5.setReadOnly(True)
        self.label_9 = QLabel(FurnaceWireHeating)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(50, 270, 54, 16))
        self.actionIDLineEdit = QLineEdit(FurnaceWireHeating)
        self.actionIDLineEdit.setObjectName(u"actionIDLineEdit")
        self.actionIDLineEdit.setGeometry(QRect(110, 270, 121, 21))
        self.generateIDPushButton = QPushButton(FurnaceWireHeating)
        self.generateIDPushButton.setObjectName(u"generateIDPushButton")
        self.generateIDPushButton.setGeometry(QRect(260, 270, 75, 24))
        self.commitPushButton = QPushButton(FurnaceWireHeating)
        self.commitPushButton.setObjectName(u"commitPushButton")
        self.commitPushButton.setGeometry(QRect(470, 300, 75, 24))
        self.cancelPushButton = QPushButton(FurnaceWireHeating)
        self.cancelPushButton.setObjectName(u"cancelPushButton")
        self.cancelPushButton.setGeometry(QRect(640, 300, 75, 24))

        self.retranslateUi(FurnaceWireHeating)

        QMetaObject.connectSlotsByName(FurnaceWireHeating)
    # setupUi

    def retranslateUi(self, FurnaceWireHeating):
        FurnaceWireHeating.setWindowTitle(QCoreApplication.translate("FurnaceWireHeating", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("FurnaceWireHeating", u"A\u7089\u4e1d\u52a0\u70ed\u7535\u538b\u52a8\u4f5c\u8bbe\u7f6e", None))
        self.label_2.setText(QCoreApplication.translate("FurnaceWireHeating", u"\u7089\u4e1d\u52a0\u70ed\u7535\u538b\u7247\u9009", None))
        self.checkBox_1.setText(QCoreApplication.translate("FurnaceWireHeating", u"\u7535\u538b1", None))
        self.checkBox_2.setText(QCoreApplication.translate("FurnaceWireHeating", u"\u7535\u538b2", None))
        self.checkBox_3.setText(QCoreApplication.translate("FurnaceWireHeating", u"\u7535\u538b3", None))
        self.checkBox_4.setText(QCoreApplication.translate("FurnaceWireHeating", u"\u7535\u538b4", None))
        self.label_3.setText(QCoreApplication.translate("FurnaceWireHeating", u"\u52a0\u70ed\u7535\u538b1\u8bbe\u7f6e", None))
        self.valLineEdit_1.setText(QCoreApplication.translate("FurnaceWireHeating", u"55", None))
        self.valLineEdit_2.setText(QCoreApplication.translate("FurnaceWireHeating", u"100", None))
        self.label_4.setText(QCoreApplication.translate("FurnaceWireHeating", u"\u52a0\u70ed\u7535\u538b2\u8bbe\u7f6e", None))
        self.valLineEdit_3.setText(QCoreApplication.translate("FurnaceWireHeating", u"4", None))
        self.label_5.setText(QCoreApplication.translate("FurnaceWireHeating", u"\u52a0\u70ed\u7535\u538b3\u8bbe\u7f6e", None))
        self.valLineEdit_4.setText(QCoreApplication.translate("FurnaceWireHeating", u"10", None))
        self.label_6.setText(QCoreApplication.translate("FurnaceWireHeating", u"\u52a0\u70ed\u7535\u538b4\u8bbe\u7f6e", None))
        self.label_7.setText(QCoreApplication.translate("FurnaceWireHeating", u"\u5341\u516d\u8fdb\u5236", None))
        self.label_8.setText(QCoreApplication.translate("FurnaceWireHeating", u"\u5341\u516d\u8fdb\u5236\u7f29\u5199", None))
        self.label_9.setText(QCoreApplication.translate("FurnaceWireHeating", u"\u52a8\u4f5cID", None))
        self.generateIDPushButton.setText(QCoreApplication.translate("FurnaceWireHeating", u"\u751f\u6210\u52a8\u4f5cID", None))
        self.commitPushButton.setText(QCoreApplication.translate("FurnaceWireHeating", u"\u786e\u5b9a", None))
        self.cancelPushButton.setText(QCoreApplication.translate("FurnaceWireHeating", u"\u53d6\u6d88", None))
    # retranslateUi
