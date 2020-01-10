import sys
import pygame
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets, QtCore


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label = QLabel(self)
        pixmap = QPixmap('3.jpg')
        label.setPixmap(pixmap)

        self.btn = QPushButton('Выход', self)
        self.btn.resize(170, 60)
        self.btn.setStyleSheet('background-color: gray;')
        self.btn.clicked.connect(self.example)
        self.btn.move(225, 430)

        self.btn1 = QPushButton('Об авторах', self)
        self.btn1.resize(170, 60)
        self.btn1.setStyleSheet('background-color: gray;')
        self.btn1.clicked.connect(self.buts1)
        self.btn1.move(225, 305)

        self.btn2 = QPushButton('Играть', self)
        self.btn2.resize(170, 60)
        self.btn2.setStyleSheet('background-color: gray;')
        self.btn2.clicked.connect(self.buts2)
        self.btn2.move(225, 180)

        self.setGeometry(200, 200, 600, 600)
        self.setWindowTitle('Меню')
        self.setWindowIcon(QIcon())
        self.show()

    def example(self):
        message = 'Вы уверены, что хотите выйти?'
        reply = QtWidgets.QMessageBox.question(self, 'Уведомление', message,
                                               QtWidgets.QMessageBox.Yes,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            QApplication.quit()

    def buts1(self):
        self.ex3 = Example2()

    def buts2(self):
        self.ex3 = Example3()


class Example2(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label = QLabel(self)
        pixmap = QPixmap('3.jpg')
        label.setPixmap(pixmap)

        self.label = QLabel(self)
        self.label.setText(
            '<b><font size="4" color="black">!</font></b>')
        self.label.move(200, 235)

        self.labe2 = QLabel(self)
        self.labe2.setText(
            '<b><font size="4" color="black">!</font></b>')
        self.labe2.move(200, 245)

        self.labe2 = QLabel(self)
        self.labe2.setText(
            '<b><font size="4" color="black">!</font></b>')
        self.labe2.move(200, 255)

        self.labe2 = QLabel(self)
        self.labe2.setText('<b><font size="4" color="black">!</font></b>')
        self.labe2.move(200, 265)

        self.setGeometry(200, 200, 600, 600)
        self.setWindowTitle('Об авторах')
        self.setWindowIcon(QIcon())
        self.show()


class Example3(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label = QLabel(self)
        pixmap = QPixmap()
        label.setPixmap(pixmap)
        # Code game_


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
