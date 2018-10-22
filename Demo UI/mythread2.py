# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import work
import time
#继承 QThread 类
class myThread2(QtCore.QThread):
    """docstring for BigWorkThread"""
    #声明一个信号，同时返回一个list，同理什么都能返回啦
    finishSignal = QtCore.pyqtSignal(list)
    #构造函数里增加形参
    def __init__(self, t,parent=None):
        super(myThread2, self).__init__(parent)
        #储存参数
        self.t = t


    #重写 run() 函数，在里面干大事。
    def run(self):
        print(self.t)
        work.dopredict(str(self.t))
        f =open('resoult_1.txt')
        resoult = ''
        for line in f:
            resoult = line
        resoult1=''
        if resoult[0:1] is str(1):
            self.finishSignal.emit(['unnormal message'])
        else:
            self.finishSignal.emit(['normal message'])
        #大事

        #大事干完了，发送一个信号告诉主线程窗口
