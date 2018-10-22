# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import work
import time
#继承 QThread 类
class WorkmulThread(QtCore.QThread):
    """docstring for BigWorkThread"""
    #声明一个信号，同时返回一个list
    workmulfinishSignal = QtCore.pyqtSignal()
    #构造函数里增加形参
    def __init__(self, t,parent=None):
        super(WorkmulThread, self).__init__(parent)
        #储存参数
        self.t = t


    #重写 run() 函数。
    def run(self):
        print(self.t)
        work.mul_predict(str(self.t))
        self.workmulfinishSignal.emit()

