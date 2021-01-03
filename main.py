import sys
from PyQt5 import uic
from PyQt5.QtGui import QColor, QBrush, QPainter
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from random import randint


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


class Example(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.initUI()

    def initUI(self):
        self.setFixedSize(400, 400)
        self.pushButton.clicked.connect(self.push)
        self.painter = QPainter()
        self.objects = []

    def push(self):
        r = randint(1, 100)
        centre_x = randint(0, 400)
        centre_y = randint(0, 400)
        self.objects.append((centre_x - r // 2, centre_y - r // 2, r, r, [randint(0, 255) for i in range(3)]))
        self.update()

    def paintEvent(self, event):
        self.painter.begin(self)
        for i in range(len(self.objects)):
            colors = [randint(0, 255) for i in range(3)]
            self.painter.setBrush(QColor(*self.objects[i][4]))
            self.painter.setPen(QColor(*self.objects[i][4]))
            self.painter.drawEllipse(self.objects[i][0], self.objects[i][1], self.objects[i][2], self.objects[i][3])
        self.painter.end()
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
