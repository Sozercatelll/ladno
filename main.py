from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from PyQt5 import uic
import sys
import sqlite3 as sql


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        uic.loadUi('main.ui', self)
        self.con = sql.connect('coffee.sqlite')
        self.cur = self.con.cursor()
        self.info.clicked.connect(self.search)

    def search(self):
        coffee = self.cur.execute("""SELECT * FROM coffee""").fetchall()
        self.coffee.setColumnCount(7)
        self.coffee.setHorizontalHeaderLabels(['id', 'Название', 'Степень прожарки', 'Молотый', 'Описание вкуса',
                                               'Цена', 'Объём упаковки(мл)'])
        self.coffee.setRowCount(len(coffee))
        for i, elem in enumerate(coffee):
            for j, value in enumerate(elem):
                self.coffee.setItem(i, j, QTableWidgetItem(str(value)))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    wnd = Window()
    wnd.show()
    sys.exit(app.exec())
