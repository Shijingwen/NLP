# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(446, 368)
        palette1 = QtGui.QPalette()
        palette1.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap('D:/Python/workplace/2.png')))  # 设置背景图片
        self.setPalette(palette1)
        self.label = QtGui.QLabel(Dialog)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(150, 10, 151, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(60, 130, 81, 31))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.textBrowser = QtGui.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(220, 80, 191, 41))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(280, 60, 81, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(70, 60, 81, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(10, 80, 191, 41))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(60, 300, 81, 31))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(70, 220, 81, 21))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.textBrowser_2 = QtGui.QTextBrowser(Dialog)
        self.textBrowser_2.setGeometry(QtCore.QRect(10, 250, 191, 41))
        self.textBrowser_2.setObjectName(_fromUtf8("textBrowser_2"))
        self.pushButton_predict = QtGui.QPushButton(Dialog)
        self.pushButton_predict.setGeometry(QtCore.QRect(270, 130, 81, 31))
        self.pushButton_predict.setObjectName(_fromUtf8("pushButton_predict"))
        self.textBrowser_3 = QtGui.QTextBrowser(Dialog)
        self.textBrowser_3.setGeometry(QtCore.QRect(220, 250, 191, 41))
        self.textBrowser_3.setObjectName(_fromUtf8("textBrowser_3"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(270, 220, 101, 21))
        self.label_5.setObjectName(_fromUtf8("label_5"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(Dialog, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.test)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.workmul)
        QtCore.QObject.connect(self.pushButton_predict, QtCore.SIGNAL(_fromUtf8("clicked()")), self.predict)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.label.setStyleSheet('''font: 75 14pt "Consolas";
                                color: white''')
        self.label_2.setStyleSheet('''font: 75 11pt \"Agency FB\";
                                color: blue''')
        self.label_3.setStyleSheet('''font: 75 11pt \"Agency FB\";
                                color: blue''')
        self.label_4.setStyleSheet('''font: 75 11pt \"Agency FB\";
                                color: blue''')
        self.label_5.setStyleSheet('''font: 75 11pt \"Agency FB\";
                                color: blue''')

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "垃圾短信分类", None))
        self.label.setText(_translate("Dialog", "欢迎使用本系统", None))
        self.pushButton.setText(_translate("Dialog", "开始判断", None))
        self.label_2.setText(_translate("Dialog", "识别结果", None))
        self.label_3.setText(_translate("Dialog", "短信内容", None))
        self.pushButton_2.setText(_translate("Dialog", "批量上传", None))
        self.label_4.setText(_translate("Dialog", "上传目录", None))
        self.pushButton_predict.setText(_translate("Dialog", "判断出错", None))
        self.label_5.setText(_translate("Dialog", "结果文件目录", None))

