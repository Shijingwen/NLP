# -*- coding: utf-8 -*-
from __future__ import print_function

from sklearn import datasets
from sklearn.cross_validation import train_test_split
from sklearn.grid_search import GridSearchCV
from sklearn.metrics import classification_report
from sklearn.svm import SVC
import jieba
import jieba.analyse
import cPickle as pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.datasets.base import Bunch
import work
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui
import os
import sys
import ui

class TestDialog(QDialog, ui.Ui_Dialog):

    def __init__(self, parent=None):
        super(TestDialog, self).__init__(parent)
        self.setupUi(self)

    def test(self):
        self.pushButton.setDisabled(True)
        faile_dialog = self.lineEdit.text()
        from mythread2 import myThread2
        self.bwThread = myThread2(QString(faile_dialog))
        self.bwThread.finishSignal.connect(self.myThread2WorkEnd)
        self.bwThread.start()

    def myThread2WorkEnd(self,ls):
        for word in ls:
             self.textBrowser.append(word)
        self.pushButton.setDisabled(False)

    @QtCore.pyqtSlot()
    def workmul(self):
        self.pushButton_2.setDisabled(True)
        tmpDir = QtGui.QFileDialog.getOpenFileName()
        if (len(tmpDir) > 0):
            self.SaveDir = tmpDir

        print (self.SaveDir)
        if not os.path.exists(self.SaveDir):
            os.mkdir(self.SaveDir)
        self.pushButton_2.setDisabled(True)
        self.textBrowser_2.append(self.SaveDir)
        from mythread import WorkmulThread
        self.bwThread = WorkmulThread(QString(self.SaveDir))
        self.bwThread.workmulfinishSignal.connect(self.workmulWorkEnd)
        self.bwThread.start()


    def workmulWorkEnd(self):
        self.textBrowser_3.append("D:/Python/workplace/resoult.txt")
        self.pushButton_2.setDisabled(False)

    def predict(self):
        faile_dialog = self.lineEdit.text()
        print (faile_dialog)

app = QApplication(sys.argv)
app.setStyleSheet('''
    QPushButton{
        background-color: blue ;
        height:50px;
        border-style: outset;
        border-width: 2px;
        border-radius: 10px;
        border-color: beige;
        font: bold 6px;
        font-family:'Microsoft YaHei';
        font-size:13px;
        color:white;
        min-width: 5em;
        padding: 6px;
    }
    QPushButton:hover {
    background-color: blue;
    border-style: inset;
    }
    QPushButton:pressed {
    background-color: rgb(224, 0, 0);
    border-style: inset;
    }
    QPushButton#cancel{
        background-color: red ;
    }
    ''')
dialog = TestDialog()
dialog.show()
app.exec_()