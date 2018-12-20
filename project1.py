import sys
from math import *
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('supercalc.ui', self)
        for btn in self.nums_2.buttons():
            btn.clicked.connect(self.run)

        self.btn_clear_2.clicked.connect(self.clear)

        self.btn_plus_2.clicked.connect(self.run)

        self.btn_eq_2.clicked.connect(self.result)
        self.btn_minus_2.clicked.connect(self.run)
        self.btn_mult_2.clicked.connect(self.run)
        self.btn_div_2.clicked.connect(self.run)
        self.btn_mm_2.clicked.connect(self.run)
        self.btn_backspace.clicked.connect(self.back)
        self.sin.clicked.connect(self.run)
        self.cos.clicked.connect(self.run)
        self.log.clicked.connect(self.run)
        self.fact.clicked.connect(self.run)

        self.data = ''
        self.list = []

    def clear(self):
        self.data = ''
        self.list = []
        self.table1_2.setText('0')
        self.table1_5.setText('0')

    def back(self):
        self.data = self.data[:-1]
        self.list = self.list[:-1]
        self.table1_2.setText(str(self.data))
        self.table1_5.setText(str(''.join(self.list)))

    def run(self):
        znak = ['+', '-', '*', '/', '^', 'sin', 'cos', 'log', '!']
        f = self.sender().text()
        if self.data:
            if self.data != '':
                if self.data[-1] in znak and f in znak:
                    self.data = (self.data[:-1]) + f
                else:
                    self.data = self.data + f
        else:
            self.data = f
        self.table1_2.setText(self.data)
        self.list.append(f)
        self.table1_5.setText(''.join(self.list))
        self.list2 = self.list[:-1]
        for z in self.list2:
            if z in znak and f in znak:
                self.list = self.list2
                print(self.list)
                self.list2 = []
                if z == '+':
                    ind = self.list.index(z)
                    self.list1 = ''.join(self.list[(ind + 1):])
                    self.list = ''.join(self.list[:ind])
                    self.list = [str((int(self.list[0]) + int(self.list1[0]))), f]
                elif z == '-':
                    ind = self.list.index(z)
                    self.list1 = ''.join(self.list[(ind + 1):])
                    self.list = ''.join(self.list[:ind])
                    self.list = [str((int(self.list[0]) - int(self.list1[0]))), f]
                elif z == '*':
                    ind = self.list.index(z)
                    self.list1 = ''.join(self.list[(ind + 1):])
                    self.list = ''.join(self.list[:ind])
                    self.list = [str((int(self.list[0]) * int(self.list1[0]))), f]
                elif z == '/':
                    ind = self.list.index(z)
                    self.list1 = ''.join(self.list[(ind + 1):])
                    self.list = ''.join(self.list[:ind])
                    self.list = [str((int(self.list[0]) / int(self.list1[0]))), f]
                elif z == '^':
                    ind = self.list.index(z)
                    self.list1 = ''.join(self.list[(ind + 1):])
                    self.list = ''.join(self.list[:ind])
                    self.list = [str((int(self.list[0]) ** int(self.list1[0]))), f]
            self.table1_5.setText((' ').join(self.list))
            self.data = ''.join(self.list)

    def result(self):
        znakhere = ''
        self.data1 = ''
        print(self.data)
        self.data2 = 0
        self.res = []
        self.numbers = {}
        znak = ['+', '-', '*', '/', '^', 'sin', 'cos', 'log', '!']
        for s in self.data:
            if s not in znak:
                self.data1 += s
            else:
                self.data2 = int(self.data1)
                self.data1 = ''
                self.res.append(self.data2)
                znakhere = s
                self.res.append(znakhere)
        self.res.append(int(self.data1))
        print(self.res)
        for h in self.res:
            if h not in znak:
                p1 = h
            else:
                znakhere = h
        if znakhere == '+':
            self.data2 = self.res[0] + self.res[2]
            print(1)
        elif znakhere == '-':
            self.data2 = self.res[0] - self.res[2]
            print(2)
        elif znakhere == '*':
            self.data2 = self.res[0] * self.res[2]
            print(3)
        elif znakhere == '/':
            self.data2 = self.res[0] / self.res[2]
            print(4)
        elif znakhere == '^':
            self.data2 = self.res[0] ** self.res[2]
            print(5)
        self.table1_2.setText(str(self.data2))
        self.table1_5.setText(str(self.data2))
        self.list = [self.data2]
        self.data1 = ''
        h = ''
        self.res = []
        self.data2 = 0


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
