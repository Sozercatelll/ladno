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
        cofe = self.cur.execute("""SELECT * FROM coffee""").fetchall()
        self.coffee.setColumnCount(7)
        self.coffee.setRowCount(1)
        print(3)
        self.coffee.setHorizontalHeaderLabels(['id', 'Название', 'Степень прожарки', 'Молотый', 'Описание вкуса',
                                               'Цена', 'Объём упаковки'])
        # for i, elem in enumerate(cofe):
        #     print('Ай')
        #     for j, value in enumerate(elem):
        #         print('Ой', end='-')
        #         self.cofye.setItem(i, j, QTableWidgetItem(str(value)))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    wnd = Window()
    wnd.show()
    sys.exit(app.exec())
