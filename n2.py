from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5.QtGui import QPainter, QColor
import sys
from random import randint as rnd

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(500, 400, 500, 400)

        self.painter = False
        self.button = QPushButton(self)
        self.button.setText('Не нажимай на кнопку.')
        self.button.setGeometry(200, 30, 200, 30)
        self.button.move(250, 200)
        self.button.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.painter:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()

    def draw(self, qp):
        r, g, b = rnd(0, 256), rnd(0, 256), rnd(0, 256)
        qp.setBrush(QColor(r, g, b))
        qp.setPen(QColor(r, g, b))
        rad = rnd(50, 501)
        x, y = rnd(0, 500), rnd(0, 500)
        qp.drawEllipse(x, y, rad, rad)

    def paint(self):
        self.painter = True
        self.repaint()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    wnd = Window()
    wnd.show()
    sys.exit(app.exec())
