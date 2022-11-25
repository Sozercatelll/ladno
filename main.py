from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QMessageBox
from PyQt5 import uic
import sys
import sqlite3 as sql

con = sql.connect('coffee.sqlite')
cur = con.cursor()


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        uic.loadUi('main.ui', self)
        self.info.clicked.connect(self.search)
        self.chang.clicked.connect(self.new)

    def search(self):
        coffee = cur.execute("""SELECT * FROM coffee""").fetchall()
        self.coffee.setColumnCount(7)
        self.coffee.setHorizontalHeaderLabels(['id', 'Название', 'Степень прожарки', 'Молотый', 'Описание вкуса',
                                               'Цена', 'Объём упаковки (гр)'])
        self.coffee.setRowCount(len(coffee))
        for i, elem in enumerate(coffee):
            for j, value in enumerate(elem):
                self.coffee.setItem(i, j, QTableWidgetItem(str(value)))

    def new(self):
        self.wnd = Changed()
        self.wnd.show()


class Changed(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.setFixedSize(self.size())
        self.add.clicked.connect(self.adder)
        self.changed.clicked.connect(self.changer)

    def adder(self):
        if len(cur.execute("""SELECT * FROM coffee
                                WHERE name = ?""", (self.name.text(),)).fetchall()) == 0:
            cur.execute("""INSERT INTO coffee(name, roasting, chop, var, price, capasity) VALUES(?, ?, ?, ?, ?, ?)""",
                        (self.name.text(), self.roasting.text(), self.chop.text(),
                         self.var.text(), self.price.text(), self.capasity.text()))
            con.commit()
            QMessageBox.about(self, 'Вы молодец', 'Кофе упешно добавлен.')
        else:
            QMessageBox.about(self, 'Не обманывайте систему,'
                                    ' а то система обманет Вас.', 'Такой кофе уже существует. '
                                                              'Единственный способ с ним взаимодействовать -'
                                                              ' это его изменение.')

    def changer(self):
        if len(cur.execute("""SELECT * FROM coffee
                                WHERE id = ?""", (self.name.text(),)).fetchall()) == 1:
            cur.execute("""UPDATE coffee
                        SET name = ?,
                        roasting = ?,
                        chop = ?,
                        var = ?,
                        price = ?,
                        capasity = ?
                        WHERE id = ?""", (self.name.text(), self.roasting.text(), self.chop.text(),
                                          self.var.text(), self.price.text(), self.capasity.text(), self.id.text()))
            con.commit()
            QMessageBox.about(self, 'Вы молодец', 'Кофе упешно изменён.')
        else:
            QMessageBox.about(self, 'Не обманывайте систему,'
                                    ' а то система обманет Вас.', 'Такого кофе нет. Если хотите,'
                                                                  ' Вы можете добавить его.')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    wnd = Window()
    wnd.show()
    sys.exit(app.exec())
