from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
import sys


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        uic.loadUi('UI.ui', self)
        self.painter = False
        self.b1.clicked.connect(self.paint)
        self.b2.clicked.connect(self.paint)
        self.b3.clicked.connect(self.paint)
        self.b4.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.painter:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()

    def draw(self, qp):
        qp.setBrush(QColor(255, 255, 20))
        qp.setPen(QColor(255, 255, 40))
        qp.drawEllipse(30, 40, 500, 500)

    def paint(self):
        self.painter = True
        self.repaint()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    wnd = Window()
    wnd.show()
    sys.exit(app.exec())
