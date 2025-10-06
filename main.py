#список покупок с БД
#шаблон https://www.pythontutorial.net
import sys
from pathlib import Path
import sqlite3
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QLineEdit, QSpinBox, QSlider, QLabel, QPushButton, \
    QListWidget


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.conn = sqlite3.connect("pokupki.db")
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS pokupki (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, price INTEGER, kolichestvo INTEGER)")
        self.cur.execute("SELECT name,price,kolichestvo FROM pokupki")
        ans = self.cur.fetchall()

        self.sum = 0
        self.setWindowTitle('Список покупок')
        layout = QGridLayout()
        self.setLayout(layout)
        self.name_entry = QLineEdit(maxLength=100,
                                    placeholderText="Название"
                                    )
        layout.addWidget(self.name_entry, 0, 0)
        self.quantity_entry = QSpinBox(
            minimum=1,
            maximum=1000,
            singleStep=10,
            suffix="руб.",
            value=100
        )
        layout.addWidget(self.quantity_entry, 1, 0)
        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.valueChanged.connect(self.show_value)
        self.slider.setTickPosition(
            QSlider.TickPosition.TicksBelow
        )
        self.slider.setRange(1, 10)
        self.slider.setSingleStep(1)
        self.slider.setPageStep(1)
        layout.addWidget(self.slider, 2, 0)
        self.value_label = QLabel("Количество:")
        layout.addWidget(self.value_label, 3, 0)
        self.add_btn = QPushButton("+")
        self.add_btn.clicked.connect(self.add_tovar)
        layout.addWidget(self.add_btn, 0, 1, 3, 1)
        self.add_btn.setFixedSize(QSize(100, 150))
        self.goods_lst = QListWidget()
        for item in ans:
            self.goods_lst.addItem(f"{item[0]} {item[1]}руб. {item[2]}")
        layout.addWidget(self.goods_lst,3,0,1,2)
        self.total = QLabel("Итого:")
        layout.addWidget(self.total,4,0)
        self.show()

    def show_value(self, value):
        print(value)
        #сюда написать значение от ползунка!

    def add_tovar(self):
        name = self.name_entry.text()
        value = self.quantity_entry.value()
        kol = self.slider.value()
        self.goods_lst.addItem(f"Название:{name}, цена: {value}, количество: {kol}")
        x = value * kol
        self.sum = self.sum + x
        self.total.setText(f"ИТОГО: {self.sum}")




if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(Path('style.qss').read_text())
    window = MainWindow()
    sys.exit(app.exec())
