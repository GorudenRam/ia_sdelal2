import sys
from PyQt5 import uic
from PyQt5.QtGui import QColor, QBrush, QPainter
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from random import randrange


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
        r = randrange(1, 100)
        centre_x = randrange(0, 400)
        centre_y = randrange(0, 400)
        self.objects.append((centre_x - r // 2, centre_y - r // 2, r, r))
        self.update()

    def paintEvent(self, event):
        self.painter.begin(self)
        for obj in self.objects:
            self.painter.setBrush(QColor('yellow'))
            self.painter.setPen(QColor('yellow'))
            self.painter.drawEllipse(obj[0], obj[1], obj[2], obj[3])
        self.painter.end()
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
